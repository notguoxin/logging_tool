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
        loglevels: list = None,
    ):
        colorama.just_fix_windows_console()  # Initialize colorama once
        self.log_to_file = log_to_file
        self.logpath = logpath
        self.log_DEBUG_tofile = log_DEBUG_tofile
        self.loglevels = loglevels

    def _has_multiple_lines(self, s: str) -> bool:
        try:
            return s.count("\n") > 0
        except Exception:
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

    def _getlog_string(self, input: str, prefix: str, level: str) -> str:
        if self.loglevels and level:
            if level in self.loglevels:
                log_str = (
                    f"{datetime.datetime.now().isoformat()} {prefix} [{level}]: {input}"
                )
            else:
                raise ValueError
        else:
            log_str = f"{datetime.datetime.now().isoformat()} {prefix}: {input}"
        return log_str

    def _log(self, input: str, prefix: str, level: str, color: str) -> None:
        """Handles the logging functionality."""
        if self._has_multiple_lines(input):
            self._log_multiline(input, prefix, level, color)

        else:
            log_str = self._getlog_string(input, prefix, level)

            print(termcolor.colored(log_str, color))
            if self.log_to_file and self.logpath:
                self._write_to_file(log_str, prefix)

    def _log_multiline(self, input: str, prefix: str, level: str, color: str) -> None:
        def handler(splited_input):
            return self._getlog_string(input, prefix, level)

        for line in input.splitlines():
            print(termcolor.colored(handler(line), color))
            if self.log_to_file and self.logpath:
                self._write_to_file(handler(line), prefix)

    def debug(self, input: str, level: str = "") -> None:
        self._log(input, "DEBUG", level, "light_blue")

    def log(self, input: str, level: str = "") -> None:
        self._log(input, " INFO", level, "green")

    def warn(self, input: str, level: str = "") -> None:
        self._log(input, " WARN", level, "yellow")

    def error(self, input: str, level: str = "") -> None:
        self._log(input, "ERROR", level, "red")
