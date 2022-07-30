from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
        
class game(Page):
    form_model = "player"
    form_fields = ["player_report"]
    
    
    # def vars_for_template(self):#We identify what we have in the html in the return function in "" and the return brackets are curly unlike normal brackets or dict() since the function returns a dictionary.
    #     if random.choice([1, 0]) == 1:
    #         self.player.player_witness  = 1
    #         witness = 1
    #         video = 'global/giphy2.gif'
    #     else:
    #         self.player.player_witness  = 0
    #         witness = 0
    #         video = 'global/giphy.gif'
        
    #     return {"coin_toss": witness,"film": video}
    

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)


##
        if p1.player_report == 1 and p2.player_report == 1:
            p1.report_value = c(5)
            p2.report_value = c(5)
            p1.payoff= c(5) + Constants.endowment
            p2.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff
            
            
        if p1.player_report == 0 and p2.player_report == 0:
            p1.report_value = c(0)
            p2.report_value = c(0)
            p1.payoff= c(0) + Constants.endowment
            p2.payoff= c(0) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff
            
            
            
        if p1.player_report == 1 and p2.player_report == 0:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff            
            

        if p1.player_report == 0 and p2.player_report == 1:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff
        
##        

        


class Results(Page):
    pass

class Welcome(Page):
    pass

class video(Page):
        
    def vars_for_template(self):#We identify what we have in the html in the return function in "" and the return brackets are curly unlike normal brackets or dict() since the function returns a dictionary.
        if random.choice([1, 0]) == 1:
            self.player.player_witness  = 1
            witness = 1
            video = 'global/giphy2.gif'
        else:
            self.player.player_witness  = 0
            witness = 0
            video = 'global/giphy.gif'
        
        return {"coin_toss": witness,"film": video}
    timeout_seconds = 12.5

class Questionnaire(Page):
    form_model = "player" #still do not understand, I know the class is important for the logic of the html but..?
    form_fields = ["age", "gender","nationality", "comment", "intention"]
class ControlQuestions(Page):
    form_model = "player"
    form_fields = ["controlQuestionChoices1","controlQuestionChoices2", "controlQuestionChoices3"]    
  

    
    def error_message(self, values):#Validation
        print('values is', values)
        solutions = [c(0),c(2.5),c(2.5)]
        if values['controlQuestionChoices1'] != solutions[0] and values['controlQuestionChoices2'] == solutions[1] and values['controlQuestionChoices3'] == solutions[2]:
            self.player.wrong_clicksQ1 = 1 + self.player.wrong_clicksQ1
            return 'Revise question 1, take another look at the cheat sheet!'
        if values['controlQuestionChoices1'] != solutions[0] and values['controlQuestionChoices2'] != solutions[1] and values['controlQuestionChoices3'] == solutions[2]:
            self.player.wrong_clicksQ1 = 1 + self.player.wrong_clicksQ1
            self.player.wrong_clicksQ2 = 1 + self.player.wrong_clicksQ2
            return 'Revise question 1 and question 2, take another look at the cheat sheet!'
        if values['controlQuestionChoices1'] != solutions[0] and values['controlQuestionChoices2'] != solutions[1] and values['controlQuestionChoices3'] != solutions[2]:
            self.player.wrong_clicksQ1 = 1 + self.player.wrong_clicksQ1
            self.player.wrong_clicksQ2 = 1 + self.player.wrong_clicksQ2
            self.player.wrong_clicksQ3 = 1 + self.player.wrong_clicksQ3
            return 'Revise question 1, question 2 and question 3, take another look at the cheat sheet!'
        if values['controlQuestionChoices1'] == solutions[0] and values['controlQuestionChoices2'] != solutions[1] and values['controlQuestionChoices3'] == solutions[2]:
            self.player.wrong_clicksQ2 = 1 + self.player.wrong_clicksQ2
            return 'Revise question 2, take another look at the cheat sheet!'        
        if values['controlQuestionChoices1'] == solutions[0] and values['controlQuestionChoices2'] != solutions[1] and values['controlQuestionChoices3'] != solutions[2]:
            self.player.wrong_clicksQ2 = 1 + self.player.wrong_clicksQ2
            self.player.wrong_clicksQ3 = 1 + self.player.wrong_clicksQ3
            return 'Revise question 2 and question 3 take another look at the cheat sheet!'      
        if values['controlQuestionChoices1'] == solutions[0] and values['controlQuestionChoices2'] == solutions[1] and values['controlQuestionChoices3'] != solutions[2]:
            self.player.wrong_clicksQ3 = 1 + self.player.wrong_clicksQ3
            return 'Revise question 3, take another look at the cheat sheet!'
        if values['controlQuestionChoices1'] != solutions[0] and values['controlQuestionChoices2'] == solutions[1] and values['controlQuestionChoices3'] != solutions[2]:
            self.player.wrong_clicksQ3 = 1 + self.player.wrong_clicksQ3
            return 'Revise question 1 and question 3, take another look at the cheat sheet!' 

             
        



page_sequence = [ControlQuestions, video ,game, Questionnaire, ResultsWaitPage,Results]
