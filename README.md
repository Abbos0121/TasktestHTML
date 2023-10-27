# Split Message

## Описание

Проект представляет собой функцию `split_message`, которая разделяет HTML-код на фрагменты с учетом ограничения по максимальной длине.

## Использование

Просто вызовите функцию `split_message` и передайте ей HTML-код:

```
from msg_split import split_message

html_text = """
<!DOCTYPE html>
<html>
<body>

<p>This is a <b>sample</b> HTML <i>text</i> for testing.</p>
<p>It contains multiple <span>tags</span> that should be split correctly.</p>

</body>
</html>
"""

fragments = list(split_message(html_text))
print(fragments)
```

## Тестирование

`python -m unittest html_unittest.py`

## Структура проекта

`msg_split.py:` Основной код функции разделения сообщения.

`html_unittest.py:` Тесты для проверки правильности работы функции.

`README.md:` Информация о проекте.

## Лицензия

MIT License


Этот пример включает в себя:

- **Описание проекта:** Краткое описание того, что делает ваш проект.
- **Использование:** Пример кода и описание того, как использовать вашу функцию.
- **Тестирование:** Как запустить тесты.
- **Структура проекта:** Описание файлов в проекте.
- **Лицензия:** Указание лицензии, в данном случае, MIT License.



