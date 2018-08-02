class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '{}, {}'.format(self._name, self._score)

def main():
    player1 = GameEntry("John", 123)

    print(player1)

if __name__ == '__main__':
    main()