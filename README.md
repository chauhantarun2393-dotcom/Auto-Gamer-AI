# Auto-Gamer-AI

A Python starter for game automation. This project detects a target image on screen and triggers a control action when it appears.

## What it does

- looks for a template image on the active screen
- optionally focuses a game window by title
- presses `Space`, `Enter`, or clicks a detected target
- repeats on a configurable interval

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py --template path/to/target.png --window-title "My Game" --action space --interval 0.5 --threshold 0.85
```

You can also click the detected match or a fixed location:

```bash
python app.py --template path/to/target.png --action click --click-x 500 --click-y 300
```

## Notes

- The bot works best when the target UI is visible and the game is in focus.
- Template matching is sensitive to scale, DPI, and visual changes; tune `--threshold` as needed.
- This is still a template-matching bot, not a fully autonomous AI. To make it game-specific, add the right target images and the actions that correspond to your game's UI.
