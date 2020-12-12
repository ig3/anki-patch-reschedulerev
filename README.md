# anki-patch-reschedulerev
This add-on monkey patches the V2 scheduler routine _rescheduleRev.

This patch makes the ease factor adjustments for Hard, Good and
Easy configurable, with defaults of -150, 50 and +150 respectively.

The ease factor is the interval multiplier applied on Good, in
thousandths. A factor of 1500 is 1.5 increases the interval by 50%.
Thus the ease factor determines how quickly the interval grows when the
answer is Good. The minimum easiness/factor is 1300. There is no maximum.
In the card browser, this is displayed as 'ease' as a percentage. 1500
would be displayed as 150%.

The V2 scheduler decreases the ease factor by 200 on a lapse, decreases it
by 150 on Hard, doesn't change it on Good and increases it by 150 on Easy.

This is problematic because lapses and Hard both decrease the ease factor,
but Good doesn't change it. So, the factor tends to decrease to the minimum
and then stay there, unless one answers Easy. Thus, unless one often
answers Easy, the interval tends to increase only at the minimal rate: an
increase of 30% per review, if the card is always Good.

I think it is better to increase the ease factor on Good so that if a card
is always good, the interval will gradually increase faster and faster.
Eventually the card should become Hard, which will decrease the ease factor
a bit. Ideally, the card will alternate between Good and Hard - around the
limits of retention. Ideally, the interval will increase fast enough that
the card is never Easy and never so fast that it lapses - or only
occasionally. There are various reports that a lapse rate of about 10% 
might be optimum for learning. Hard is just a slightly less severe lapse.

I generally select Again if I fail to remember some fundamental of the
card, or remember it incorrectly. I select Hard if I remember some minor
detail of the card incorrectly or if it takes me a long time to remember or
I am uncertain about it. Good is for cards that I remember correctly,
reasonably quickly and with confidence. I rarely answer Easy - only if I
have very immediate recall, with no effort, including full details of the
card. 

See:
https://github.com/ijgnd/anki__scheduler_apply_different_ease_basic/blob/master/reviewer_apply_different_ease.py
for a similar add-on that uses wrap instead of a full monkey patch.
