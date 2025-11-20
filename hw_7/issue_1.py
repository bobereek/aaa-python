import keyword


class Advert:
    def __init__(self, json_data: dict, is_root=True):
        for key, value in json_data.items():
            if keyword.iskeyword(key) or key == "price":
                attr_name = key + "_"
            else:
                attr_name = key

            if isinstance(value, dict):
                setattr(self, attr_name, Advert(value, is_root=False))
            else:
                setattr(self, attr_name, value)

        if is_root:
            if json_data.get("title") is None:
                raise ValueError("Title is required")
        else:
            if json_data.get("price") is None:
                self.price_ = 0
            else:
                self.price = json_data["price"]

    @property
    def price(self):
        return self.price_

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be >= 0")
        else:
            self.price_ = value
