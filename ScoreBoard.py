from GameEntry import GameEntry

class ScoreBoard:

    def __init__(self, capacity = 10):
        self._board = [None] * capacity
        self._n = 0  # number of players

    def __getitem__(self, k):
        return self._board[k]

    def __str__(self):
        return "".join(str(self._board[j]) + "\n" for j in range(self._n))

    def add(self, entry):
        score = entry.get_score()

        good = self._n < len(self._board) or score > self[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1

            j = self._n - 1
            while j > 0 and self[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j-=1
            self._board[j] = entry

def main():
    player1 = GameEntry("John", 123)
    player2 = GameEntry("Tim", 322)
    player3 = GameEntry("Wong", 3)
    player4 = GameEntry("Tsao", 1000)

    board = ScoreBoard()
    board.add(player1)
    board.add(player2)
    board.add(player3)
    board.add(player4)

    print(board)

if __name__ == '__main__':
    main()
