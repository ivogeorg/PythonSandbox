class TwoWeapons:
    def __init__(self, weapon1, weapon2):
        if weapon1 > weapon2:
            self.weapon1 = weapon2
            self.weapon2 = weapon1
        else:
            self.weapon1 = weapon1
            self.weapon2 = weapon2

    def __hash__(self):
        return hash((self.weapon1, self.weapon2))

    def __eq__(self, other):
        return self.weapon1 == other.weapon1 and self.weapon2 == other.weapon2

    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    weapondict = {
        TwoWeapons('lizard', 'spock'): 'lizard poisons spock',
        TwoWeapons('rock', 'spock'): 'spock crushes spock'
    }

    print(weapondict)

    print(TwoWeapons('spock', 'lizard'))

    print(weapondict[TwoWeapons('spock', 'lizard')])

    print(weapondict[TwoWeapons('lizard', 'spock')])

    print(isinstance(TwoWeapons('spock', 'lizard'), TwoWeapons))
