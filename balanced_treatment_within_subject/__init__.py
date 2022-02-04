from otree.api import *
import itertools

doc = """
Within-subject design, with three treatment conditions. Orders of the treatment
will be balanced as long as the subjects arrive in multiples of 6.
"""


class C(BaseConstants):
    NAME_IN_URL = 'balanced_treatment_within_subject'
    PLAYERS_PER_GROUP = None
    # On treatment and how they repeat
    NUM_Repeated_Rounds_Treatment_Condition = 10
    NUM_Treatment_Conditions = 3
    # On what to show before/after the rounds
    NUM_LeaderPage = 1
    NUM_FinishPage = 1

    # Welcome page + ROUNDS + Results page
    NUM_ROUNDS = (
              NUM_LeaderPage               # Start page
            + NUM_Treatment_Conditions     #Intro for each treatment
            + NUM_Repeated_Rounds_Treatment_Condition * NUM_Treatment_Conditions
            + NUM_FinishPage               # Finish page
            )

    ROUNDS_for_TreatmentIntro = [
            # Here, name the rounds in which TreatmentIntro needs to be displayed
            (NUM_LeaderPage                                              + 1),
            # Then, 
            (
            NUM_LeaderPage + 1 + NUM_Repeated_Rounds_Treatment_Condition 
                                                                         + 1),
            (
            NUM_LeaderPage + 1 + NUM_Repeated_Rounds_Treatment_Condition 
                           + 1 + NUM_Repeated_Rounds_Treatment_Condition + 1)
            ]

    FULL_list_of_rounds = list(range(1,NUM_ROUNDS + 1))
    ROUNDS_for_T1 = FULL_list_of_rounds[ROUNDS_for_TreatmentIntro[0] : ROUNDS_for_TreatmentIntro[0] + NUM_Repeated_Rounds_Treatment_Condition]
    ROUNDS_for_T2 = FULL_list_of_rounds[ROUNDS_for_TreatmentIntro[1] : ROUNDS_for_TreatmentIntro[1] + NUM_Repeated_Rounds_Treatment_Condition]
    ROUNDS_for_T3 = FULL_list_of_rounds[ROUNDS_for_TreatmentIntro[2] : ROUNDS_for_TreatmentIntro[2] + NUM_Repeated_Rounds_Treatment_Condition]
    ROUND_for_FinishPage = NUM_ROUNDS
    # Parameters of the simple demand function

    print(ROUNDS_for_TreatmentIntro)
    print(ROUNDS_for_T1)
    print(ROUNDS_for_T2)
    print(ROUNDS_for_T3)

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    treatments = itertools.cycle(
            itertools.permutations([1,2,3])
            )
    if subsession.round_number == 1:
        for p in subsession.get_players():
            treatment = next(treatments)
            # print('treatment is', treatment)
            p.participant.treatment_sequence = treatment # Log the assigned treatment ordering


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment_sequence = models.StringField()
    worker_page_choice = models.BooleanField(initial=0)


# PAGES
class WelcomePage(Page):
    def vars_for_template(player):
        return dict(
                num_of_treatments = C.NUM_Treatment_Conditions,
                num_of_repeats = C.NUM_Repeated_Rounds_Treatment_Condition,
                total_rounds = C.NUM_ROUNDS
                )
    @staticmethod
    def is_displayed(player: Player): 
        return player.round_number <= C.NUM_LeaderPage

    def before_next_page(player : Player, timeout_happened):
        player.treatment_sequence = "-".join([str(T) for T in player.participant.treatment_sequence])


class ExpConditionIntro(Page):
    def vars_for_template(player):

        # Decide current treatment by treatment_sequence and round_number
        # This could have been a player method
        if player.round_number == C.ROUNDS_for_TreatmentIntro[0]:
            treatment_for_round = player.participant.treatment_sequence[0]
        elif player.round_number == C.ROUNDS_for_TreatmentIntro[1]:
            treatment_for_round = player.participant.treatment_sequence[1]
        elif player.round_number == C.ROUNDS_for_TreatmentIntro[2]:
            treatment_for_round = player.participant.treatment_sequence[2]

        return dict(
                treatment_for_round = treatment_for_round,
                sequence = player.participant.treatment_sequence # for diagnostics only. Remove for production.
                )

    pass
    @staticmethod
    def is_displayed(player: Player): 
        if player.round_number in C.ROUNDS_for_TreatmentIntro:
            return True

class WorkerPage(Page):

    def vars_for_template(player):

        # Decide current treatment by treatment_sequence and round_number
        # This could have been a player method
        if player.round_number in C.ROUNDS_for_T1:
            rounds_under_same_treatment = C.ROUNDS_for_T1
            treatment_for_round = player.participant.treatment_sequence[0]
        elif player.round_number in C.ROUNDS_for_T2:
            rounds_under_same_treatment = C.ROUNDS_for_T2
            treatment_for_round = player.participant.treatment_sequence[1]
            print("Found you")
        elif player.round_number in C.ROUNDS_for_T3:
            rounds_under_same_treatment = C.ROUNDS_for_T3
            treatment_for_round = player.participant.treatment_sequence[2]
        else:
            print(player.round_number)
            print(C.ROUNDS_for_T2)

        # Then, report the current page number, as a progress indicator
        round_count_out_of_Total = rounds_under_same_treatment.index(player.round_number) + 1


        return dict(
                treatment_for_round = treatment_for_round,
                round_count_out_of_Total = round_count_out_of_Total
                )


    @staticmethod
    def is_displayed(player: Player): 
        if player.round_number in C.ROUNDS_for_T1:
            return True
        elif player.round_number in C.ROUNDS_for_T2:
            return True
        elif player.round_number in C.ROUNDS_for_T3:
            return True






class Results(Page):

    @staticmethod
    def is_displayed(player: Player): 
        if player.round_number == C.ROUND_for_FinishPage:
            return True




page_sequence = [WelcomePage, ExpConditionIntro, WorkerPage, Results]
