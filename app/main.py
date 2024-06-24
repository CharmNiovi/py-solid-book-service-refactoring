import json
import xml.etree.ElementTree as ET


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def chose_method(self, cmd: str, method_type: str):
        i = self.get_spicific_method(cmd, method_type)
        if i:
            return getattr(self, i[0])()
        raise ValueError(f"Unknown {cmd} type: {method_type}")

    @classmethod
    def get_spicific_method(cls, cmd: str, method_type: str) -> list:
        return [i for i in dir(cls) if cmd in i and method_type in i]

    def display_console(self):
        print(self.content)

    def print_console(self):
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_reverse(self):
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def display_reverse(self):
        print(self.content[::-1])

    def serialize_json(self):
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.title
        content = ET.SubElement(root, "content")
        content.text = self.content
        return ET.tostring(root, encoding="unicode")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        book.chose_method(cmd, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
