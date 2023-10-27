from typing import Generator
from bs4 import BeautifulSoup

MAX_LEN = 4096


def normalize_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    return str(soup)


def split_message(source: str, max_len=MAX_LEN) -> Generator[str, None, None]:
    current_fragment = ""
    current_fragment_len = 0

    soup = BeautifulSoup(source, 'html.parser')  #Создаем объект BeautifulSoup для парсинга HTML

    for tag in soup.find_all(True):  #Итерируемся по всем тегам в HTML
        tag_str = str(tag)

        if current_fragment_len + len(tag_str) > max_len:           #Если добавление текущего тега превысит максимальную длину, начинаем новый фрагмент
            yield current_fragment
            current_fragment = ""
            current_fragment_len = 0

        current_fragment += tag_str
        current_fragment_len += len(tag_str)

    if current_fragment:
        yield current_fragment


if __name__ == "__main__":
    html_text = """
    <!DOCTYPE html>
    <html>
    <body>

    <p>This is a <b>sample</b> HTML <i>text</i> for testing.</p>
    <p>It contains multiple <span>tags</span> that should be split correctly.</p>

    </body>
    </html>
    """

    for fragment in split_message(html_text):
        print(fragment)


