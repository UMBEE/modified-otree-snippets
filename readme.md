# Intro
This repo contains modified apps from the [`otree-snippets`
project](https://www.otreehub.com/projects/otree-snippets/) on oTree Hub.

The list of modified apps includes:
* `detect_window`, for detecting user-agent and window dimension of the client's
  browser.
  
  
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
`otree-snippets` project.

The naming convension is adopted from zTree, where a fully-fledged "What if"
calculator has been known for decades.

### What's new?
The main improvement is to keep track of all attempts in an easy-to-export
format.
