import math


class Vector3:

    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def origin():
        return origin

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return self + (-1 * other)

    def __mul__(self, other):
        if other is float:
            return self.mul_with_scalar(other)
        elif other is Vector3:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other: float):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __floordiv__(self, other):
        return Vector3(self.x / other, self.y / other, self.z / other)

    def __len__(self):
        return self.length()

    def __str__(self):
        return f"{str(self.x)}, {str(self.y)}, {str(self.z)}"

    def mul_with_scalar(self, scalar: float):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def normalize(self):
        length = self.length()
        return Vector3(self.x / length, self.y / length, self.z / length)

    def cross_product(self, other):
        return Vector3(self.y * other.z - self.z * other.y,
                       self.z * other.x - self.x * other.z,
                       self.x * other.y - self.y * other.x)

    def distance_to(self, other) -> float:
        return math.sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2) + pow(self.z - other.z, 2))


origin = Vector3(0, 0, 0)
