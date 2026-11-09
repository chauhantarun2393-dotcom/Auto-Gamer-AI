"""Entry point for the Auto-Gamer-AI automation project."""

from __future__ import annotations

import argparse

from src.auto_gamer_ai.bot import BotConfig, GameBot


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Auto-Gamer-AI automation bot.")
    parser.add_argument("--window-title", default="Game", help="Target game window title.")
    parser.add_argument("--interval", type=float, default=0.5, help="Polling interval in seconds.")
    parser.add_argument("--threshold", type=float, default=0.85, help="Detection confidence threshold.")
    args = parser.parse_args()

    config = BotConfig(
        interval=args.interval,
        threshold=args.threshold,
        target_window_title=args.window_title,
    )

    bot = GameBot(config=config)
    bot.run()


if __name__ == "__main__":
    main()
