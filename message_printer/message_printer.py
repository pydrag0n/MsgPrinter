"""
Color	    Code
Black	    \u001b[30m
Red	        \u001b[31m
Green	    \u001b[32m
Yellow	    \u001b[33m
Blue	    \u001b[34m
Purple	    \u001b[35m
Cyan	    \u001b[36m
White	    \u001b[37m
Reset color	\u001b[0m"""

from datetime import datetime
import time

class Font:
    
    class Color:
        RED = '\u001b[31m'
        GREEN = '\u001b[32m'
        YELLOW = '\u001b[33m'
        BLUE = '\u001b[34m'
        ENDC = '\u001b[0m'

    class Style:
        BOLD = '\033[1m'
        ENDS = '\033[0m'
        
        @staticmethod
        def bold(text: str)-> str:
            return f"{Font.Style.BOLD}{text}{Font.Style.ENDS}"

class MessagePrinter:
    """
    This class provides methods to print different types of messages in colored text.

    - error_message: Prints an error message in red color.
    - info_message: Prints an information message in green color.
    - warning_message: Prints a warning message in yellow color.
    """
    
    @staticmethod
    def error_message(msg: str, bold: bool=False) -> str:
        if bold is True:
            print(Font.Style.bold(f"{Font.Style.BOLD}{Font.Color.RED}[ERROR {datetime.now()}] {Font.Color.ENDC}{msg}{Font.Style.ENDS}"))
            return
        print(f"{Font.Color.RED}[ERROR {datetime.now()}] {Font.Color.ENDC}{msg}")
    
    @staticmethod
    def info_message(msg: str, bold: bool=False) -> str:
        if bold is True:
            print(Font.Style.bold(f"{Font.Color.GREEN}[INFO {datetime.now()}] {Font.Color.ENDC}{msg}"))
            return 
        
        print(f"{Font.Color.GREEN}[INFO {datetime.now()}] {Font.Color.ENDC}{msg}")
    
    @staticmethod       
    def warning_message(msg: str, bold: bool=False) -> str:
        if bold is True:
            return Font.Style.bold(f"{Font.Color.YELLOW}[WARNING {datetime.now()}] {Font.Color.ENDC}{msg}")
        print(f"{Font.Color.YELLOW}[WARNING {datetime.now()}] {Font.Color.ENDC}{msg}")
    
    @staticmethod
    def timer(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f'{Font.Style.BOLD}{Font.Color.BLUE}{func.__name__} function execution took {end_time - start_time:.2f} seconds ~{Font.Style.ENDS} ')
            return result
        return wrapper
