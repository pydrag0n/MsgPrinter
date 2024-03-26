```python
import message_printer
import time
mp = message_printer.MessagePrinter()

@mp.timer
def textwrite(text):
    time.sleep(2)
    return text

print(textwrite("hello world"))

print(mp.info_message("Информируюущее сообщение", bold=True)) 
print(mp.error_message("Сообщение об ошибке", bold=True))
print(mp.warning_message("Предупреждающее сообщение"))
```

![output](imgs\output.png)

### timer

*Время за которое выполниться функция, можно измерить с помощью декоратора `timer` (время выводиться в секундах)*

----

### messages

__info_message__ - *метод для вывода информационного сообщения (`[INFO] Bot started`)*

__error_message__ - *метод для вывода сообщения об ошибке (`[ERROR] TimeoutError: The operation timed out.`)*

__warning_message__ - *метод для вывода предупреждающего сообщения (`[WARNING] FutureWarning: Sorting because non-concatenation axis is not aligned.`)*

> Вышеперчисленные функции имеют два аргумента.

#### msg - текст сообщения

#### bold - выводит сообщение жирным шрифтом (либо True либо False, по умолчанию False)
