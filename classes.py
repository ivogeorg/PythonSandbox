circle = 'circle'


class CoinflipGame:
    def __init__(self, di, sd, sk, sq):
        self.diamond = di
        self.small_diamond = sd
        self.skull = sk
        self.square = sq
        self.circle = circle
        self.ellipse = 'ellipse'

    def display(self):
        print(self.diamond, self.small_diamond, self.skull, self.square)

    def test(self):
        self.display()


game = CoinflipGame('diamond', 'small_diamond', 'skull', 'square')
game.display()
