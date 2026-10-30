# clock

A tiny, dependency-free CLI clock written in Python. It started as a
status-bar clock for **i3blocks**, but it works anywhere you just need the
current time on one line.

```console
$ clock
09:05:03

$ clock --format "%H:%M"
09:05

$ clock -f "%a %d %b" --utc
Thu 30 Oct
```

## Features

- One line of output, so it drops straight into i3blocks, polybar, tmux, etc.
- Any `strftime` format via `--format/-f`, local time or UTC (`--utc/-u`)
- Zero-padded output and a single clock read per run
- Standard library only — no install dependencies

## Install

```console
git clone https://github.com/MrNotInk/clock.git
cd clock
chmod +x bin/main.py          # optional
ln -s "$PWD/bin/main.py" ~/.local/bin/clock
```

Or, if you use the [weld](https://github.com/MrNotInk/weld) package manager:

```console
weld --run clock
```

## Usage

```console
python3 bin/main.py [--format FMT] [--utc]
```

| Option | Description | Default |
| --- | --- | --- |
| `-f`, `--format FMT` | `strftime` format string | `%H:%M:%S` |
| `-u`, `--utc` | use UTC instead of local time | off |
| `-h`, `--help` | show help and exit | — |

### i3blocks

Add a block to `~/.config/i3blocks/config`:

```ini
[clock]
command=$HOME/clock/bin/main.py --format "%H:%M"
interval=10
```

Set `interval=1` for a seconds-precision display.

## Library use

The helpers in `bin/lib/_clock.py` can be imported directly. They take an
optional `datetime`, which makes them easy to test:

```python
from bin.lib import _clock

_clock.hour()                                  # current hour, e.g. 9
_clock.timestamp("%H:%M:%S")                   # "09:05:03"
_clock.timestamp("%H:%M", datetime.datetime(2026, 1, 2, 3, 4, 5))  # "03:04"
```

`sec()`, `minute()` and `hour()` are also available; `mint()` remains as a
deprecated alias for `minute()`.

## Tests

From the repository root:

```console
python3 -m unittest discover -s tests -t . -v
```

## Project layout

```
bin/main.py         CLI entry point
bin/lib/_clock.py   time helpers
config.json         weld package manifest
plugins/            weld plugin hooks
tests/              unit tests
```

## License

No license file yet — until one is added, all rights are reserved. Adding a
`LICENSE` (MIT or GPL-3.0, for example) is recommended before publishing.
