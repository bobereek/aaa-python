from abc import ABC, abstractmethod


class PokemonTrainInterface(ABC):
    @abstractmethod
    def increase_experience(self, val):
        pass

    @property
    @abstractmethod
    def experience(self):
        pass


class AlmostBasePokemon(PokemonTrainInterface):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self._experience = 100

    @property
    def experience(self):
        return self._experience

    def increase_experience(self, val: int):
        self._experience += val

    def __str__(self):
        return f"{self.name}/{self.poketype}"
