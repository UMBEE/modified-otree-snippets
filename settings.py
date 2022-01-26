from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.000, participation_fee=0.00, doc=""
)

SESSION_CONFIGS = [
    dict(
        name='detect_window',
        display_name='Detect and track window dimension for browser client',
        num_demo_participants=1,
        # Note, from otree-snippets, the source app is called: detect_mobile
        app_sequence=['detect_window'],
    ),
    dict(
        name='what_if_calc',
        display_name='Calculate payoff using JavaScript',
        num_demo_participants=1,
        # Note, from otree-snippets, the source app is called: detect_mobile
        app_sequence=['what_if_calculator'],
    ),
        ]
# SESSION_CONFIGS = [
#     dict(
#         name='are_you_sure',
#         display_name="""'Are you sure?' popup based on the user's input""",
#         num_demo_participants=1,
#         app_sequence=['are_you_sure'],
#     ),
#     dict(
#         name='audio_alert',
#         display_name="""Audio alert (speak some text to get the participant's attention, after a wait page)""",
#         num_demo_participants=2,
#         app_sequence=['audio_alert'],
#     ),
#     dict(
#         name='balance_treatments_for_dropouts',
#         display_name='Assign a player to the treatment with the fewest datapoints',
#         num_demo_participants=6,
#         app_sequence=['balance_treatments_for_dropouts'],
#     ),
#     dict(
#         name='groups_csv',
#         display_name='Assign players to groups defined in a CSV file',
#         num_demo_participants=6,
#         app_sequence=['groups_csv'],
#     ),
#     dict(
#         name='back_button',
#         display_name='Back button for multiple instructions pages',
#         num_demo_participants=1,
#         app_sequence=['back_button'],
#     ),
#     dict(
#         name='bmi_calculator',
#         display_name='Basic 1-player game (BMI calculator)',
#         num_demo_participants=1,
#         app_sequence=['bmi_calculator'],
#     ),
#     dict(
#         name='detect_mobile',
#         display_name='Block mobile browsers',
#         num_demo_participants=1,
#         app_sequence=['detect_mobile'],
#     ),
#     dict(
#         name='input_calculation',
#         display_name="Immediate calculation so the user can see the potential result of their decision",
#         num_demo_participants=1,
#         app_sequence=['input_calculation'],
#     ),
#     dict(
#         name='chat_from_scratch',
#         display_name="Chat implementation from scratch (easier to customize)",
#         num_demo_participants=3,
#         app_sequence=['chat_from_scratch'],
#     ),
#     dict(
#         name='chat_with_experimenter',
#         display_name="Chat with experimenter",
#         num_demo_participants=1,
#         app_sequence=['chat_with_experimenter'],
#     ),
#     dict(
#         name='complex_form_layout',
#         display_name="Complex form layout",
#         num_demo_participants=1,
#         app_sequence=['complex_form_layout'],
#     ),
#     dict(
#         name='comprehension_test',
#         display_name="Comprehension test (quiz you must pass to proceed)",
#         num_demo_participants=1,
#         app_sequence=['comprehension_test'],
#     ),
#     dict(
#         name='comprehension_test_simple',
#         display_name="Comprehension test (simple version)",
#         num_demo_participants=1,
#         app_sequence=['comprehension_test_simple'],
#     ),
#     dict(
#         name='constant_sum',
#         display_name="Constant-sum input (3 numbers that add up to 100)",
#         num_demo_participants=1,
#         app_sequence=['constant_sum'],
#     ),
#     dict(
#         name='configurable_players_per_group',
#         display_name="Configurable players_per_group (doesn't work in demo mode)",
#         num_demo_participants=12,
#         app_sequence=['configurable_players_per_group'],
#         players_per_group=3,
#     ),
#     dict(
#         name='count_button_clicks',
#         display_name='Count button clicks',
#         num_demo_participants=1,
#         app_sequence=['count_button_clicks'],
#     ),
#     dict(
#         name='css',
#         num_demo_participants=1,
#         app_sequence=['css'],
#         display_name="CSS to style timer and chat box",
#     ),
#     dict(
#         name='custom_export_groups',
#         display_name="""custom_export: 1 row for each group""",
#         num_demo_participants=4,
#         app_sequence=['custom_export_groups'],
#     ),
#     dict(
#         name='dropout_detection',
#         display_name='Dropout detection for single-player game',
#         num_demo_participants=1,
#         app_sequence=['dropout_detection'],
#     ),
#     dict(
#         name='dropout_end_game',
#         display_name="Dropout detection for multiplayer game (end game if has dropout)",
#         num_demo_participants=2,
#         app_sequence=['dropout_end_game', 'placeholder'],
#     ),
#     dict(
#         name='experimenter_input',
#         app_sequence=['experimenter_input'],
#         display_name="Experimenter input during the experiment (e.g. entering a random drawing)",
#         num_demo_participants=2,
#     ),
#     dict(
#         name='factorial_treatments',
#         display_name="Factorial balanced treatment design",
#         num_demo_participants=16,
#         app_sequence=['factorial_treatments'],
#     ),
#     dict(
#         name='getattr_setattr',
#         display_name="""getattr() to access numbered fields like player.num1, player.num2, ..., player.num9""",
#         num_demo_participants=1,
#         app_sequence=['getattr_setattr'],
#     ),
#     dict(
#         name='gbat_fallback_smaller_group',
#         display_name="group_by_arrival_time: fall back to a smaller group if not enough people show up",
#         num_demo_participants=4,
#         app_sequence=[
#             'gbat_fallback_smaller_group_part0',
#             'gbat_fallback_smaller_group_part1',
#         ],
#     ),
#     dict(
#         name='gbat_fallback_solo_task',
#         display_name="group_by_arrival_time: skip the multiplayer task if no other players show up",
#         num_demo_participants=2,
#         app_sequence=[
#             'gbat_fallback_solo_task_part0',
#             'gbat_fallback_solo_task_part1',
#             'gbat_fallback_solo_task_part2',
#         ],
#     ),
#     dict(
#         name='gbat_treatments',
#         display_name="group_by_arrival_time and group-level treatments",
#         num_demo_participants=6,
#         app_sequence=['gbat_treatments'],
#     ),
#     dict(
#         name='gbat_treatments_complex',
#         display_name="group_by_arrival_time and group-level treatments (complex version)",
#         num_demo_participants=6,
#         app_sequence=['gbat_treatments_complex'],
#     ),
#     dict(
#         name='gbat_new_partners',
#         display_name="group by arrival time, but in each round assign to a new partner.",
#         num_demo_participants=16,
#         app_sequence=['gbat_new_partners'],
#     ),
#     dict(
#         name='gbat_keep_same_groups',
#         display_name="group_by_arrival_time: Preserve same groups as a previous app that used group_by_arrival_time.",
#         num_demo_participants=6,
#         app_sequence=[
#             'gbat_keep_same_groups_part0',
#             'gbat_keep_same_groups_part1',
#             'gbat_keep_same_groups_part2',
#         ],
#     ),
#     dict(
#         name='history_table',
#         display_name='History table',
#         num_demo_participants=1,
#         app_sequence=['history_table'],
#     ),
#     dict(
#         name='image_choices',
#         display_name="Images in radio button choices",
#         num_demo_participants=1,
#         app_sequence=['image_choices'],
#     ),
#     dict(
#         name='live_volunteer',
#         display_name="Live volunteer's dilemma (first player to click moves everyone forward).",
#         num_demo_participants=3,
#         app_sequence=['live_volunteer'],
#     ),
#     dict(
#         name='longitudinal',
#         display_name='Longitudinal study (2-part study taking place across days/weeks)',
#         num_demo_participants=1,
#         app_sequence=['longitudinal'],
#     ),
#     dict(
#         name='question_with_other_option',
#         display_name="Menu with an 'other' option that lets you type in a valueInput manually",
#         num_demo_participants=4,
#         app_sequence=['question_with_other_option'],
#     ),
#     dict(
#         name='min_time_on_page',
#         display_name='Minimum time on a page',
#         num_demo_participants=1,
#         app_sequence=['min_time_on_page'],
#     ),
#     dict(
#         name='multi_select',
#         display_name="Multi-select widget (a.k.a. multiple choice / multiple answer)",
#         num_demo_participants=1,
#         app_sequence=['multi_select'],
#     ),
#     dict(
#         name='multi_select_complex',
#         display_name="Multi-select widget (flexible version with custom labels & 'select at least N')",
#         num_demo_participants=1,
#         app_sequence=['multi_select_complex'],
#     ),
#     dict(
#         name='pass_data_between_apps',
#         display_name='Pass data between apps',
#         num_demo_participants=1,
#         app_sequence=['pass_data_between_apps_part1', 'pass_data_between_apps_part2'],
#     ),
#     dict(
#         name='pay_random_app',
#         display_name="Pay a randomly selected app",
#         num_demo_participants=2,
#         app_sequence=['pay_random_app1', 'pay_random_app2', 'pay_random_app3'],
#     ),
#     dict(
#         name='pay_random_round',
#         display_name="Pay a randomly selected round",
#         num_demo_participants=1,
#         app_sequence=['pay_random_round'],
#     ),
#     dict(
#         name='persist_raw',
#         display_name="Persist raw HTML form inputs on reload (sliders, checkboxes, etc).",
#         app_sequence=['persist_raw'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='practice_rounds',
#         display_name="Practice rounds",
#         app_sequence=['practice_rounds'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='progress_bar',
#         display_name="Progress bar",
#         num_demo_participants=1,
#         app_sequence=['progress_bar'],
#     ),
#     dict(
#         name='questions_from_csv_simple',
#         display_name='Quiz questions loaded from CSV spreadsheet (simple version)',
#         num_demo_participants=2,
#         app_sequence=['questions_from_csv_simple'],
#     ),
#     dict(
#         name='questions_from_csv',
#         display_name='Quiz questions loaded from CSV spreadsheet (complex version)',
#         num_demo_participants=2,
#         app_sequence=['questions_from_csv_complex'],
#     ),
#     dict(
#         name='quiz_with_explanation',
#         display_name="Quiz + post-quiz explanation. Re-display the previous page's form as read-only, with answers/explanation.",
#         num_demo_participants=1,
#         app_sequence=['quiz_with_explanation'],
#     ),
#     dict(
#         name='radio_switching_point',
#         display_name='Radio button table with single switching point (strategy method)',
#         num_demo_participants=1,
#         app_sequence=['radio_switching_point'],
#     ),
#     dict(
#         name='radio',
#         display_name="Radio buttons in various layouts, looping over radio choices",
#         app_sequence=['radio'],
#         num_demo_participants=1,
#     ),
#     dict(
#         name='random_num_rounds',
#         display_name="Random number of rounds",
#         num_demo_participants=2,
#         app_sequence=['random_num_rounds'],
#     ),
#     dict(
#         name='random_num_rounds_multiplayer',
#         display_name="Random number of rounds for multiplayer (random stopping rule)",
#         num_demo_participants=2,
#         app_sequence=[
#             'random_num_rounds_multiplayer',
#             'random_num_rounds_multiplayer_end',
#         ],
#     ),
#     dict(
#         name='random_question_order',
#         display_name='Randomize order of questions',
#         num_demo_participants=4,
#         app_sequence=['random_question_order'],
#     ),
#     dict(
#         name='random_task_order',
#         display_name='Randomize order of different tasks',
#         num_demo_participants=4,
#         app_sequence=['random_task_order'],
#     ),
#     dict(
#         name='rank_players',
#         display_name="Rank players",
#         num_demo_participants=4,
#         app_sequence=['rank_players'],
#     ),
#     dict(
#         name='rank_widget',
#         display_name="Rank/reorder form widget",
#         num_demo_participants=1,
#         app_sequence=['rank_widget'],
#     ),
#     dict(
#         name='rank_topN',
#         display_name="Ranking your top N choices from a list of options.",
#         num_demo_participants=1,
#         app_sequence=['rank_topN'],
#     ),
#     dict(
#         name='redirect_to_other_website',
#         display_name="Redirect the user to another website and pass their data",
#         num_demo_participants=1,
#         app_sequence=['redirect_to_other_website'],
#     ),
#     dict(
#         name='appcopy',
#         display_name='Sandwich design (App A -> App B -> App A)',
#         num_demo_participants=1,
#         app_sequence=['appcopy1', 'multi_select', 'appcopy2'],
#     ),
#     dict(
#         name='sequential',
#         display_name="""Sequential game""",
#         num_demo_participants=3,
#         app_sequence=['sequential'],
#     ),
#     dict(
#         name='sequential_symmetric',
#         display_name="""Sequential game (symmetric)""",
#         num_demo_participants=3,
#         app_sequence=['sequential_symmetric'],
#     ),
#     dict(
#         name='other_player_previous_rounds',
#         display_name="Showing other players' decisions from previous rounds",
#         num_demo_participants=8,
#         app_sequence=['other_player_previous_rounds'],
#     ),
#     dict(
#         name='slider_live_label',
#         display_name="Slider with live updating label",
#         num_demo_participants=1,
#         app_sequence=['slider_live_label'],
#     ),
#     dict(
#         name='slider_graphic',
#         display_name="Slider that changes an image (e.g. happy to sad scale)",
#         num_demo_participants=1,
#         app_sequence=['slider_graphic'],
#     ),
#     dict(
#         name='supergames',
#         display_name="Supergames consisting of multiple rounds each",
#         num_demo_participants=1,
#         app_sequence=['supergames'],
#     ),
#     dict(
#         name='wait_page_timeout',
#         display_name="Timeout on a WaitPage (exit the experiment)",
#         num_demo_participants=2,
#         app_sequence=['wait_page_timeout'],
#     ),
#     dict(
#         name='multi_page_timeout',
#         display_name="Timeout spanning multiple pages",
#         num_demo_participants=1,
#         app_sequence=['multi_page_timeout'],
#     ),
#     dict(
#         name='timer_custom',
#         display_name="Timer: replacing the default timer with your own",
#         num_demo_participants=1,
#         app_sequence=['timer_custom'],
#     ),
#     dict(
#         name='multi_language',
#         display_name="Translate an app to multiple languages (e.g. English and German)",
#         num_demo_participants=1,
#         app_sequence=['multi_language'],
#     ),
#     dict(
#         name='treatments_from_spreadsheet',
#         display_name="Treatments defined in a spreadsheet",
#         num_demo_participants=12,
#         app_sequence=['treatments_from_spreadsheet'],
#     ),
#     dict(
#         name='wait_for_specific_people',
#         display_name="Wait only for specific people",
#         num_demo_participants=8,
#         app_sequence=['wait_for_specific_people'],
#     ),
# ]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin passwordInput in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


DEMO_PAGE_TITLE = """
Recipes for common tasks in oTree
"""

DEMO_PAGE_INTRO_HTML = """
Recipes for common tasks in oTree
"""


# don't share this with anybody.
SECRET_KEY = 'fnv*lfr%ghepfge1rg1a56t0sj+9d*p&1+&g%q@j!ju@zu^v@6'

SESSION_FIELDS = [
    'completions_by_treatment',
    'past_groups',
    'matrices',
    'wait_for_ids',
    'arrived_ids',
]

PARTICIPANT_FIELDS = [
    'app_payoffs',
    'expiry',
    'finished_rounds',
    'language',
    'num_rounds',
    'partner_history',
    'past_group_id',
    'progress',
    'quiz_num_correct',
    'selected_round',
    'task_rounds',
    'time_pressure',
    'wait_page_arrival',
]
