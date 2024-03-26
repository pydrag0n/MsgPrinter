![](imgs/logo.png)


# MsgPrinter

Простая библиотека для вывода информационных сообщений, и не только

✅ Вывод информационных сообщений.

✅ Время вывода

✅ Измерение времени работы функции 

🚫 Запись логов


## install
```sh
pip install message_printer
```

## example
```python
import message_printer
import time
mp = message_printer.MessagePrinter()

@mp.timer
def textwrite(text):
    time.sleep(2)
    return text

textwrite("hi world")
mp.info_message("Информируюущее сообщение", bold=True)
mp.error_message("Сообщение об ошибке", bold=True)
mp.warning_message("Предупреждающее сообщение")
```
![output](imgs/example.png)

#### version: 0.0.3
