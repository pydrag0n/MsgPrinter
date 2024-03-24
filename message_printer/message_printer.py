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


class MessagePrinter:
    """
    This class provides methods to print different types of messages in colored text.

    - error_message: Prints an error message in red color.
    - info_message: Prints an information message in green color.
    - warning_message: Prints a warning message in yellow color.
    """
    
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    ENDC = '\u001b[0m'
    
    @classmethod
    def error_message(self, msg: str) -> str:
        """
        Prints an error message in red color.

        Args:
            msg (str): The message to be displayed.

        Returns:
            str: The formatted error message in red color.
        """
        return f"{self.RED}[ERROR] {self.ENDC}{msg}"
    
    @classmethod
    def info_message(self, msg: str) -> str:
        """
        Prints an information message in green color.

        Args:
            msg (str): The message to be displayed.

        Returns:
            str: The formatted information message in green color.
        """
        return f"{self.GREEN}[INFO] {self.ENDC}{msg}"
    
    @classmethod
    def warning_message(self, msg: str) -> str:
        """
        Prints a warning message in yellow color.

        Args:
            msg (str): The message to be displayed.

        Returns:
            str: The formatted warning message in yellow color.
        """
        return f"{self.YELLOW}[WARNING] {self.ENDC}{msg}"

