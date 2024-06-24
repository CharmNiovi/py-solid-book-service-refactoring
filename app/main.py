import json
import xml.etree.ElementTree as ET # NOQA N817


class ConsoleBook:
    def display_console(self) -> None:
        print(self.content)

    def print_console(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReverseBook:
    def print_reverse(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def display_reverse(self) -> None:
        print(self.content[::-1])


class SerializeBook:
    def serialize_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml(self) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


class Book(ConsoleBook, ReverseBook, SerializeBook):
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def choose_method(self, cmd: str, method_type: str) -> str:
        method_name = self.get_specific_method(cmd, method_type)
        if method_name:
            method = getattr(self, method_name)
            return method()
        raise ValueError(f"Unknown {cmd} type: {method_type}")

    @classmethod
    def get_specific_method(cls, cmd: str, method_type: str) -> str:
        for method_name in dir(cls):
            if cmd in method_name and method_type in method_name:
                return method_name
        return ""


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        result = book.choose_method(cmd, method_type)
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
