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
        help="Path to an image of the on-screen target that triggers an action.",
    )
    parser.add_argument("--interval", type=float, default=0.5, help="Polling interval in seconds.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Template matching confidence between 0 and 1 (default: 0.85).",
    )
    args = parser.parse_args()

    bot = GameBot(
        BotConfig(
            interval=args.interval,
            threshold=args.threshold,
            template_path=args.template,
        )
    )
    bot.run()


if __name__ == "__main__":
    main()
