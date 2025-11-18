from issue_1 import Advert


class ColorizedMixin:
    def __str__(self):
        res = f"\033[1;{self.repr_color_code}m"
        for key, value in self.__dict__.items():
            if key == "repr_color_code":
                continue
            res += f"{value}"
            if key == "price_":
                res += "₽"
            res += " | "
        return res.rstrip(" | ") + "\033[0m"


class ColorizedAdvert(ColorizedMixin, Advert):
    def __init__(self, json_data: dict, color_code: int, is_root=True):
        super().__init__(json_data, is_root)
        self.repr_color_code = color_code
