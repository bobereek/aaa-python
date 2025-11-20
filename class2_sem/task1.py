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


if __name__ == "__main__":
    red = Color(255, 0, 0)
    print(red)
