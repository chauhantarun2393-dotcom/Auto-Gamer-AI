"""Entry point for the Auto-Gamer-AI automation project."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.auto_gamer_ai.bot import BotConfig, GameBot


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Auto-Gamer-AI automation bot.")
    parser.add_argument(
        "--template",
        required=True,
        type=Path,
        help="Image template of the target object to look for on screen.",
    )
    parser.add_argument(
        "--window-title",
        default="",
        help="Optional title of the game window to activate before automating.",
    )
    parser.add_argument("--interval", type=float, default=0.5, help="Polling interval in seconds.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Template matching confidence between 0 and 1 (default: 0.85).",
    )
    parser.add_argument(
        "--action",
        default="space",
        choices=["space", "enter", "click", "left_click"],
        help="Action to trigger when the object is found.",
    )
    parser.add_argument("--click-x", type=int, default=None, help="Optional X coordinate to click when action is click.")
    parser.add_argument("--click-y", type=int, default=None, help="Optional Y coordinate to click when action is click.")
    args = parser.parse_args()

    config = BotConfig(
        interval=args.interval,
        threshold=args.threshold,
        template_path=args.template,
        target_window_title=args.window_title,
        action=args.action,
        click_x=args.click_x,
        click_y=args.click_y,
    )

    bot = GameBot(config)
    bot.run()


if __name__ == "__main__":
    main()
