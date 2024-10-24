from abc import abstractmethod, ABC


class Display(ABC):
    @abstractmethod
    def display(self, book_content: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book_content: str) -> None:
        print(book_content)


class ReverseDisplay(Display):
    def display(self, book_content: str) -> None:
        print(book_content[::-1])
