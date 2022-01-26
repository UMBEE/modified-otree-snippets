from otree.api import *


doc = """
Your app description
"""


class EXP_DemandFunction:
    high_demand_max = 100
    high_demand_price_coef = -1
    low_demand_max  = 100
    low_demand_price_coef = -2
    def high_demand(price):
        return high_demand_max + high_demand_price_coef * price

    def low_demand(price):
        return low_demand_max + low_demand_price_coef * price



#
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
    quantity = models.IntegerField(min=0)
    price = models.FloatField(min=0)

    amount = models.CurrencyField(min=0, max=100000)
    num_years = models.IntegerField(min=1, max=50)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['quantity', 'price', ]

    @staticmethod
    def js_vars(player: Player):
        return dict(APR=C.APR)


class PQDecision(ExtraModel):
    player = models.Link(Player)
    image_id = models.IntegerField()
    decoy_text = models.StringField()
    color = models.StringField()
    is_correct = models.BooleanField()
    is_congruent = models.BooleanField()
    reaction_ms = models.IntegerField()

def live_method(player: Player, data):
    # Do the calculation using native Python function

    if data:
        if is_finished(player):
            return
        trial = get_current_trial(player)

        displayed_timestamp = data['displayed_timestamp']
        answered_timestamp = data['answered_timestamp']
        trial.submission = data['submission']

        trial.is_correct = trial.submission == trial.color
        trial.reaction_ms = answered_timestamp - displayed_timestamp

        if trial.is_correct:
            player.num_correct += 1
            feedback = '✓'
        else:
            feedback = '✗'
        player.num_completed += 1

    else:
        feedback = ''

    if is_finished(player):
        return {player.id_in_group: dict(is_finished=True)}

    payload = dict(feedback=feedback, image_id=get_current_trial(player).image_id)
    return {player.id_in_group: payload}




page_sequence = [MyPage]
