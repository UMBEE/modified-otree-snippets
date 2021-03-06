from otree.api import *

doc = """Detect and block mobile browsers (original source: https://www.otreehub.com/projects/otree-snippets/ by Chris @ oTree
        & measure the window inner size (modified by Linfeng & Seura @ UMBEE)"""


class C(BaseConstants):
    NAME_IN_URL = 'detect_mobile'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    is_mobile = models.BooleanField()
    window_width = models.IntegerField()
    window_height = models.IntegerField()
    user_agent_str = models.StringField()


# PAGES
class MobileCheck(Page):
    form_model = 'player'
    form_fields = ['is_mobile', 'window_width', 'window_height', 'user_agent_str']

    def error_message(player: Player, values):
        if values['is_mobile']:
            return "Sorry, this experiment does not allow mobile browsers."


class Task(Page):
    pass


page_sequence = [MobileCheck, Task]
