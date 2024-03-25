class Water:
    def __init__(self):
        self.name = 'Water'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm
        elif isinstance(other, Fire):
            return Par


class Air:
    def __init__(self):
        self.name = 'Air'


class Fire:
    def __init__(self):
        self.name = 'Fire'


class Ground:
    def __init__(self):
        self.name = 'Ground'


class Shtorm:
    def __init__(self):
        self.name = 'Shtorm'

    def __str__(self):
        return 'Шторм !!'



class Par:
    def __init__(self):
        self.name = 'Par'

result = Water() + Air()
print(result)


result_2 = Water() + Fire()
print(result_2)
