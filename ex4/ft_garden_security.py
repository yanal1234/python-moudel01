class Plant:
    _name: str
    _height: float
    _age_day: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age_day = 0
        else:
            self._age_day = age

    def show(self) -> None:
        print(
            f"Plant created: {self._name}:",
            f"{self._height}cm, {self._age_day} days old",
        )

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height:g}cm")

    def get_height(self) -> float:
        return self._height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_day = age
            print(f"Age updated: {age} days")

    def get_age(self) -> int:
        return self._age_day

    def get_name(self) -> str:
        return self._name


def create_plant(name: str, height: float, age: int) -> Plant:
    return Plant(name, height, age)


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = create_plant("Rose", 15.0, 10)
    rose.show()

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print(
        f"Current state: {rose.get_name()}:",
        f"{rose.get_height()}cm, {rose.get_age()} days old",
    )
