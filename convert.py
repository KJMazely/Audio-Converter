"""Audio conversion helpers used by both the command line and GUI."""

from pathlib import Path
import shutil
import subprocess
import sys


def find_ffmpeg():
    """Return the FFmpeg bundled with the app, or the development copy on PATH."""
    bundled_directory = getattr(sys, "_MEIPASS", None)
    if bundled_directory:
        bundled_ffmpeg = Path(bundled_directory) / "ffmpeg.exe"
        if bundled_ffmpeg.is_file():
            return str(bundled_ffmpeg)
    return shutil.which("ffmpeg")


def audio_file(file_name, new_format, output_dir=None):
    """Convert *file_name* and return the path of the newly-created file.

    Requires FFmpeg to be installed and available on PATH.
    """
    source = Path(file_name).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"'{source}' was not found.")
    if source.suffix.lower() == ".dcr":
        raise ValueError(
            "DCR files must be exported through Liberty Player. Open the file in Liberty Player, "
            "press Ctrl+Shift+E, and export it as MP3 before converting it here."
        )

    target_format = new_format.lower().lstrip(".")
    supported_formats = {"flac", "mp2", "mp3", "m4a", "ogg", "wav"}
    if target_format not in supported_formats:
        raise ValueError(f"Unsupported format: {new_format}")

    destination = Path(output_dir).expanduser().resolve() if output_dir else source.parent
    if not destination.is_dir():
        raise NotADirectoryError(f"'{destination}' is not a folder.")

    output_path = destination / f"{source.stem}.{target_format}"
    if output_path == source:
        raise ValueError("Choose a different output format from the source file.")

    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        raise RuntimeError("FFmpeg was not found. Install FFmpeg and add it to your PATH.")

    result = subprocess.run(
        [ffmpeg, "-y", "-i", str(source), str(output_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        details = result.stderr.strip().splitlines()
        message = details[-1] if details else "FFmpeg could not convert this file."
        raise RuntimeError(message)
    return output_path
