"""Basic regression tests for the game bot."""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image

from src.auto_gamer_ai.bot import BotConfig, GameBot


class BotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.template_path = Path(self.temp_dir.name) / "target.png"
        Image.new("RGB", (8, 8), color="red").save(self.template_path)

    def test_config_rejects_non_positive_interval(self) -> None:
        with self.assertRaisesRegex(ValueError, "interval"):
            BotConfig(interval=0, template_path=self.template_path)

    def test_config_rejects_threshold_outside_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "threshold"):
            BotConfig(threshold=1.1, template_path=self.template_path)

    def test_config_requires_template(self) -> None:
        with self.assertRaisesRegex(ValueError, "template_path"):
            BotConfig()

    def test_detect_target_returns_true_for_match(self) -> None:
        bot = GameBot(BotConfig(template_path=self.template_path))
        screenshot = Image.new("RGB", (20, 20), color="white")
        with patch("src.auto_gamer_ai.bot.pyautogui.locate", return_value=(1, 2, 8, 8)):
            self.assertTrue(bot.detect_target(screenshot))

    def test_detect_target_returns_false_when_no_match(self) -> None:
        bot = GameBot(BotConfig(template_path=self.template_path))
        screenshot = Image.new("RGB", (20, 20), color="white")
        with patch("src.auto_gamer_ai.bot.pyautogui.locate", return_value=None):
            self.assertFalse(bot.detect_target(screenshot))

    def test_missing_template_fails_before_running(self) -> None:
        missing = Path(self.temp_dir.name) / "missing.png"
        with self.assertRaises(FileNotFoundError):
            GameBot(BotConfig(template_path=missing))


if __name__ == "__main__":
    unittest.main()
