import json
import xml.etree.ElementTree as ET # NOQA N817


class Display:
    @staticmethod
    def console(content: str) -> None:
        print(content)

    @staticmethod
    def reverse(content: str) -> None:
        print(content[::-1])


class Print:
    @staticmethod
    def console(title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)

    @staticmethod
    def reverse(title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


class Serialize:
    @staticmethod
    def json(title: str, content: str) -> str:
        return json.dumps({"title": title, "content": content})

    @staticmethod
    def xml(title: str, content: str) -> str:
        root = ET.Element("book")
        et_title = ET.SubElement(root, "title")
        et_title.text = title
        et_content = ET.SubElement(root, "content")
        et_content.text = content
        return ET.tostring(root, encoding="unicode")


class Book:
    strategy = {
        "display": {
            "console": Display.console,
            "reverse": Display.reverse
        },
        "print": {
            "console": Print.console,
            "reverse": Print.reverse
        },
        "serialize": {
            "json": Serialize.json,
            "xml": Serialize.xml
        }
    }

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        display_strategy = self.strategy["display"].get(display_type)
        if not display_strategy:
            raise ValueError(f"Unknown display type: {display_type}")
        display_strategy(self.content)

    def print_book(self, print_type: str) -> None:
        print_strategy = self.strategy["print"].get(print_type)
        if not print_strategy:
            raise ValueError(f"Unknown print type: {print_type}")
        print_strategy(self.title, self.content)

    def serialize(self, serialize_type: str) -> str:
        serialize_strategy = self.strategy["serialize"].get(serialize_type)
        if not serialize_strategy:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return serialize_strategy(self.title, self.content)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
