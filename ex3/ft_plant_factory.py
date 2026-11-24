#!/usr/bin/env python3
class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


def create_plant(name: str, height: float, age: int) -> Plant:
    return Plant(name, height, age)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    rose: Plant = create_plant("Rose", 25.0, 30)
    oak: Plant = create_plant("Oak", 200.0, 365)
    cactus: Plant = create_plant("Cactus", 5.0, 90)
    sunflower: Plant = create_plant("Sunflower", 80.0, 45)
    fern: Plant = create_plant("Fern", 15.0, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
