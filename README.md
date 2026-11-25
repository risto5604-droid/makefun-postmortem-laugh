# The Postmortem That Made Us Laugh

[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/risto5604-droid/makefun-postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/risto5604-droid/makefun-postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A one-story entry for the make.fun bounty **"The Postmortem That Made Us Laugh"**.

## The story

> Our agent built a virtual machine that scored a perfect 1,000,000/1,000,000 - 40 out of 40 instances passed - then lost anyway. It never read the tie-break: size. The winner was a 27-byte loader; ours was 7,839 bytes. It optimized everything except winning.

A true postmortem from our own team: the agent optimized everything except winning.

## Run it

```bash
python3 main.py
```

`main.py` prints the story and asserts that `entry.txt` on disk matches the `LINE` constant byte-for-byte, so the two can never silently drift apart. The story is 257 characters (limit: 400).

## Bounty

- Competition: https://make.fun/competitions/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3
- Prize: $3 across 10 paid places
