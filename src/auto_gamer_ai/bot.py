"""Template-based game automation scaffold for Auto-Gamer-AI."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import time
from typing import Optional

import pyautogui
from PIL import Image, ImageGrab, UnidentifiedImageError


@dataclass
class BotConfig:
    interval: float = 0.5
    threshold: float = 0.85
    template_path: Path | str = ""
    target_window_title: str = ""
    action: str = "space"
    click_x: Optional[int] = None
    click_y: Optional[int] = None

    def __post_init__(self) -> None:
        if self.interval <= 0:
            raise ValueError("interval must be greater than zero")
        if not 0 <= self.threshold <= 1:
            raise ValueError("threshold must be between 0 and 1")
        if not self.template_path:
            raise ValueError("template_path is required; refusing to run without a target")
        if self.action not in {"space", "enter", "click", "left_click"}:
            raise ValueError("action must be one of: space, enter, click, left_click")
        if self.action in {"click", "left_click"} and (self.click_x is None or self.click_y is None):
            # Allow click at the detected target center if coordinates are omitted.
            pass


class GameBot:
    """Look for a target image on the screen and automate a game action."""

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

    def focus_window(self) -> None:
        """Activate the configured game window when a title is provided."""
        if not self.config.target_window_title:
            return
        try:
            import pygetwindow as gw

            windows = gw.getWindowsWithTitle(self.config.target_window_title)
            if windows:
                windows[0].activate()
                time.sleep(0.25)
        except Exception:
            # A game may not expose a title or the dependency may be absent.
            pass

    def capture_screen(self) -> Image.Image:
        """Capture the current screen for matching."""
        return pyautogui.screenshot().convert("RGB")

    def detect_target(self, screenshot: Image.Image):
        """Return the matching target box or None when the target is absent."""
        try:
            return pyautogui.locate(
                self._template,
                screenshot,
                confidence=self.config.threshold,
            )
        except pyautogui.ImageNotFoundException:
            return None

    def perform_action(self, target_box=None) -> None:
        """Perform the configured action when a target is detected."""
        if self.config.action == "space":
            pyautogui.press("space")
            return

        if self.config.action == "enter":
            pyautogui.press("enter")
            return

        if target_box is not None:
            left, top, width, height = target_box
            center_x = left + (width // 2)
            center_y = top + (height // 2)
            if self.config.click_x is not None and self.config.click_y is not None:
                center_x = self.config.click_x
                center_y = self.config.click_y
            pyautogui.click(center_x, center_y)
            return

        if self.config.click_x is not None and self.config.click_y is not None:
            pyautogui.click(self.config.click_x, self.config.click_y)

    def run(self) -> None:
        """Main loop: focus window, find target, and trigger an action."""
        print(f"Starting Auto-Gamer-AI bot. Target template: {self.config.template_path}")
        if self.config.target_window_title:
            print(f"Target window: {self.config.target_window_title}")
        print("Press Ctrl+C to stop.")
        try:
            while True:
                if self.config.target_window_title:
                    self.focus_window()
                screenshot = self.capture_screen()
                target_box = self.detect_target(screenshot)
                if target_box is not None:
                    self.perform_action(target_box)
                time.sleep(self.config.interval)
        except KeyboardInterrupt:
            print("\nBot stopped by user.")


__all__ = ["BotConfig", "GameBot"]
