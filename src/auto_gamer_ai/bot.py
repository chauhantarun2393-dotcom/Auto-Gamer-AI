"""Template-matching automation scaffold for Auto-Gamer-AI."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import time

import pyautogui
from PIL import Image, ImageGrab, UnidentifiedImageError


@dataclass
class BotConfig:
    interval: float = 0.5
    threshold: float = 0.85
    template_path: Path | str = ""

    def __post_init__(self) -> None:
        if self.interval <= 0:
            raise ValueError("interval must be greater than zero")
        if not 0 <= self.threshold <= 1:
            raise ValueError("threshold must be between 0 and 1")
        if not self.template_path:
            raise ValueError("template_path is required; refusing to run without a target")


class GameBot:
    """Find a target image on screen and press Space when it is visible.

    This starter bot captures the full desktop. It does not isolate a particular
    game window; ensure the intended game is visible before starting it.
    """

    def __init__(self, config: BotConfig) -> None:
        self.config = config
        template_path = Path(config.template_path).expanduser()
        if not template_path.is_file():
            raise FileNotFoundError(f"Target template image not found: {template_path}")
        try:
            with Image.open(template_path) as template:
                self._template = template.convert("RGB").copy()
        except (UnidentifiedImageError, OSError) as exc:
            raise ValueError(f"Could not read target template image: {template_path}") from exc

    def capture_screen(self) -> Image.Image:
        """Capture the current desktop as an RGB image."""
        return ImageGrab.grab().convert("RGB")

    def detect_target(self, screenshot: Image.Image) -> bool:
        """Return whether the configured template is visible in the screenshot."""
        try:
            location = pyautogui.locate(
                self._template,
                screenshot,
                confidence=self.config.threshold,
            )
        except pyautogui.ImageNotFoundException:
            return False
        return location is not None

    def perform_action(self) -> None:
        """Press Space once after a target has been detected."""
        pyautogui.press("space")

    def run(self) -> None:
        """Capture, detect, and act until interrupted."""
        print("Starting Auto-Gamer-AI. Target template:", self.config.template_path)
        print("Capturing the full desktop; press Ctrl+C to stop.")
        try:
            while True:
                screenshot = self.capture_screen()
                if self.detect_target(screenshot):
                    self.perform_action()
                time.sleep(self.config.interval)
        except KeyboardInterrupt:
            print("\nBot stopped by user.")


__all__ = ["BotConfig", "GameBot"]
