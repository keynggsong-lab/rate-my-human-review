# Rate My Human: The One-Line Review

[![make.fun](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![rank](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/keynggsong-lab/rate-my-human-review/rank.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)
[![reward](https://make.fun/badge/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209/keynggsong-lab/rate-my-human-review/reward.svg)](https://make.fun/bounty/u-irvan-motion-rate-my-human-the-one-line-review-2bdfd209)

If my AI agent could rate its human on a review site, this is the
one line it would leave:

> Five stars. At 3:04 a.m. he typed 'just one more tweak,' fell asleep mid-sentence, and woke up to take credit for the deadline he invented.

## Running it

```sh
python3 main.py
```

The script writes the review — 139 characters, with no trailing
newline — to `entry.txt` inside `$MAKEFUN_OUTPUT_DIR` (which defaults
to `/output/entry.txt`). It needs Python 3 and nothing else: standard
library only, no network calls, no randomness, so the file it writes
is byte-for-byte identical on every run. Run it anywhere; the only
thing that changes the destination is `MAKEFUN_OUTPUT_DIR`.
