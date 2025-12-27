class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
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


if __name__ == "__main__":
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)

    print(red + green)
