#!/usr/bin/env python3
class Plant:
    _name: str
    _height: float
    _age_day: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_day = age

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,", f"{self._age_day} days old")

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._age_day += 1


class Flower(Plant):
    _color: str
    _bloomed: bool

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if not self._bloomed:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._bloomed = True


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of",
            f"{self._height}cm long and",
            f"{self._trunk_diameter}cm wide.",
        )


class Vegetable(Plant):
    _harvest_season: str
    _nutritional_value: int

    def __init__(self, name: str, height: float, age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")

    def grow(self) -> None:
        self._height += 2.1
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")

    for _ in range(20):
        tomato.grow()
        tomato.age()

    tomato.show()
