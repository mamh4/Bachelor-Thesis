from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'cheating_game'
    players_per_group = 2
    num_rounds = 1
    endowment = c(0)
    head_payoff = c(5)
    controlQuestion1 = "Q1) You witness ‘tails’ and report ‘tails’. Your teammate witnesses ‘tails’ and reports ‘tails’. \n What is Your Individual payoff?"
    controlQuestion2 = "Q2) You witness ‘tails’ and report ‘tails’. Your teammate witnesses ‘tails’ and reports ‘heads’. \n What is Your Individual payoff?"
    controlQuestion3 = "Q3) You witness ‘tails’ and report ‘heads’. Your teammate witnesses ‘tails’ and reports ‘tails’. \n What is Your Individual payoff?"
    
            


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    group_payoff = models.CurrencyField(label= "")


class Player(BasePlayer):
    player_report = models.IntegerField(
        choices = [[1, "Head"], [0, "Tail"]],
        label = "",
        widget = widgets.RadioSelect
        )
    report_value = models.CurrencyField(label= "")
    supervision = models.BooleanField(label = "")
    player_witness = models.IntegerField(label = "")
    wrong_clicksQ1 = models.IntegerField(label = "", initial=0)
    wrong_clicksQ2 = models.IntegerField(label = "", initial=0)
    wrong_clicksQ3 = models.IntegerField(label = "", initial=0)
    #ArrayClicks = [ wrong_clicksQ1, wrong_clicksQ2 ,wrong_clicksQ3]
    controlQuestionChoices1 = models.CurrencyField(label = "",
                                             widget = widgets.RadioSelect,
                                             choices = [c(2.5), c(5.00),c(0.00)])

    controlQuestionChoices2 = models.CurrencyField(label = "",
                                             widget = widgets.RadioSelect,
                                             choices = [c(2.5), c(5.00),c(0.00)])

    controlQuestionChoices3 = models.CurrencyField(label = "",
                                             widget = widgets.RadioSelect,
                                             choices = [c(2.5), c(5.00),c(0.00)])
    #myArray = [controlQuestionChoices1, controlQuestionChoices2, controlQuestionChoices3]
    
    
    age = models.IntegerField(
        label = "What is your age?",
        max = 100,
        min = 14
    )
    gender= models.IntegerField(
    label = "What is your gender?",
    choices= [
        [1,"Male"],[0, "Female"], [2,"Diverse"]

    ])
    nationality = models.StringField(
        choices = ["Albania",	"Algeria",	"Andorra",	"Angola",	"Antigua and Barbuda",	"Argentina",	"Armenia",	"Australia",	"Austria",	"Azerbaijan",	"Bahamas",	"Bahrain",	"Bangladesh",	"Barbados",	"Belarus",	"Belgium",	"Belize",	"Benin",	"Bhutan",	"Bolivia",	"Bosnia and Herzegovina",	"Botswana",	"Brazil",	"Brunei",	"Bulgaria",	"Burkina Faso",	"Burundi",	"Côte d'Ivoire",	"Cabo Verde",	"Cambodia",	"Cameroon",	"Canada",	"Central African Republic",	"Chad",	"Chile",	"China",	"Colombia",	"Comoros",	"Congo (Congo-Brazzaville)",	"Costa Rica",	"Croatia",	"Cuba",	"Cyprus",	"Czechia (Czech Republic)",	"Democratic Republic of the Congo",	"Denmark",	"Djibouti",	"Dominica",	"Dominican Republic",	"Ecuador",	"Egypt",	"El Salvador",	"Equatorial Guinea",	"Eritrea",	"Estonia",	"Eswatini (fmr. 'Swaziland')",	"Ethiopia",	"Fiji",	"Finland",	"France",	"Gabon",	"Gambia",	"Georgia",	"Germany",	"Ghana",	"Greece",	"Grenada",	"Guatemala",	"Guinea",	"Guinea-Bissau",	"Guyana",	"Haiti",	"Holy See",	"Honduras",	"Hungary",	"Iceland",	"India",	"Indonesia",	"Iran",	"Iraq",	"Ireland",	"Israel",	"Italy",	"Jamaica",	"Japan",	"Jordan",	"Kazakhstan",	"Kenya",	"Kiribati",	"Kuwait",	"Kyrgyzstan",	"Laos",	"Latvia",	"Lebanon",	"Lesotho",	"Liberia",	"Libya",	"Liechtenstein",	"Lithuania",	"Luxembourg",	"Madagascar",	"Malawi",	"Malaysia",	"Maldives",	"Mali",	"Malta",	"Marshall Islands",	"Mauritania",	"Mauritius",	"Mexico",	"Micronesia",	"Moldova",	"Monaco",	"Mongolia",	"Montenegro",	"Morocco",	"Mozambique",	"Myanmar (formerly Burma)",	"Namibia",	"Nauru",	"Nepal",	"Netherlands",	"New Zealand",	"Nicaragua",	"Niger",	"Nigeria",	"North Korea",	"North Macedonia",	"Norway",	"Oman",	"Pakistan",	"Palau",	"Palestine State",	"Panama",	"Papua New Guinea",	"Paraguay",	"Peru",	"Philippines",	"Poland",	"Portugal",	"Qatar",	"Romania",	"Russia",	"Rwanda",	"Saint Kitts and Nevis",	"Saint Lucia",	"Saint Vincent and the Grenadines",	"Samoa",	"San Marino",	"Sao Tome and Principe",	"Saudi Arabia",	"Senegal",	"Serbia",	"Seychelles",	"Sierra Leone",	"Singapore",	"Slovakia",	"Slovenia",	"Solomon Islands",	"Somalia",	"South Africa",	"South Korea",	"South Sudan",	"Spain",	"Sri Lanka",	"Sudan",	"Suriname",	"Sweden",	"Switzerland",	"Syria",	"Tajikistan",	"Tanzania",	"Thailand",	"Timor-Leste",	"Togo",	"Tonga",	"Trinidad and Tobago",	"Tunisia",	"Turkey",	"Turkmenistan",	"Tuvalu",	"Uganda",	"Ukraine",	"United Arab Emirates",	"United Kingdom",	"United States of America",	"Uruguay",	"Uzbekistan",	"Vanuatu",	"Venezuela",	"Vietnam",	"Yemen",	"Zambia",	"Zimbabwe"],
        
        label = "What is your country of citizenship?"
    )
    
    #headsTailsDic = {"heads": 1, "tails" : 0}
    intention = models.TextField(#We do not want to make it compulsory
        label = "", #print("You witnessed ", headsTailsDic[player_witness], " but reported ", headsTailsDic[player_report], "please explain your intention.")
        blank = "True" #This allows user to continue without filling up the comment section
    )

    comment = models.TextField(#We do not want to make it compulsory
        label = "Were the instructions clear? If not, please explain why.",
        blank = "True" #This allows user to continue without filling up the comment section
    )


