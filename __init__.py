# This Anki add-on makes the fuzzed ranges increase monotonically
#
# The original implementation has ranges that go up and down as the
# interval increases. This implementation is simpler and ensures monotonic
# increase of range as interval increases.
#

from aqt import mw
from anki.schedv2 import Scheduler as SchedulerV2
from anki.cards import Card

config = mw.addonManager.getConfig(__name__)

def updateConfig(newConfig):
    global config
    config = newConfig

mw.addonManager.setConfigUpdateAction(__name__, updateConfig)

def myRescheduleRev(self, card: Card, ease: int, early: bool) -> None:
    # update interval
    card.lastIvl = card.ivl
    if early:
        self._updateEarlyRevIvl(card, ease)
    else:
        self._updateRevIvl(card, ease)

    # then the rest
    # card.factor = max(1300, card.factor + [-150, 0, 150][ease - 2])
    card.factor = max(1300, card.factor +
        [
            config.get('easeAdjustmentHard', -150),
            config.get('easeAdjustmentGood', 50),
            config.get('easeAdjustmentEasy', 150)
        ][ease - 2])
    card.due = self.today + card.ivl

    # card leaves filtered deck
    self._removeFromFiltered(card)

SchedulerV2._rescheduleRev = myRescheduleRev
