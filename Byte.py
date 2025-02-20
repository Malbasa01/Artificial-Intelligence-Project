import random
import copy

class ByteGame:
    def __init__(self, board_size, player_mode='C'):
        self.beli_stekovi=0
        self.crni_stekovi=0
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size * 4)] for _ in range(board_size * 4)]
        self.bele_figure = []  # Dodatni atribut za cuvanje informacija o belim figurama
        self.crne_figure = []  # Dodatni atribut za cuvanje informacija o crnim figurama
        self.current_player = 'X'  # 'O' za belog igraca, 'X' za crnog igraca
        self.player_mode = player_mode #mod igre (covek/racunar) (covek/covek)
        self.svi_stekovi=[]
                       
    
    def initialize_board(self):
        # Postavi tablu na početno stanje
        row_count=0
        col_count=1
        for i in range(0, self.board_size * 4, 4):
            for j in range(0, self.board_size * 4, 4):
                self.board[i][j]=' '
                if (i // 4 + j // 4) % 2 == 0:
                    # Crno polje
                    
                    self.board[i][j:j + 3] = ['.', '.', '.']
                    self.board[i + 1][j:j + 3] = ['.', '.', '.']
                    if(row_count==0 or row_count==self.board_size-1):
                        self.board[i + 2][j:j + 3] = ['.', '.', '.']
                    else:
                        if(row_count%2==0):
                            self.board[i + 2][j:j + 3] = ['O', '.', '.']
                            self.bele_figure.append({'player': 'O', 'height': 0, 'position': [i+2, j], 'row':chr(ord('A') + row_count),'col':col_count})
                        else:
                            self.board[i + 2][j:j + 3] = ['X', '.', '.']
                            self.crne_figure.append({'player': 'X', 'height': 0, 'position': [i+2, j], 'row':chr(ord('A') + row_count),'col':col_count})   
                        
                else:
                    # Belo polje
                    self.board[i][j:j + 3] = [' ', ' ', ' ']
                    self.board[i + 1][j:j + 3] = [' ', ' ', ' ']
                    self.board[i + 2][j:j + 3] = [' ', ' ', ' ']
                col_count=col_count+1    
                    
            row_count=row_count+1
            col_count=1    

        
    def empty_board(self):
        for i in range(0, self.board_size * 4, 4):
            for j in range(0, self.board_size * 4, 4):
                if (i // 4 + j // 4) % 2 == 0:
                    # Crno polje
                    self.board[i][j:j + 3] = '...'
                    self.board[i + 1][j:j + 3] = '...'
                    self.board[i + 2][j:j + 3] = '...'
                else:
                    # Belo polje
                    self.board[i][j:j + 3] = '   '
                    self.board[i + 1][j:j + 3] = '   '
                    self.board[i + 2][j:j + 3] = '   '                  
    
   
    def evaluate(self, beli_stekovi, crni_stekovi):
        if(self.board_size==8):
            if(beli_stekovi==2):
                if self.current_player == 'X':
                    return -10
                else:
                    return 10
            else:
                if(crni_stekovi==2):
                    if self.current_player =='O':
                        return 10
                    else:
                        return -10
                else:
                    if self.current_player =='O':
                        return -10
                    else:
                        return 10
        return 0
    

            
                
    def display_board(self):
        b=self.beli_stekovi
        c=self.crni_stekovi
        
        print("       ", end=' ')
        for i in range(1, self.board_size + 1):
            print(i, end='           ')
        print()    
        print()
        for i, row in enumerate(self.board):
            if i % 4 == 1:
                current_row_letter = chr(ord('A') + i // 4)
                print(f"{current_row_letter}  ", end="")
            else:
                print("   ", end="")

            frmt = "{:>3}" * len(row)
            print(frmt.format(*row))
        print()
        print("Crni:",c, "-------", "Beli:",b)    
    #--------------------------------------------------------------------------------------------------------------------------------------------        
    def is_game_over(self):
        # Provera kraja igre
        # Igra se završava ako je tabla prazna ili jedan od igrača ima više od polovine stekova
        prazna=True
        for i in range(self.board_size*4):
            for j in range(self.board_size*4):
                if self.board[i][j] not in ['.', '']:
                    prazna=False
        if(prazna==True):
            print("Game over")
            return True
        if(self.board_size==8):
            if(self.beli_stekovi==2):
                print("Pobednik je beli!!!")
                return True
            else:
                if(self.crni_stekovi==2):
                    print("Pobednik je crni!!!")
                    return True
        
        elif(self.board_size==10):
            if(self.beli_stekovi==3):
                print("Pobednik je beli!!!")
                return True
            else:
                if(self.crni_stekovi==3):
                    print("Pobednik je crni!!!")
                    return True            
        
        elif(self.board_size==16):
            if(self.beli_stekovi==8):
                print("Pobednik je beli!!!")
                return True
            else:
                if(self.crni_stekovi==8):
                    print("Pobednik je crni!!!")
                    return  True
        else:
            print("Next move")    
            return False
    #--------------------------------------------------------------------------------------------------------------------------------------------        
    def choose_first_player(self):
        while True:
            choice = input("Ko će igrati prvi? (X-crni, O - beli): ").upper()
            if choice == 'O':
                self.current_player = 'O'  # Postavljamo da beli igra prvi
                break
            elif choice == 'X':
                self.current_player = 'X'  # Postavljamo da crni igra prvi (za primer)
                break
            else:
                print("Nepoznata opcija. Molimo vas da unesete 'X' ili 'O'.")

    def get_board_size_from_user(self):
        # Unos dimenzije table od strane korisnika
        valid_sizes = [8, 10, 16]

        while True:
            try:
                size = int(input("Unesite dimenziju table (8, 10 ili 16): "))
                if size in valid_sizes:
                    self.board_size = size
                    break
                else:
                    print("Dimenzija table mora biti jedan od brojeva 8, 10 ili 16.")
            except ValueError:
                print("Neispravan unos. Unesite celobrojnu vrednost.")
 
    def switch_player(self):      
        self.current_player = 'X' if self.current_player == 'O' else 'O'
    #--------------------------------------------------------------------------------------------------------------------------------------------        


    def start_game(self):
        self.get_board_size_from_user()
        self.initialize_board()
        

        player_mode = input("Izaberite način igre ( H - čovek protiv čoveka): ").upper()
        self.player_mode = player_mode

        self.choose_first_player()
        self.display_board()

        while not self.is_game_over():
            print(f"\nTrenutni igrač: {self.current_player}")

            if self.player_mode == 'R' and self.current_player == 'X':
                # Ako je na potezu računar, neka izvrši potez
                #self.computer_make_move()
                print("Racunar je na potezu")
            else:
                # Ako je na potezu čovek, neka unese potez
                try:
                    old_x = input("Unesite red (A,B,C...): ")
                    old_y = int(input("Unesite kolonu(1,2,3,...) : "))
                    stack_index = int(input("Unesite indeks steka(0,1...7): "))
                    
                    x=self.convert_letter_to_number(old_x)
                    y=self.convert_number_to_new_number(old_y)
                    
                    direction = input("Unesite smer (GL, GD, DL, DD): ")
                    move_x, move_y = 0, 0
                    num_of_figures = int(input("Unesite broj figura: "))
                    if direction == 'GL':
                        move_x = -4
                        move_y = -4
                    elif direction == 'GD':
                        move_x = -4
                        move_y = 4
                    elif direction == 'DL':
                        move_x = 4
                        move_y = -4
                    else:
                        move_x = 4
                        move_y = 4
                    move = (x, y, stack_index, direction, move_x, move_y, num_of_figures,self.current_player)

                    # Provera ispravnosti poteza i odigravanje poteza
                    if self.valid_move_2(move):
                        #self.make_move(move)
                        #self.switch_player()
                        test = self.make_move(move)
                        if test:
                            print("Potez ispravan")
                            self.switch_player()
                            
                        #self.display_board()
                        if(self.is_game_over()==True):
                            break

                    else:
                        print("Neispravan potez. Pokušajte ponovo.")

                except ValueError:
                    print("Neispravan unos. Unesite broj.")
                except IndexError:
                    print("Neispravan unos. Indeks steka izvan opsega.")
                except Exception as e:
                    print(f"Greška: {e}")

        print("Kraj igre.")



    def is_valid_move(self, move):
            position, stack_index, direction = move
            x, y = position
            
            
            # Provera da li zadato polje postoji na tabli
            valid_range1= set(chr(ord('A') + j) for j in range(self.board_size))
            if x not in valid_range1:
                print("Invalid row")
                return
            valid_range2 = set(range(1, self.board_size))
            if y not in valid_range2:
                print("Invalid column")
                return

            # Provera da li postoje figure na zadatom polju i Provera da li postoji figura na zadatom mestu na steku na zadatom polju
            postoji=False
            if(self.current_player=='O'):
                for figure in self.bele_figure:
                    if figure['row'] == x and figure['col'] == y and figure['height'] == stack_index:
                        postoji=True
                if postoji==False:
                    print("Figura ne postoji")
                    return    
            else:
                for figure in self.crne_figure:
                    if figure['row'] == x and figure['col'] == y and figure['height'] == stack_index:
                        postoji=True
                if postoji==False:
                    print("Figura ne postoji")
                    return    
            
            # Provera da li je smer jedan od četiri moguća
            if direction not in ['GL', 'GD', 'DL', 'DD']:
                print("Neispravan potez. Nije izabran ispravan smer.")
                return False

            # Ako sve provere prođu, potez je ispravan
            return True
#---------------------------------------------------------------------------------------------------------------------------
    def valid_move_2(self, move):
        # out of bounds
        print("Uslo u valid move funkciju!")
        x, y, stack_index, direction, move_x, move_y, num_of_figures,current_player = move
        # Check if indices are within the valid range
        if not (0 <= x < len(self.board) and 0 <= y < len(self.board[0])):
            print("Invalid indices.")
            return False
        
        
        
        if(self.board[x][y]!=current_player):
            print("Pogresna figura")
            return False
        
        if(x==2):
            if direction=='GL' or direction=='GL':
                print("Potez van granica!")
                return False
        
        if(y==0):
            if direction=='GL' or direction=='DL':
                print("Potez van granica!")
                return False
        
        if(y==28):
            if direction=='GD' or direction=='DD':
                print("Potez van granica!")
                return False    
        
        if(x==30 ):
            if direction=='DD' or direction=='DL':
                print("Potez van granica!")
                return False
        # Ostalo 
         
        
        if(y==0):
            if(self.board[x-4][y+4]=='.' and
            self.board[x+4][y+4]=='.'):
                correct_move = self.find_nearest_figure((x, y))
                if correct_move[1]:
                    if direction != correct_move[1]:
                        print("Udaljavate se od najblize figure!")
                        return False       
            else:
                if(direction=='GD' and self.board[x-4][y+4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False
                if(direction=='DD' and self.board[x+4][y+4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False

        elif(y==28):
            if(self.board[x-4][y-4]=='.' and
            self.board[x+4][y-4]=='.'):
                correct_move = self.find_nearest_figure((x, y))
                if correct_move[1]:
                    if direction != correct_move[1]:
                        print("Udaljavate se od najblize figure!")
                        return False       
            else:
                if(direction=='GL' and self.board[x-4][y-4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False
                if(direction=='DL' and self.board[x+4][y-4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False            
                                                              
        else:
            if(self.board[x-4][y+4]=='.' and
            self.board[x-4][y-2]=='.' and
            self.board[x+4][y+4]=='.' and
            self.board[x+4][y-2]=='.'):
                correct_move = self.find_nearest_figure((x, y))
                if correct_move[1]:
                    if direction != correct_move[1]:
                        print("Udaljavate se od najblize figure!")
                        return False       
            else:
                if(direction=='GL' and self.board[x-4][y-4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False
                if(direction=='GD' and self.board[x-4][y+4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False
                if(direction=='DL' and self.board[x+4][y-4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False
                if(direction=='DD' and self.board[x+4][y+4]=='.'):
                    print("Nisu sva susedna polja prazna!")
                    return False            

        print("Dobar potez")    
        return True
    
    
    def find_nearest_figure(self, specific_position):
        
        all_figures = self.bele_figure + self.crne_figure

        def calculate_distance(pos1, pos2):
            # Calculate the Manhattan distance between two positions
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        nearest_figure = None
        min_distance = float('inf')

        for figure in all_figures:
            if figure['position'] == specific_position:
                continue  # Skip the specific figure itself
            distance = calculate_distance(specific_position, figure['position'])
            if distance < min_distance:
                min_distance = distance
                nearest_figure = figure['position']

        if nearest_figure is not None:
            direction = ''
            row_diff = nearest_figure[0] - specific_position[0]
            col_diff = nearest_figure[1] - specific_position[1]

            if row_diff > 0:
                direction += 'D'
            elif row_diff < 0:
                direction += 'G'

            if col_diff > 0:
                direction += 'D'
            elif col_diff < 0:
                direction += 'L'

            return [nearest_figure, direction]

        return [None, None]  
        
    
    
    
    
    
    
    def figure_on_field(self, x, y):
        if self.board[x][y]!='.' and self.board[x][y]!=' ':
            return True
        else:
            return False
    
    def make_move(self, move):
        x, y, stack_index, direction, move_x, move_y, num_of_figures,current_player = move
        
        board = copy.deepcopy(self.board)
        
        if not self.valid_move_2(move):
            print("Nepravilan potez!")
            return False
        else:
            new_x = x + move_x
            new_y = y + move_y
            counter = 0
            if self.figure_on_field(new_x, new_y):
                for i in range(new_x, new_x-3, -1):
                    for j in range(new_y, new_y+3):
                        if board[i][j] != '.' and board[i][j] != ' ':
                            counter+=1
            current_couter = 0
            for i in range(x, x-3, -1):
                for j in range(y, y+3):
                    if board[i][j] != '.' and board[i][j] != ' ':
                        current_couter+=1                        
            if(counter + num_of_figures) > 8:
                print("Previse figura zelite da premestite!")
                return False
            if (counter + num_of_figures) < current_couter:
                print("Losa visina steka!")
                return False
            
            num_of_figs = num_of_figures - 1
            figures = []
            indicator = 0
            
            
            for i in range(x-2, x+1):
                for j in range(y+2, y-1, -1):
                    if board[i][j] != '.' and num_of_figs>=0:
                        figures.append(board[i][j])
                        board[i][j] = '.'
                        num_of_figs-=1

            if figures[-1]!=current_player:
                print("Poslednja figura u steku koji se pomera mora biti vase boje!")
                return False
                
            figure_counter = num_of_figures - 1           
            for i in range(new_x, new_x-3, -1):
                for j in range(new_y, new_y+3):
                    if board[i][j] == '.' and figure_counter>=0:
                        board[i][j] = figures[figure_counter]
                        figure_counter = figure_counter - 1
            
            counter = 0
            boja='N'
            
            for i in range(new_x, new_x-3, -1):
                for j in range(new_y, new_y+3):
                    if board[i][j] != '.' and board[i][j] != ' ':
                        counter+=1
                        if(counter==8):
                            boja=board[i][j]
                                
            if(counter==8):
                for i in range(new_x, new_x-3, -1):
                    for j in range(new_y, new_y+3):
                        if board[i][j] != '.' and board[i][j] != ' ':
                            board[i][j]='.'
            if(boja=='X'):
                self.crni_stekovi+=1
            if(boja=='O'):    
                self.beli_stekovi+=1
            
        self.board = copy.deepcopy(board)                               
        self.display_board()
        return True
                
               
             
        
    



    def convert_letter_to_number(self, letter):
        
        if not isinstance(letter, str) or len(letter) != 1 or not letter.isupper():
            raise ValueError("Input must be a single capital letter.")

        base_number = ord('A') - 1  # ASCII value of 'A' minus 1
        letter_number = ord(letter) - ord('A') + 1

        return letter_number * 4 - 2
    
    def convert_number_to_new_number(self, number):
        
        if not isinstance(number, int) or number < 1:
            raise ValueError("Input must be a positive integer greater than or equal to 1.")

        return (number - 1) * 4       

    def generate_all_moves(self):
        all_moves = {"Loši potezi": [], "Dobri potezi": []}
        player_moves = self.crne_figure if self.current_player == 'X' else self.bele_figure 
        current_player = 'X' if self.current_player == 'X' else 'O'

        for figure in player_moves:
            x, y, stack_index = figure['row'], figure['col'], figure['height']
            print(f"Player: {figure['player']}, Height: {figure['height']}, Position: {figure['position']}, Row: {figure['row']}, Col: {figure['col']}")


            
            x = self.convert_letter_to_number(x)
            y = self.convert_number_to_new_number(int(y))

            for direction in ['GL', 'GD', 'DL', 'DD']:
                move_x, move_y = 0, 0

                if direction == 'GL':
                    move_x, move_y = -4, -4
                elif direction == 'GD':
                    move_x, move_y = -4, 4
                elif direction == 'DL':
                    move_x, move_y = 4, -4
                else:
                    move_x, move_y = 4, 4

                new_x, new_y = x + move_x, y + move_y
                move_type=""
                if self.valid_move_2((x, y, stack_index, direction, move_x, move_y, 1,current_player)):
                    move_type = "Dobri potezi" 
                else: move_type = "Loši potezi"
                
                move_description = f"{figure['player']} {figure['row']} {figure['col']} {stack_index} {direction} {current_player}"
                all_moves[move_type].append(move_description)

        return all_moves






#----------------------------------------------------------------------------------------------------------------------------

size = int(input("Unesite dimenziju table (celobrojna vrednost): "))   
game = ByteGame(size)

game.initialize_board()
game.display_board()



for figure in game.bele_figure:
    print(f"Player: {figure['player']}, Height: {figure['height']}, Position: {figure['position']}, Row: {figure['row']}, Col: {figure['col']}")
print()

for figure in game.crne_figure:
    print(f"Player: {figure['player']}, Height: {figure['height']}, Position: {figure['position']}, Row: {figure['row']}, Col: {figure['col']}")
    
print()
game.start_game()




#Ovo je za gledanje dobrih i losih poteza
"""
all_moves = game.generate_all_moves()

print("Loši potezi:")
for move_type, moves in all_moves.items():
    if "Loši potezi" in move_type:
        for i, move in enumerate(moves, 1):
            print(f"{i}. [{move}]")

print("Dobri potezi:")
for move_type, moves in all_moves.items():
    if "Dobri potezi" in move_type:
        for i, move in enumerate(moves, 1):
            print(f"{i}. [{move}]")
"""