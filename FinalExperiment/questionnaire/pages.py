from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire(Page): #same as html file name
    form_model = "player" #still do not understand, I know the class is important for the logic of the html but..?
    form_fields = ["age", "gender","nationality", "comment"]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass
class Payoff(Page):
    pass


page_sequence = [Questionnaire, Payoff] #remember to include it in pages ;)
