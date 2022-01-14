class Glass:
    def __init__(self, material: str):
        self.material = None
        self.get_material(material)

    def get_material(self, material) -> None:
        if not isinstance(material, str):
            raise TypeError('ojoj')
        self.material = material

class Glass:
    def __init__(self):

if __name__ == "__main__":

    glass = Glass('plastic')
    print(glass.material)
