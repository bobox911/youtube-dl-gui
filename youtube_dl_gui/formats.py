from __future__ import annotations

from typing import Callable

import wx

_: Callable[[str], str] = wx.GetTranslation

OUTPUT_FORMATS: dict[str, str] = {
    "0": _("ID"),
    "1": _("Title"),
    "2": _("Title + ID"),
    "4": _("Title + Quality"),
    "5": _("Title + ID + Quality"),
    "3": _("Custom"),
}

DEFAULT_FORMATS: dict[str, str] = {"0": _("default")}

VIDEO_FORMATS: dict[str, str] = {
    "3gp": "3gp",
    "17": "3gp [144p]",
    "36": "3gp [240p]",
    "flv": "flv",
    "5": "flv [240p]",
    "34": "flv [360p]",
    "35": "flv [480p]",
    "webm": "webm",
    "43": "webm [360p]",
    "44": "webm [480p]",
    "45": "webm [720p]",
    "46": "webm [1080p]",
    "mp4": "mp4",
    "18": "mp4 [360p]",
    "**": "mp4 [480p]",
    "22": "mp4 [720p]",
    "37": "mp4 [1080p]",
    "bestvideo[ext=mp4][vcodec=avc1.42001E]+bestaudio[ext=m4a]": "mp4 [360p] (Best)",
    "bestvideo[ext=mp4][vcodec=avc1.4D401E]+bestaudio[ext=m4a]": "mp4 [480p] (Best)",
    "bestvideo[ext=mp4][vcodec=avc1.4D401F]+bestaudio[ext=m4a]": "mp4 [720p] (Best)",
    "bestvideo[ext=mp4][vcodec=avc1.640028]+bestaudio[ext=m4a]": "mp4 [1080p] (Best)",
}

AUDIO_FORMATS: dict[str, str] = {
    "mp3": "mp3",
    "wav": "wav",
    "aac": "aac",
    "m4a": "m4a",
    "vorbis": "vorbis",
    "opus": "opus",
    "flac": "flac",
}

FORMATS: dict[str, str] = DEFAULT_FORMATS.copy()
FORMATS.update(VIDEO_FORMATS)
FORMATS.update(AUDIO_FORMATS)
