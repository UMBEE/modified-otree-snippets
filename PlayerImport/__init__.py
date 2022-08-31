from otree.api import *
from PlayerImport.intro_player import Player


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'PlayerImport'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
