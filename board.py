import pygame

class Board:
    def __init__(self, width,height,screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.rows = 9
        self.cols = 9
        self.size = self.width // self.cols
        if self.difficulty == "easy":
            cells = 30
        elif self.difficulty == "medium":
            cells = 40
        else:
            cells = 50
        self.original_board = []
        for row in range(self.rows):
            new_row = []
            for col in range(self.cols):
                value = self.board[row][col]

