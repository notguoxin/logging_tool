import termcolor
import colorama
import datetime
import os

class Logger:
    def __init__(self, should_log: bool, logpath: str):
        colorama.just_fix_windows_console()  # Initialize colorama once
        self.should_log = should_log
        self.logpath = logpath

    def _write_to_file(self, log_str: str) -> None:
        """Writes a log message to the file if logging is enabled."""
        if self.should_log and self.logpath:
            if os.path.exists(self.logpath):
                with open(self.logpath, "a") as log_file:
                    log_file.write(log_str + "\n")  # Add newline for each log entry
            else:
                with open(self.logpath, "w") as log_file:
                    log_file.write(log_str + "\n")  # Add newline for each log entry
                
    def _log(self, string: str, text: str, color: str) -> None:
        """Handles the logging functionality."""
        log_str = f"{datetime.datetime.now().isoformat()} {text}: {string}"
        print(termcolor.colored(log_str, color))
        self._write_to_file(log_str)
        
    def debug(self,string:str) -> None:
        self._log(string,"DEBUG","light_blue")
        
    def log(self,string:str) -> None:
        colorama.just_fix_windows_console()
        self._log(string," INFO","green")
        
    def warn(self,string:str) -> None:
        colorama.just_fix_windows_console()
        self._log(string," WARN","yellow")
        
    def error(self,string:str) -> None:
        colorama.just_fix_windows_console()
        self._log(string,"ERROR","red")
