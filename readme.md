==> [Demo](https://modified-otree-snippets.herokuapp.com/demo) <== 


# Intro
This repo contains modified apps from the [`otree-snippets`
project](https://www.otreehub.com/projects/otree-snippets/) on oTree Hub.

The list of modified apps includes:
* `detect_window`, for detecting user-agent and window dimension of the client's
  browser.
* `what_if_calculator`, for calculating profits with given user input. Attempts
  are logged with `epoch` timestamps.
* `balanced_treatment_within_subject`, for executing treatments in a "random
  order" (first, permutate the possible sequence of treatments, and then, assign
  the sequence by arrival order.)
  
  
-----

For detailed notes on the modified apps, please read along

----

## Detect user-agent and window dimension
The
[`detect_window/`](https://github.com/UMBEE/modified-otree-snippets/tree/master/detect_window)
folder contains an application adopted from [the
`otree-snippets` project on
oTreeHub](https://www.otreehub.com/projects/otree-snippets/). Specifically, the
original application is named as `detect_mobile/` in the original
`otree-snippets` project.

### What's new
The following model fields are added for export:
1. `user_agent_str` - the full `User-Agent` string of the client browser, in raw
   format.
2. `window_width` - the width (in pixels) of the client browser, 
4. `window_height` - the height (in pixels) of the client browser, 
3. `is_mobile` - a binary variable indicating whether the `User-Agent` contains
   any of "Android", "iPad" or "iPhone" - if so, the device is a mobile device.

### Warning
This snippet is constructed as a proof-of-concept. Pull requests are welcomed to
make it ready for production.


## What-if calculator
The
[`what_if_calculator/`](https://github.com/UMBEE/modified-otree-snippets/tree/master/what_if_calculator)
folder contains an application adopted from [the
`otree-snippets` project on
oTreeHub](https://www.otreehub.com/projects/otree-snippets/). Specifically, the
original application is named as `input_calculation/` in the original
`otree-snippets` project. Another important reference is the `stroop/` app from
[the `otree-more-demos` project on
oTreeHub](https://www.otreehub.com/projects/otree-more-demos/).

The naming convension is adopted from zTree, where a fully-fledged "What if"
calculator has been known for decades.

### What's new?
The main improvement is to keep track of all attempts in an easy-to-export
format.
* Using the syntax from the `stroop/` app from [the `otree-more-demos` project
  on oTreeHub](https://www.otreehub.com/projects/otree-more-demos/), the
  computation for profit is done in Python on the server.
* Using the syntax from the original `input_calculation/` app, we replaced the
  `amount` and `NumYears` variables to be `price` and `quantity`.


## Balanced ordering of treatments
In an within-subject design, let there be three treatment conditions. With
fixed multiples of subjects, scheduling the ordering of treatment conditions by
in a "Latin Square" approach may sound intuitive. Assume that subjects come in
groups of three, then, they could have been assigned according to the following
naturally generated Latin Square:
```
1 2 3
2 3 1
3 1 2
```
That is, the three subjects may be exposed to the three treamtents, in three
possbile orders: `1-2-3`, `2-3-1`, and `3-1-2`. Now, how about `2-1-3`? Or, say,
`3-2-1`?


Due to the construction of "Latin Squares", they are not unique when there are
more than one treatment condition. Technically, to rule out ordering effect of
treatments, what we are actually looking for is to randomize subjects into the
permutation of treatment `[1,2,3]` with equal probability.


In this demo, there are three treatments and the ordering of the treatments will
be randomized. Code references include:
* The `random_task_order/` app from [the `otree-snippets` project on
  oTreeHub](https://www.otreehub.com/projects/otree-snippets/)), which helps to
  explain how pages are ordered, and
* The `factorial_treatments/` app from `otree-snippets`, which introduced the
  use of `itertools` to generate and interate through the full set of
  treatments.
