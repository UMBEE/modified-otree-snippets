# Experiment Design
Let there be three treatment conditions for the experiment. In this demo, we opt
to use a within-subject design where subjects will play 10 rounds under each
treatment condition. Across the 10 rounds that repeats, they are subject to
change

By permuting the order of treatments, each subject will be assigned into one of
six ordering of treatment conditions with equal probability. The full set of
ordering include: 
    1-2-3,
    1-3-2,
    2-1-3,
    2-3-1,
    3-1-2,
    3-2-1.
The ordering of the treatment conditions is randomized for each subject, based
on arrival order.

Assuming the subject is assigned to treatment ordering 1-2-3, then, the subject
will be prompted with the following sequence of pages:
* Welcome page
* Intro page for Treatment 1
    * Page for Round 1
    * Page for Round 2
    * Page for Round 3
    * Page for Round 4
    * Page for Round 5
    * Page for Round 6
    * Page for Round 7
    * Page for Round 8
    * Page for Round 9
    * Page for Round 10
* Intro page for Treatment 2
    * Page for Round 1
    * Page for Round 2
    * Page for Round 3
    * Page for Round 4
    * Page for Round 5
    * Page for Round 6
    * Page for Round 7
    * Page for Round 8
    * Page for Round 9
    * Page for Round 10
* Intro page for Treatment 3
    * Page for Round 1
    * Page for Round 2
    * Page for Round 3
    * Page for Round 4
    * Page for Round 5
    * Page for Round 6
    * Page for Round 7
    * Page for Round 8
    * Page for Round 9
    * Page for Round 10
* Result Page

Technically, there will be a total of 3 x 10 rounds, with each page displayed
conditionally on the round number and the randomly selected ordering of the
treatments. In this demo, we prepend the sequence of experimental rounds with
one welcome page, and append towards the end of the sequence a result page that
reviews the full sequencing of all apps.


# Code References

