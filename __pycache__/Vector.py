class Vector:

    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        if isinstance(d, list):
            self._coords = d
        else:
            self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

def main():
    vec1 = Vector([23, 45, 12, 23, 1])
    vec2 = Vector([92, 21, 234, 55, 7])
    vec3 = Vector(8)

    print(vec1 + vec2) # <115, 66, 246, 78, 8>
    print(vec1 != vec2) # True
    print(vec3) # <0, 0, 0, 0, 0, 0, 0, 0>

if __name__ == '__main__':
    main()