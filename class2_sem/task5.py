class Color:
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
    red = Color(255, 0, 0)
    print(0.5 * red)
