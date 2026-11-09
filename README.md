# Auto-Gamer-AI

A Python starter for screen-template-based automation. The bot code is generic and is **not designed or appropriate for automating competitive online gameplay**.

## Free Fire controls

For manual emulator key mapping, sensitivity tuning, and accessibility tips, see [the Free Fire emulator controls guide](docs/free-fire-emulator-controls.md). Use the emulator's built-in control editor and test changes in practice mode; the guide does not automate game input.

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
