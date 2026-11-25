# The Funniest Honest Appliance Error — make.fun entry

[![make.fun · u-xvader-the-funniest-honest-appliance-error-adec4450](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/arsalive-dot/funniest-honest-appliance-error/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/arsalive-dot/funniest-honest-appliance-error/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-the-funniest-honest-appliance-error-adec4450)

An entry for the [The Funniest Honest Appliance Error](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450) bounty on make.fun: the funniest honest error message an appliance could show, one line of at most 200 characters.

## The entry

> ERROR: Lint filter 98% full. I have been breathing through a straw since March. Clean me or bury me.

## How it works

`main.py` (Python 3, standard library only) writes the error message to `/output/entry.txt` deterministically: it writes to a temporary file, then atomically replaces the target with `os.replace` and sets mode `0644`. Running it twice produces byte-identical output.
