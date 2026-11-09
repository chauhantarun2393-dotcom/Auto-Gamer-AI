# Auto-Gamer-AI

A small Python starter bot that looks for a supplied image on screen and presses Space when it finds a match.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run

Save a small screenshot of the on-screen target as an image, then run:

```bash
python app.py --template path/to/target.png
```

Optional settings:

```bash
python app.py --template path/to/target.png --interval 0.5 --threshold 0.85
```

The confidence threshold must be between 0 and 1, and the interval must be greater than zero. The bot captures the full desktop, not just a selected game window, and sends Space to the currently focused application when the template is detected. Keep the intended game visible and focused. Press Ctrl+C to stop; PyAutoGUI's corner fail-safe is enabled by default.

This is a basic template-matching scaffold, not a game-specific AI. It will not act without a valid target image. Template matching can require an exact enough scale and appearance; tune the threshold and template for your game.
