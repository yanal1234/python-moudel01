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

    rose = create_plant("Rose", 25.0, 30)
    oak = create_plant("Oak", 200.0, 365)
    cactus = create_plant("Cactus", 5.0, 90)
    sunflower = create_plant("Sunflower", 80.0, 45)
    fern = create_plant("Fern", 15.0, 120)

    rose.show()
    oak.show()
    cactus.show()
    sunflower.show()
    fern.show()
