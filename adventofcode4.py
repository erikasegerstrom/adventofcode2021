from typing import List
import numpy as np

class Board():
    def __init__(self, board_numbers: List[List[int]]) -> None:
        self.board_numbers = np.array(board_numbers)
        self.drawn_numbers = np.ones((5,5))
        self.bingo = False

    def update_drawn_numbers(self, random_number: int) -> None:
        index = np.where(self.board_numbers == random_number)
        self.drawn_numbers[index] = 0
    
    def is_bingo(self) -> bool:
        sum_columns = np.sum(self.drawn_numbers, axis=0)
        sum_rows = np.sum(self.drawn_numbers, axis=1)
        if (0 in sum_columns) or (0 in sum_rows):
            self.bingo = True
            return True
        else:
            self.bingo = False
            return False

    def calculate_sum_of_matrix_elements(self) -> int:
        product = np.multiply(self.board_numbers, self.drawn_numbers)
        sum = int(np.sum(product))
        return sum

    @staticmethod
    def parse(raw: str) -> 'Board':
        grid = [
            [int(n) for n in row.split()]
            for row in raw.split('\n')
        ]
        return Board(grid)

class Game():
    def __init__(self, boards: List[Board], random_numbers: List[int]) -> None:
        self.boards = boards
        self.random_numbers = random_numbers

    def play_bingo(self):
        """
        Loop through random numbers, update boards and check for bingo
        """
        for number in self.random_numbers:   
            for i, board in enumerate(self.boards):
                board.update_drawn_numbers(number)
                if board.is_bingo():
                    sum_of_elements = board.calculate_sum_of_matrix_elements()
                    result = sum_of_elements * number
                    print("Assignment 1: ", i, result)
                    exit()

    def play_bingo_find_last(self):
        """
        Loop through random numbers, update boards and check for bingo.
        Return last board to bingo including board score.
        """
        for number in self.random_numbers:   
            for i, board in enumerate(self.boards):
                if board.bingo == False:
                    board.update_drawn_numbers(number)
                    if board.is_bingo():
                        sum_of_elements = board.calculate_sum_of_matrix_elements()
                        result = sum_of_elements * number

        print("Assignment 2: ", i, result)
                    

if __name__ == "__main__":
    raw = open('inputs/day04.txt').read()
    paragraphs = raw.split("\n\n")
    random_numbers = [int(n) for n in paragraphs[0].split(",")]

    paragraphs = paragraphs[1:]
    bingo_boards = [Board.parse(paragraph) for paragraph in paragraphs]

    game = Game(bingo_boards, random_numbers)
    #game.play_bingo()
    game.play_bingo_find_last()