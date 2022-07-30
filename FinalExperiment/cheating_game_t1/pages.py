from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


#def detection():  
#    value = random.randrange(0,100,1)
#    if value < 21:
#        supervision = True
#    else:
#        supervision = False
#    return(supervision)
##def vars_for_template(self):
 ##       p1 = self.group.get_player_by_id(1)
 ##       p2 = self.group.get_player_by_id(2)         

##        value1 = random.randrange(0,100,1)
  ##      value2 = random.randrange(0,100,1)
    ##    if value1 < 50 and value2 < 50 :
      ##      self.group.group_supervised = True
            #p1p2Dic = {"player_1": p1,"player_2":p2}
            #p1p2Dic[random.choice(["player_1", "player_2"])].supervision = True#so that it appears in data
        ##  supervision = True
          ##  p1.supervision = True
            ##p2.supervision = False
           ## player_supervised="p1 supervised"
        ##if value1 < 50 and value2 > 50:
          ##  self.group.group_supervised = True
           ## supervision = True
           ## p2.supervision = True
            ##p1.supervision = False
           ## player_supervised="p2 supervised"
       ## if value1 > 50:
         ##   p1.supervision = False
          ##  p2.supervision = False
           ## supervision = False
           ## player_supervised= False
         ##   self.group.group_supervised = False#so that it appears in data
       ## return{"supervision":supervision, "player_seen":player_supervised}
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
            
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)
            
        isGroupSupervised = self.group.group_supervised
        isP1Supervised= p1.supervision
        isP2Supervised= p2.supervision
        
        
       ## return {"coin_toss": witness, "supervision": vars_for_template(self)["supervision"], "film": video, "player_seen":vars_for_template(self)["player_seen"]}
    
        return {"coin_toss": witness, "film": video, "p1supervision":isP1Supervised, "p2supervision":isP2Supervised, "groupsupervision": isGroupSupervised}
    timeout_seconds = 12.5
    
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
            
    #     p1 = self.group.get_player_by_id(1)
    #     p2 = self.group.get_player_by_id(2)
            
    #     isGroupSupervised = self.group.group_supervised
    #     isP1Supervised= p1.supervision
    #     isP2Supervised= p2.supervision
        
        
    #    ## return {"coin_toss": witness, "supervision": vars_for_template(self)["supervision"], "film": video, "player_seen":vars_for_template(self)["player_seen"]}
    
    #     return {"coin_toss": witness, "film": video, "p1supervision":isP1Supervised, "p2supervision":isP2Supervised, "groupsupervision": isGroupSupervised}

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        p1 = self.group.get_player_by_id(1)
        p2 = self.group.get_player_by_id(2)        
        
        ##
        if p1.player_report == 1 and p2.player_report == 1 and p1.supervision == False and p2.supervision == False:
            p1.report_value = c(5)
            p2.report_value = c(5)
            p1.payoff= c(5) + Constants.endowment
            p2.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff
            
            
        if p1.player_report == 0 and p2.player_report == 0 and p1.supervision == False and p2.supervision == False:
            p1.report_value = c(0)
            p2.report_value = c(0)
            p1.payoff= c(0) + Constants.endowment
            p2.payoff= c(0) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff
            
            
            
        if p1.player_report == 1 and p2.player_report == 0 and p1.supervision == False and p2.supervision == False:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff            
            

        if p1.player_report == 0 and p2.player_report == 1 and p1.supervision == False and p2.supervision == False:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff
         
        ##Witness p1
            
        if p1.player_report == 1 and p2.player_report == 0 and p1.supervision == True and p2.supervision == False and p1.player_witness == 1:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff            
            
        if p1.player_report == 1 and p2.player_report == 1 and p1.supervision == True and p2.supervision == False and p1.player_witness == 1:
            p1.report_value = c(5)
            p2.report_value = c(5)
            p1.payoff= c(5) + Constants.endowment
            p2.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff

        if p1.player_report == 0 and p2.player_report == 1 and p1.supervision == True and p2.supervision == False and p1.player_witness == 1:
            p1.report_value = c(1.5)
            p2.report_value = c(2.5)
            p1.payoff= c(1.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff             

        if p1.player_report == 1 and p2.player_report == 1 and p1.supervision == True and p2.supervision == False and p1.player_witness == 0:
            p1.report_value = c(1.5)
            p2.report_value = c(5)
            p1.payoff= c(1.5) + Constants.endowment
            p2.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff
            
        if p1.player_report == 0 and p2.player_report == 0 and p1.supervision == True and p2.supervision == False and p1.player_witness == 1:
            p1.report_value = c(-1.00)
            p2.report_value = c(0.00)
            p1.payoff= c(-1.00) + Constants.endowment
            p2.payoff= c(0.00) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff  

        if p1.player_report == 1 and p2.player_report == 0 and p1.supervision == True and p2.supervision == False and p1.player_witness == 0:
            p1.report_value = c(-1.0)
            p2.report_value = c(2.5)
            p1.payoff= c(-1.0) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff


        if p1.player_report == 0 and p2.player_report == 1 and p1.supervision == True and p2.supervision == False and p1.player_witness == 0:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff  
            
        if p1.player_report == 0 and p2.player_report == 0 and p1.supervision == True and p2.supervision == False and p1.player_witness == 0:
            p1.report_value = c(0.00)
            p2.report_value = c(0.00)
            p1.payoff= c(0.00) + Constants.endowment
            p2.payoff= c(0.00) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff              
        
        #witness p2    
        

        if p2.player_report == 1 and p1.player_report == 0 and p2.supervision == True and p1.supervision == False and p2.player_witness == 1:
            p2.report_value = c(2.5)
            p1.report_value = c(2.5)
            p2.payoff= c(2.5) + Constants.endowment
            p1.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff            
            
        if p2.player_report == 1 and p1.player_report == 1 and p2.supervision == True and p1.supervision == False and p2.player_witness == 1:
            p2.report_value = c(5)
            p1.report_value = c(5)
            p2.payoff= c(5) + Constants.endowment
            p1.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff

        if p2.player_report == 0 and p1.player_report == 1 and p2.supervision == True and p1.supervision == False and p2.player_witness == 1:
            p2.report_value = c(1.5)
            p1.report_value = c(2.5)
            p2.payoff= c(1.5) + Constants.endowment
            p1.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff             

        if p2.player_report == 1 and p1.player_report == 1 and p2.supervision == True and p1.supervision == False and p2.player_witness == 0:
            p2.report_value = c(1.5)
            p1.report_value = c(5)
            p2.payoff= c(1.5) + Constants.endowment
            p1.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff
            
        if p2.player_report == 0 and p1.player_report == 0 and p2.supervision == True and p1.supervision == False and p2.player_witness == 1:
            p2.report_value = c(-1.00)
            p1.report_value = c(0.00)
            p2.payoff= c(-1.00) + Constants.endowment
            p1.payoff= c(0.00) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff  

        if p2.player_report == 1 and p1.player_report == 0 and p2.supervision == True and p1.supervision == False and p2.player_witness == 0:
            p2.report_value = c(-1.0)
            p1.report_value = c(2.5)
            p2.payoff= c(-1.0) + Constants.endowment
            p1.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff


        if p2.player_report == 0 and p1.player_report == 1 and p2.supervision == True and p1.supervision == False and p2.player_witness == 0:
            p2.report_value = c(2.5)
            p1.report_value = c(2.5)
            p2.payoff= c(2.5) + Constants.endowment
            p1.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff  
            
        if p2.player_report == 0 and p1.player_report == 0 and p2.supervision == True and p1.supervision == False and p2.player_witness == 0:
            p2.report_value = c(0.00)
            p1.report_value = c(0.00)
            p2.payoff= c(0.00) + Constants.endowment
            p1.payoff= c(0.00) + Constants.endowment
            self.group.group_payoff = p2.payoff + p1.payoff   
            

            
            ##p2 and p1 witness
       
        if p1.player_report == 1 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 1:
            p1.report_value = c(5)
            p2.report_value = c(5)
            p1.payoff= c(5) + Constants.endowment
            p2.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff           
        
        if p1.player_report == 1 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 1:
            p1.report_value = c(1.5)
            p2.report_value = c(5)
            p1.payoff= c(1.5) + Constants.endowment
            p2.payoff= c(5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff          
        
        if p1.player_report == 1 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 0:
            p1.report_value = c(5)
            p2.report_value = c(1.5)
            p1.payoff= c(5) + Constants.endowment
            p2.payoff= c(1.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff  
            
        if p1.player_report == 1 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 0:
            p1.report_value = c(1.5)
            p2.report_value = c(1.5)
            p1.payoff= c(1.5) + Constants.endowment
            p2.payoff= c(1.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff              
            
        if p1.player_report == 0 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 0:
            p1.report_value = c(0)
            p2.report_value = c(0)
            p1.payoff= c(0) + Constants.endowment
            p2.payoff= c(0) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff              

        if p1.player_report == 0 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 0:
            p1.report_value = c(-1.00)
            p2.report_value = c(0)
            p1.payoff= c(-1.00) + Constants.endowment
            p2.payoff= c(0) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff  


        if p1.player_report == 0 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 1:
            p1.report_value = c(0)
            p2.report_value = c(-1.00)
            p1.payoff= c(0) + Constants.endowment
            p2.payoff= c(-1.00) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff   
            
        if p1.player_report == 0 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 1:
            p1.report_value = c(-1.00)
            p2.report_value = c(-1.00)
            p1.payoff= c(-1.00) + Constants.endowment
            p2.payoff= c(-1.00) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff        
           

        if  p1.player_report == 1 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 1:
            p1.report_value = c(2.5)
            p2.report_value = c(1.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(1.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff           
        
        if p1.player_report == 0 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 1:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff          
        
        if p1.player_report == 1 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 0:
            p1.report_value = c(2.5)
            p2.report_value = c(2.5)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff  
            
        if p1.player_report == 0 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 0:
            p1.report_value = c(2.5)
            p2.report_value = c(-1.00)
            p1.payoff= c(2.5) + Constants.endowment
            p2.payoff= c(-1.00) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff              
            
        if p1.player_report == 1 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 0:
            p1.report_value = c(-1.00)
            p2.report_value = c(2.5)
            p1.payoff= c(-1.00) + Constants.endowment
            p2.payoff= c(2.5) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff              

        if p1.player_report == 0 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 0:
            p1.report_value = c(1.50)
            p2.report_value = c(-1.00)
            p1.payoff= c(1.50) + Constants.endowment
            p2.payoff= c(-1.00) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff  


        if p1.player_report == 1 and p2.player_report == 0 and p1.supervision == True and p2.supervision == True and p1.player_witness == 0 and p2.player_witness == 1:
            p1.report_value = c(-1.00)
            p2.report_value = c(1.50)
            p1.payoff= c(-1.00) + Constants.endowment
            p2.payoff= c(1.50) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff   
            
        if p1.player_report == 0 and p2.player_report == 1 and p1.supervision == True and p2.supervision == True and p1.player_witness == 1 and p2.player_witness == 1:
            p1.report_value = c(1.50)
            p2.report_value = c(2.50)
            p1.payoff= c(1.50) + Constants.endowment
            p2.payoff= c(2.50) + Constants.endowment
            self.group.group_payoff = p1.payoff + p2.payoff             
            

class Results(Page):
    pass  

class Welcome(Page):
    pass
    ##def vars_for_template(self):
 ##       p1 = self.group.get_player_by_id(1)
 ##       p2 = self.group.get_player_by_id(2)         

##        value1 = random.randrange(0,100,1)
  ##      value2 = random.randrange(0,100,1)
    ##    if value1 < 50 and value2 < 50 :
      ##      self.group.group_supervised = True
            #p1p2Dic = {"player_1": p1,"player_2":p2}
            #p1p2Dic[random.choice(["player_1", "player_2"])].supervision = True#so that it appears in data
        ##  supervision = True
          ##  p1.supervision = True
            ##p2.supervision = False
           ## player_supervised="p1 supervised"
        ##if value1 < 50 and value2 > 50:
          ##  self.group.group_supervised = True
           ## supervision = True
           ## p2.supervision = True
            ##p1.supervision = False
           ## player_supervised="p2 supervised"
       ## if value1 > 50:
         ##   p1.supervision = False
          ##  p2.supervision = False
           ## supervision = False
           ## player_supervised= False
         ##   self.group.group_supervised = False#so that it appears in data
       ## return{"supervision":supervision, "player_seen":player_supervised}

class Questionnaire(Page):
    form_model = "player" #still do not understand, I know the class is important for the logic of the html but..?
    form_fields = ["age", "gender","nationality", "comment", "intention"]
class ControlQuestions(Page):
    form_model = "player"
    form_fields = ["controlQuestionChoices1","controlQuestionChoices2", "controlQuestionChoices3"]    
  

    
    def error_message(self, values):#Validation
        print('values is', values)
        solutions = [c(0),c(2.5),c(-1.00)]
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

