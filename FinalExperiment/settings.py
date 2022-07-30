from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point= 1.00, participation_fee= 4.00, doc=""
)

SESSION_CONFIGS = [
     dict(
        name='Experiment',
        display_name="Experiment",
        num_demo_participants=6,
        app_sequence=['cheating_game']
     ),
     dict(
        name='Experiment2',
        display_name="Experiment II",
        num_demo_participants=30,
        app_sequence=['cheating_game_t1']
         ),
     dict(
        name='Experiment3',
        display_name="Experiment III",
        num_demo_participants=6,
        app_sequence=['cheating_game_t2']
         )
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '3_05n63##xfw^w*e@28#!ytw%umft#a&e)zx(wv5mk--i$(@ua'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
