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



#
class C(BaseConstants):
    NAME_IN_URL = 'input_calculation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # Parameters of the dumb demand function
    HIGH_DEMAND_MAX = 100
    HIGH_DEMAND_PRICE_COEF = -1
    LOW_DEMAND_MAX  = 50
    LOW_DEMAND_PRICE_COEF = -2

    COST_PER_UNIT = 5
    


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    for p in subsession.get_players():
        p.calculator_log = ""



class Group(BaseGroup):
    pass

def calculate_profit(price, cost, units_sold, units_produced):
    return units_sold * price - cost * units_produced

class Player(BasePlayer):
    # Note, these are all vars that are round-specific
    # These model fields will be logged, for each round of the app.
    quantity = models.IntegerField(min=0)
    price = models.FloatField(min=0)
    profit = models.FloatField(min=0)
    high_demand_status = models.BooleanField()
    calculator_log = models.StringField()

    def random_init_instance():
        return random.Random(player.participant.label)
    def check_if_high_demand_status():
        player_specific_random_instance = player.random_init_instance()
        # Then, make use of the random instance to decide on the status of demand
        high_demand_status = player_specific_random_instance.randint(0, 1)   
        return high_demand_status == 1

    @staticmethod
    def calc_player_profit(player): 
        if player.check_if_high_demand_status(player):
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


    def calc_high_demand_profit(player):
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


    def calc_low_demand_profit(player):
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

        

    @staticmethod
    def log_player_attempt(player):
        player.calculator_log += f"p={player.price},q={player.quantity},t={time.time()};"
        print("Log added")




# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['quantity', 'price']

    @staticmethod
    def before_next_page(player):
        # Label the clicktime
        player.calc_player_profit(player)

    @staticmethod
    def live_method(player,data):
        # Upon receiving the data, do the following
        player.price = data['price_set']
        player.quantity = data['quantity_set']
        player.log_player_attempt(player)
        return {player.id_in_group:
                {
                'high_demand_profit': player.calc_high_demand_profit(),
                'low_demand_profit': player.calc_low_demand_profit()
                }
                }
        

    @staticmethod
    def vars_for_template(player):
        return dict(
                cost_per_unit =  C.COST_PER_UNIT,
                HIGH_DEMAND_MAX = 100,
                HIGH_DEMAND_PRICE_COEF = -1,
                LOW_DEMAND_MAX  = 50,
                LOW_DEMAND_PRICE_COEF = -2,
                )




def live_method(player: Player, data):
    # Do the calculation using native Python function
    # Restricted by the Javascript conditions, we 
    # if data:
    #     if is_finished(player):
    #         return

    # if is_finished(player):
    #     return {player.id_in_group: dict(is_finished=True)}



    print("triggering the live_method")
    return {
            player.id_in_group:  "something back"
            # {
            #     'high_demand_profit': 100,
            #     'low_demand_profit': 50
            #     }
            }




page_sequence = [MyPage]
