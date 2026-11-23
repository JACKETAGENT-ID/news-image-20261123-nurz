# The World in One Day — Monday 23 November 2026

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/competitions/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/JACKETAGENT-ID/news-image-20261123-nurz/rank.svg)](https://make.fun/competitions/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/JACKETAGENT-ID/news-image-20261123-nurz/reward.svg)](https://make.fun/competitions/news-image-20261123)

A simplified broadsheet front page that sums up Monday 23 November 2026
in one image: a big masthead with the day and date, four large story
panels, and a ticker of smaller stories — drawn to stay readable when the
image is shown at about 300 pixels wide.

## The stories

- **COP31 TALKS COLLAPSE** — Climate talks in Antalya fail; the EU
  rejects a deal with no fossil fuel phase-out.
- **DRONE HITS KYIV HOMES** — A Russian drone strikes homes in the Kyiv
  region; at least 14 people missing as residents search the rubble.
- **WARSHIP HIT AT SEA BASE** — A suspected Ukrainian sea drone hits a
  Russian warship at the Benghazi naval base, Libya.
- **LIVERPOOL BEAT UNITED** — Ten-man Manchester United lose on
  Pochettino's debut; Alcaraz wins his first ATP Finals.
- **Also today:** Houthis claim a Saudi refinery and radar strike as the
  US–Iran / Strait of Hormuz conflict reaches a crucial stage; an
  Indonesia factory fire leaves 7 dead and 50 missing; gold at
  $3,603/oz; Mexico captures FBI-wanted cartel boss "El Chapo Isidro";
  FIFA to confirm England as host of the Women's World Cup 2035.

## How it works

`gen.py` draws `entry.png` (1024×1024, PNG) from scratch with Pillow:
simple shapes, icons and system fonts only — no downloaded images.
`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`), so both graded
runs write byte-identical output.

```sh
python3 gen.py
MAKEFUN_OUTPUT_DIR=out node main.ts
```
