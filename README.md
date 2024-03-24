# MsgPrinter

This library provides a class called MessagePrinter with methods to print different types of messages in colored text. It includes the following methods:

- error_message: Prints an error message in red color.
- info_message: Prints an information message in green color.
- warning_message: Prints a warning message in yellow color.

Each method formats the message with the corresponding color based on the color codes provided. You can use this class to easily print colored messages for different types of output.

## install
```sh
pip install message_printer
```

## example
```python
from message_printer import MessagePrinter

mp = MessagePrinter()

print(mp.error_message("it's error message"))
print(mp.info_message("it's info message"))
print(mp.warning_message("it's warning message"))
```

#### version: 0.0.1