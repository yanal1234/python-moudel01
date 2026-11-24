#!/usr/bin/env python3
class Plant:
    name: str
    height: float
    age_day: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_day = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_day} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_day += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose: Plant = Plant("Rose", 25.0, 30)
    rose.show()
    count: int = 1
    while count <= 7:
        print(f"=== Day {count} ===")
        rose.grow()
        rose.age()
        count += 1
        rose.show()
    print(f"Growth this week: {7 * 0.8:.1f}cm")
