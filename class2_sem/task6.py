from abc import ABC, abstractmethod


class ComputerColor(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


class Color(ComputerColor):
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        END = "\033[0"
        START = "\033[1;38;2"
        MOD = "m"
        return f"{START};{self.r};{self.g};{self.b}{MOD}•{END}{MOD}"

    def __eq__(self, other: "Color"):
        if not isinstance(other, Color):
            raise TypeError
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __add__(self, other: "Color"):
        if not isinstance(other, Color):
            raise TypeError
        return Color((self.r + other.r) % 256, (self.g + other.g) % 256, (self.b + other.b) % 256)

    def __hash__(self):
        return hash((self.r, self.g, self.b))

    @staticmethod
    def _contrast_color(color: int, c: float):
        cl = -256 * (1 - c)
        f = (259 * (cl + 255)) / (255 * (259 - cl))
        return int(f * (color - 128) + 128)

    def __mul__(self, c: float):
        if c < 0 or c > 1:
            raise ValueError
        return Color(Color._contrast_color(self.r, c), Color._contrast_color(self.g, c), Color._contrast_color(self.b, c))

    def __rmul__(self, c: float):
        if c < 0 or c > 1:
            raise ValueError
        return Color(Color._contrast_color(self.r, c), Color._contrast_color(self.g, c), Color._contrast_color(self.b, c))


if __name__ == "__main__":
    hsl_color = Color(255, 20, 110)
    print_a(hsl_color)
