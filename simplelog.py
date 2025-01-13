import termcolor
import colorama
import datetime
import os


class Logger:
    def __init__(
        self,
        log_to_file: bool = False,
        log_DEBUG_tofile: bool = False,
        logpath: str = None,
    ):
        colorama.just_fix_windows_console()  # Initialize colorama once
        self.log_to_file = log_to_file
        self.logpath = logpath
        self.log_DEBUG_tofile = log_DEBUG_tofile

    def _has_multiple_lines(self, s: str) -> bool:
        try:
            return s.count("\n") > 0
        except AttributeError:
            return False

    def _write_to_file(self, log_str: str, log_type: str) -> None:
        """Writes a log message to the file if logging is enabled."""
        if log_type == "DEBUG" and not self.log_DEBUG_tofile:
            return

        if os.path.exists(self.logpath):
            with open(self.logpath, "a") as log_file:
                log_file.write(log_str + "\n")  # Add newline for each log entry
        else:
            with open(self.logpath, "w") as log_file:
                log_file.write(log_str + "\n")  # Add newline for each log entry

    def _log(self, input: str, prefix: str, color: str) -> None:
        """Handles the logging functionality."""
        if self._has_multiple_lines(input):
            self._log_multiline(input, prefix, color)

        else:
            log_str = f"{datetime.datetime.now().isoformat()} {prefix}: {input}"
            print(termcolor.colored(log_str, color))
            if self.log_to_file and self.logpath:
                self._write_to_file(log_str, prefix)

    def _log_multiline(self, input: str, prefix: str, color: str) -> None:
        def handler(splited_input):
            return f"{datetime.datetime.now().isoformat()} {prefix}: {splited_input}"

        for line in input.splitlines():
            print(termcolor.colored(handler(line), color))
            if self.log_to_file and self.logpath:
                self._write_to_file(handler(line), prefix)

    def debug(self, input: str) -> None:
        self._log(input, "DEBUG", "light_blue")

    def log(self, input: str) -> None:
        self._log(input, " INFO", "green")

    def warn(self, input: str) -> None:
        self._log(input, " WARN", "yellow")

    def error(self, input: str) -> None:
        self._log(input, "ERROR", "red")
