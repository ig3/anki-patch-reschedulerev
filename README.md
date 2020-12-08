# anki-patch-reschedulerev
This add-on monkey patches the V2 scheduler routine _rescheduleRev.

The original doesn't adjust easiness/factor on Good.

This version increases easiness/factor by 50 on Good. It still decreases by
150 on Hard and incrases by 150 on Easy. So, always answering Good increases
easiness slowly, answering Easy increases it quickly (three times as fast)
and answering Hard decreases it. The expectation is that one will usually
answer Good, but may occasionally answer Hard or Easy. Eventually, all cards
should be at maximum easiness/factor (i.e., when well learned, one should
always be answering Good or Easy).
