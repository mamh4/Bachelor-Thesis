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
    name_in_url = 'cheating_game_t1'
    players_per_group = 2
    num_rounds = 1
    endowment = c(0)
    head_payoff = c(5)
    controlQuestion1 = "Q1) You witness ‘tails’ and report ‘tails’. Your teammate witnesses ‘tails’ and reports ‘tails’. \n What is Your Individual payoff?"
    controlQuestion2 = "Q2) You witness ‘tails’ and report ‘tails’. Your teammate witnesses ‘tails’ and reports ‘heads’. Your teammate is supervised. \n What is Your Individual payoff?"
    controlQuestion3 = "Q3) You witness ‘tails’ and report ‘heads’. Your teammate witnesses ‘tails’ and reports ‘tails’. you are supervised. \n What is Your Individual payoff?"
     
class Subsession(BaseSubsession):
    def creating_session(self):
        for group in self.get_groups():
            p1 = group.get_player_by_id(1)
            p2 = group.get_player_by_id(2)
            value1 = random.randrange(0,100,1)
            value2 = random.randrange(0,100,1)
            if value1<50 and value2 <50:
                group.group_supervised = True
                p1.supervision= True
                p2.supervision= False
            if value1<50 and value2 >50:
                group.group_supervised = True
                p1.supervision= False
                p2.supervision= True
            if value1>50:
                group.group_supervised = False
                p1.supervision= False
                p2.supervision= False


class Group(BaseGroup):
    group_payoff = models.CurrencyField(label= "")
    group_supervised = models.BooleanField(label="")




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
                                             choices = [c(2.5), c(5.00),c(-1.00)])

    controlQuestionChoices3 = models.CurrencyField(label = "",
                                             widget = widgets.RadioSelect,
                                             choices = [c(-1.00), c(5.00),c(0.00)])
    #myArray = [controlQuestionChoices1, controlQuestionChoices2, controlQuestionChoices3]
    intention = models.TextField(#We do not want to make it compulsory
        label = "", #print("You witness ", headsTailsDic[player_witness], " and report ", headsTailsDic[player_report], "please explain your intention.")
        blank = "True" #This allows user to continue without filling up the comment section
    )
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
        choices = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"],
        label = "What is your country of citizenship?"
    )
    comment = models.TextField(#We do not want to make it compulsory
        label = "Were the instructions clear? If not, please explain why.",
        blank = "True" #This allows user to continue without filling up the comment section
    )