#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Contains test cases for the optionsmanager.py module."""


import sys
import unittest
from pathlib import Path
from unittest import mock

PATH = Path(__file__).parent
sys.path.insert(0, str(PATH.parent))

from youtube_dl_gui import optionsmanager


class TestOptionsManager(unittest.TestCase):
    def setUp(self) -> None:
        self.config_path: str = str(PATH.joinpath("fixtures"))

    def test_init(self):
        opt_mng = optionsmanager.OptionsManager(self.config_path)
        self.assertEqual(
            opt_mng.settings_file, str(Path(self.config_path) / Path("settings.json"))
        )

    @mock.patch("youtube_dl_gui.optionsmanager.OptionsManager")
    def test_save_to_file(self, mock_optionsmanager):
        opt_mng = mock_optionsmanager.return_value
        opt_mng.save_to_file()
        opt_mng.save_to_file.assert_called_once()