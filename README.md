# Auto-Gamer-AI

A Python starter for screen-template-based automation. It is not designed or appropriate for automating competitive online gameplay.

## Free Fire on mobile

For touchscreen HUD placement, sensitivity tuning, and mobile play tips, see the [Free Fire mobile controls guide](docs/free-fire-mobile-controls.md). The guide uses the game's own settings and does not automate gameplay.

## Bot setup (offline/single-player projects only)

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Run the template-matching starter only in an offline or single-player project where automation is permitted:

```bash
python app.py --template path/to/target.png --action space
```

The bot captures the desktop and sends input to the currently focused application when a template is detected. Press Ctrl+C to stop. Template matching is sensitive to scale, DPI, and visual changes. Do not use this tool to automate competitive online matches.
