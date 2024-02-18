
class Game:

    def __init__(self):
        self.player1 = input("Hello! Please enter your name as the 1st player: ")
        self.player2 = input("Hello! Please enter your name as the 2nd player: ")
        self.table = { 0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''}
        self.player1_shape = input(f'{self.player1}, please choose your shape: O or X?')
        self.player2_shape = input(f'{self.player2}, please choose your shape: O or X?')


    
    def take_turn(self, player):
        tile_number = input(f"{player}'s turn: ")
        return tile_number

    def start_game(self ):
        current_player = self.player1
        is_table_filled = all(isinstance(value, str) and value.strip() for value in self.table.values())
        while not is_table_filled:
            tile_number = self.take_turn(current_player)
            if self.table[int(tile_number)] == '':
                self.table[int(tile_number)] = self.player1_shape if current_player == self.player1 else self.player2_shape
            else:
                print("That tile is filled. Please enter another one.")
                current_player = self.player2 if current_player == self.player1 else self.player1

            current_player = self.player2 if current_player == self.player1 else self.player1
            if self.check_winner(self.player1):
                print(f"{self.player1} has won!!!")
                break
            elif self.check_winner(self.player2):
                print(f"{self.player2} has won!!!")
                break
            elif is_table_filled:
                print("It's a tie!")
                break
       

    def check_winner(self, player):
        winning_combos = [
                [0,1,2], [3,4,5], [6,7,8],
                [0,3,6], [1,4,7], [2,5,8],
                [0,4,8], [2,4,6]
            ]
        for combination in winning_combos:
            if all(self.table[tile_number] == self.player1_shape for tile_number in combination):
                if player == self.player1:
                    return True
            elif all(self.table[tile_number] == self.player2_shape for tile_number in combination):
                if player == self.player2:
                    return True
        return False


            

game_board_str = '''
    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
'''

print("Welcome to TIC-TAC-TOE!")
print(game_board_str)
game = Game()
print("Enter a number that corresponds to a point on the board as shown on the table.")
game.start_game()


