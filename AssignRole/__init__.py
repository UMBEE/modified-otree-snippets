from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'AssignRole'
    PLAYERS_PER_GROUP = 8
    NUM_ROUNDS = 1
    A_ROLE = "A"
    B_ROLE = "B"

def creating_session(subsession):
    subsession.group_randomly()
    for player in subsession.get_players():
        print(player.role)

    print('a new draw')
    subsession.group_randomly()
    for player in subsession.get_players():
        print(player.role)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['role']


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
