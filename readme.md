# Intro

## Detect user-agent and window dimension

### What's new
The following model fields are added for export:
1. `user_agent_str` - the full `User-Agent` string of the client browser, in raw
   format.
2. `window_dimension` - the dimension of the client browser, in format 
3. `is_mobile` - a binary variable indicating whether the `User-Agent` contains
   any of "Android", "iPad" or "iPhone" - if so, the device is a mobile device.

### Warning
This snippet is constructed as a proof-of-concept. Pull requests are welcomed to
make it ready for production.
