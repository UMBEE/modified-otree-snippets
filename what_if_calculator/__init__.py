from otree.api import *
import time

import random


doc = """
This is a demo of a calculator, used in a pricing experiment. Subjects are to
face a high or low demand with equal chance. The calculator computes the profit
for each case.
"""


class EXP_DemandFunction:
    def high_demand(price):
        quantity_sold =  C.HIGH_DEMAND_MAX + C.HIGH_DEMAND_PRICE_COEF * price
        if quantity_sold < 0:
            return 0
        else:
            return quantity_sold

    def low_demand(price):
        quantity_sold = C.LOW_DEMAND_MAX + C.LOW_DEMAND_PRICE_COEF * price
        if quantity_sold < 0:
            return 0
        else:
            return quantity_sold

def calculate_profit(price, cost, units_sold, units_produced):
    return units_sold * price - cost * units_produced

#
class C(BaseConstants):
    NAME_IN_URL = 'input_calculation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Parameters of the simple demand function
    HIGH_DEMAND_MAX = 100
    HIGH_DEMAND_PRICE_COEF = -1
    LOW_DEMAND_MAX  = 50
    LOW_DEMAND_PRICE_COEF = -2
    COST_PER_UNIT = 5
    


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        # Initialize the log-collecting tool.
        p.calculator_log = ""



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Note, these are all vars that are round-specific
    # These model fields will be logged, for each round of the app.
    quantity = models.IntegerField(min=0)
    price = models.FloatField(min=0)
    profit = models.FloatField(min=0)
    high_demand_status = models.BooleanField()
    calculator_log = models.StringField()


    

def log_player_attempt(player:Player):
    player.calculator_log += f"p={player.price},q={player.quantity},t={time.time()};"
    print("Log added")

def calc_player_profit(player:Player): 
    if check_if_high_demand_status(player):
        amount_sold = min(
                player.quantity, # Amount subject chose as quantity
                EXP_DemandFunction.high_demand(player.price) # Demand amount
                ) 
    else:
        amount_sold = min(
                player.quantity, 
                EXP_DemandFunction.low_demand(player.price)
                )
    player.profit = calculate_profit(
            price = player.price,
            cost = C.COST_PER_UNIT,
            units_sold = amount_sold,
            units_produced = player.quantity,
            )

def calc_high_demand_profit(player:Player):
    amount_sold = min(
            player.quantity, # Amount subject chose as quantity
            EXP_DemandFunction.high_demand(player.price) # Demand amount
            ) 
    print(dict(
            price = player.price,
            cost = C.COST_PER_UNIT,
            units_sold = amount_sold,
            units_produced = player.quantity,
        )
        )
    return calculate_profit(
            price = player.price,
            cost = C.COST_PER_UNIT,
            units_sold = amount_sold,
            units_produced = player.quantity,
            )


def calc_low_demand_profit(player:Player):
    amount_sold = min(
            player.quantity, 
            EXP_DemandFunction.low_demand(player.price)
            )
    print(dict(
            price = player.price,
            cost = C.COST_PER_UNIT,
            units_sold = amount_sold,
            units_produced = player.quantity,
        )
        )
    return calculate_profit(
            price = player.price,
            cost = C.COST_PER_UNIT,
            units_sold = amount_sold,
            units_produced = player.quantity,
            )


# For deciding which demand function the subject is assigned to.
def random_init_instance(player:Player):
    # Note, we initialize a "fixed" random state for each subject, pertaining to the participant.label
    return random.Random(player.participant.label)
def check_if_high_demand_status(player:Player):
    player_specific_random_instance = random_init_instance()
    # Then, make use of the random instance to decide on the status of demand
    high_demand_status = player_specific_random_instance.randint(0, 1)   
    return high_demand_status == 1







def live_method(player:Player,data):
    # Upon receiving the data, do the following
    player.price = data['price_set']
    player.quantity = data['quantity_set']
    log_player_attempt(player)
    return {player.id_in_group:
            {
            'high_demand_profit': calc_high_demand_profit(player),
            'low_demand_profit': calc_low_demand_profit(player)
            }
            }



# PAGES
class MyPage(Page):
    live_method = live_method
    form_model = 'player'
    form_fields = ['quantity', 'price']

    @staticmethod
    def before_next_page(player):
        # Label the clicktime
        calc_player_profit(player)
        

    @staticmethod
    def vars_for_template(player):
        return dict(
                cost_per_unit =  C.COST_PER_UNIT,
                HIGH_DEMAND_MAX = 100,
                HIGH_DEMAND_PRICE_COEF = -1,
                LOW_DEMAND_MAX  = 50,
                LOW_DEMAND_PRICE_COEF = -2,
                )


page_sequence = [MyPage]
