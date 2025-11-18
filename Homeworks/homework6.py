class Distance:
    _to_meters = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        if unit not in self._to_meters:
            raise ValueError(f"Неизвестная единица измерения: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self._to_meters[self.unit]

    def from_meters(self, meters, unit):
        return meters / self._to_meters[unit]

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        total_m = self.to_meters() + other.to_meters()

        new_value = self.from_meters(total_m, self.unit)
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        total_m = self.to_meters() - other.to_meters()
        new_value = self.from_meters(total_m, self.unit)
        return Distance(new_value, self.unit)

if __name__ == "__main__":
    a = Distance(10, "m")
    b = Distance(2, "km")
    c = Distance(150, "cm")

    print(a)
    print(b)
    print(c)

    print(a + b)
    print(b - a)
    print(a + c)