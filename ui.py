"""Every string on the game must be taken from here
"""
class UI:
    def __init__(self) -> None:
        self.language = 'English'

    def select_language_options(self):
        return {'1': 'ENGLISH', '2': 'PORTUGUES'}

    def select_game_command(self):
        returns = {'English': 'SELECT LANGUAGE',
                    'Portugues': 'SELECIONAR IDIOMA'}
        
        return returns[self.language]

    def main_menu_options(self):
        returns = {'English': {'1': 'PLAY', '2':'SELECT LANGUAGE', '3': 'HOW TO PLAY', '4':'EXIT'},
                    'Portugues': {'1': 'JOGAR', '2':'SELECIONAR IDIOMA','3': 'COMO JOGAR', '4':'SAIR'}}

        return returns[self.language]
    
    def main_menu_command(self):
        returns = {'English': 'MENU OPTIONS',
                    'Portugues': 'MENU DE OPÇÕES'}

        return returns[self.language]

    def pre_game_options(self):
        returns = {'English': {'1': 'START', '2': 'RETURN'},
                    'Portugues': {'1': 'COMEÇAR', '2': 'VOLTAR'}}
                
        return returns[self.language]
    
    def pre_game_command(self):
        returns = {'English': 'GAME',
                    'Portugues': 'JOGO'}
                
        return returns[self.language]

    def select_opponent_options(self):
        returns = {'English': {'1': 'LOCAL MULTIPLAYER', '2': 'CPU'},
                    'Portugues': {'1': 'MULTI JOGADOR LOCAL ', '2': 'COMPUTADOR'}}

        return returns[self.language]
    
    def select_opponent_command(self):
        returns = {'English': 'PICK YOUR OPPONENT',
                    'Portugues': 'SELECIONE SEU OPONENTE'}

        return returns[self.language]

    def select_difficulty_options(self):
        returns = {'English': {'1': 'EASY', '2': 'MEDIUM', '3': 'HARD'},
                    'Portugues': {'1': 'FACIL', '2': 'MEDIO', '3': 'DIFICIL'}}

        return returns[self.language]
    
    def select_difficulty_command(self):
        returns = {'English': 'PICK YOUR DIFFICULTY',
                    'Portugues': 'SELECIONE SUA DIFICULDADE'}

        return returns[self.language]

    def show_turn(self, turn):
        returns = {'English': f'player {turn} turn!',
                    'Portugues': f'Vez do jogador {turn}'}

        return returns[self.language]

    def get_user_input_play(self):
        returns = {'English': 'PLACE MARK ON:\n',
                    'Portugues': 'COLOCAR MARCA NO:\n'}

        return returns[self.language]

    def win_message(self, winner:str, position:str):
        returns = {'English': f'PLAYER {winner} WON THE GAME ON THE {position.upper()}!',
                    'Portugues': f'JOGADO {winner} GANHOU O JOGO NA POSIÇÃO {position.upper()}!'}

        return returns[self.language]

    def draw_message(self):
        returns = {'English': 'THE GAME ENDED UP ON A DRAW!',
                    'Portugues': 'O JOGO TEMINOU UM UM EMPATE!'}

        return returns[self.language]

    def positions(self, position):
        returns = {'English': {'diagonal': 'diagonal', 'line': 'line', 'column': 'column'},
                    'Portugues': {'diagonal': 'diagonal', 'line': 'linha', 'column': 'coluna'}}

        return returns[self.language][position]


    def how_to_play(self):
        returns = {'English': 'You will play as the "x", and your opponent as the "o".\n\nIn your turn, enter the position you want to play:\nThe number 1 indicates the upper left corner: the 2, the upper middle and so on.\n\n the first player completing 3 signs on either horizontal, vertical or diagonal first wins.\n\nGOOD LUCK!',
                    'Portugues': 'Você irá jogar como o "x", e o seu oponente como o "o".\n\nNa sua vez, digite a posição que deseja jogar:\nO número 1 indica o canto superior esquerdo: o 2, o meio superior e assim por diante.\n\n o primeiro jogador a conpletar 3 de sinais em qualquer horizontal, vertical ou diagonal primeiro vence.\n\nBOA SORTE!'}

        return returns[self.language]