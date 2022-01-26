from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'input_calculation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    APR = 0.07


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    amount = models.CurrencyField(min=0, max=100000)
    num_years = models.IntegerField(min=1, max=50)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['amount', 'num_years']

    @staticmethod
    def js_vars(player: Player):
        return dict(APR=C.APR)


page_sequence = [MyPage]
