import random

class ByteGame:
    def __init__(self, board_size, player_mode='C'):
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size * 4)] for _ in range(board_size * 4)]
        self.stacks = []  # Dodatni atribut za cuvanje informacija o stekovima
        self.current_player = 'W'  # 'W' za belog igraca, 'B' za crnog igraca
        self.player_mode = player_mode #mod igre  (covek/covek)

    def initialize_board(self):
        # Postavi tablu na početno stanje
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

        # Postavi početne figure
        self.stacks.append({'player': 'B', 'height': 1, 'position': (6, 2)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (6, 10)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (6, 18)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (6, 26)})

        self.stacks.append({'player': 'W', 'height': 1, 'position': (10, 0)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (10, 6)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (10, 14)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (10, 22)})

        self.stacks.append({'player': 'B', 'height': 1, 'position': (14, 2)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (14, 10)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (14, 18)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (14, 26)})

        self.stacks.append({'player': 'W', 'height': 1, 'position': (18, 0)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (18, 6)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (18, 14)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (18, 22)})

        self.stacks.append({'player': 'B', 'height': 1, 'position': (22, 2)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (22, 10)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (22, 18)})
        self.stacks.append({'player': 'B', 'height': 1, 'position': (22, 26)})

        self.stacks.append({'player': 'W', 'height': 1, 'position': (26, 0)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (26, 6)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (26, 14)})
        self.stacks.append({'player': 'W', 'height': 1, 'position': (26, 22)})

        # Dodaj figure na tablu
        for stack in self.stacks:
            player, height, (x, y) = stack['player'], stack['height'], stack['position']
            for h in range(height):
                self.board[x + h][y:y + 3] = f' {player} '

    def choose_first_player(self):
        if self.player_mode == 'H':
            self.current_player = 'W'  # Ako je izabrana opcija za čovek protiv čoveka, beli počinje prvi
            return

        while True:
            choice = input("Ko će igrati prvi? (C - čovek, R - računar): ").upper()
            if choice == 'C':
                self.current_player = 'W'  # Postavljamo da beli igra prvi
                break
            elif choice == 'R':
                self.current_player = 'B'  # Postavljamo da crni igra prvi (za primer)
                break
            else:
                print("Nepoznata opcija. Molimo vas da unesete 'C' ili 'R'.")

    def get_board_size_from_user(self):
        # Unos dimenzije table od strane korisnika
        while True:
            try:
                size = int(input("Unesite dimenziju table (celobrojna vrednost): "))
                if size > 0:
                    self.board_size = size
                    break
                else:
                    print("Dimenzija table mora biti pozitivan ceo broj.")
            except ValueError:
                print("Neispravan unos. Unesite celobrojnu vrednost.")

    def start_game(self):
        self.get_board_size_from_user()
        self.initialize_board()

        player_mode = input("Izaberite način igre (H - čovek protiv čoveka): ").upper()
        self.player_mode = player_mode

        self.choose_first_player()
        self.display_board()

        while not self.is_game_over():
            print(f"\nTrenutni igrač: {self.current_player}")

            if self.player_mode == 'R' and self.current_player == 'B':
                # Ako je na potezu računar, neka izvrši potez
                self.computer_make_move()
            else:
                # Ako je na potezu čovek, neka unese potez
                try:
                    x = int(input("Unesite red (0-31): "))
                    y = int(input("Unesite kolonu (0-31): "))
                    stack_index = int(input("Unesite indeks steka (0-31): "))
                    direction = input("Unesite smer (GL, GD, DL, DD): ")

                    move = ((x, y), stack_index, direction)

                    # Provera ispravnosti poteza i odigravanje poteza
                    if self.is_valid_move(move):
                        self.make_move(move)
                        self.switch_player()
                        self.display_board()
                    else:
                        print("Neispravan potez. Pokušajte ponovo.")

                except ValueError:
                    print("Neispravan unos. Unesite broj.")
                except IndexError:
                    print("Neispravan unos. Indeks steka izvan opsega.")
                except Exception as e:
                    print(f"Greška: {e}")

        print("Kraj igre.")

    def reset_game(self):
        # Vrati figure na početnu poziciju
        self.initialize_board()

    def computer_make_move(self):
        # Provera kraja igre pre nego što računar odabere potez
        if self.is_game_over():
            print("Igra je završena.")
            return

        # Implementacija poteza za računar (primer: slučajno generisan potez)
        moves = self.generate_moves()

        if not moves:
            print("Računar nema validne poteze.")
            return

        move, stack_index = random.choice(moves)
        position, _, _ = move

        # Provera ispravnosti poteza i odigravanje poteza
        self.make_move(move)
        print(f"Računar je odigrao potez: {move}")
        self.display_board()

    def display_board(self):
        j = 0
        print("  ", end=' ')
        for i in range(1, self.board_size + 1):
            print(i, end='   ')
        print()
        for i, row in enumerate(self.board):
            if (i % 4 == 1):
                print(chr(ord('A') + j) + ' ' + ''.join(row))
                j += 1

            else:
                print(' ' + ' ' + ''.join(row))

    def is_game_over(self):
        # Provera kraja igre
        # Igra se završava ako je tabla prazna ili jedan od igrača ima više od polovine stekova
        empty_board = all(all(cell == ' ' for cell in row) for row in self.board)
        majority_stacks_w = sum(1 for stack in self.stacks if stack['player'] == 'W') > len(self.stacks) / 2
        majority_stacks_b = sum(1 for stack in self.stacks if stack['player'] == 'B') > len(self.stacks) / 2

        return empty_board or majority_stacks_w or majority_stacks_b

    def is_valid_move(self, move):
        try:
            (x, y), stack_index, direction = move
        except (TypeError, ValueError) as e:
            print(f"Invalid move: {move}")
            print(f"Error: {e}")
            return False

        # Provera da li zadato polje postoji na tabli
        if not (0 <= x < len(self.board)) or not (0 <= y < len(self.board[0])):
            print("Neispravan potez. Polje ne postoji na tabli.")
            return False

        # Ispisivanje informacija radi lakšeg praćenja
        print(f"Board dimensions: {len(self.board)} x {len(self.board[0])}")
        print(f"Position: ({x}, {y})")

        # Provera da li postoje figure na zadatom polju
        if any(f' {player} ' in [self.board[i][j] for i in range(x, x + 3) for j in range(y, y + 3)] for player in
               ['W', 'B']):
            # Proveravamo da li polje sadrži belu ili crnu figuru
            print("Neispravan potez. Polje nije prazno.")
            return False

        # Provera da li postoji figura na zadatom mestu na steku na zadatom polju
        if f' {self.current_player} ' not in [self.board[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]:
            print("Neispravan potez. Nema odabrane figure na zadatom mestu.")
            return False

        # Provera da li je smer jedan od četiri moguća
        if direction not in ['GL', 'GD', 'DL', 'DD']:
            print("Neispravan potez. Nije izabran ispravan smer.")
            return False

        # Provera da li je stek prazan
        if stack_index < 0 or stack_index >= len(self.stacks):
            print("Neispravan potez. Indeks steka izvan opsega.")
            return False

        # Provera da li je potez u okviru visine steka
        if self.stacks[stack_index]['height'] == 0:
            print("Neispravan potez. Stek je prazan.")
            return False

        # Ako sve provere prođu, potez je ispravan
        return True

    def make_move(self, move):
        position, stack_index, direction = move
        x, y = position

        # Provera ispravnosti unetog poteza
        if not self.is_valid_move(move):
            return

        # Izmena tabele prema izabranom potezu
        self.board[x][y:y + 3] = '   '  # Uklanjanje figure sa starog mesta

        # Ažuriranje pozicije figure na steku
        self.stacks[stack_index]['position'] = (x, y)

        # Postavljanje figure na novo mesto
        self.board[x][y:y + 3] = f' {self.current_player} '

    def apply_move(self, move):
        position, stack_index, direction = move
        x, y = position

        # Kopiranje trenutnog stanja igre
        new_board = [row[:] for row in self.board]
        new_stacks = [{'player': stack['player'], 'height': stack['height'], 'position': stack['position']} for stack in
                      self.stacks]

        # Provera ispravnosti poteza
        if not self.is_valid_move(move):
            raise ValueError("Neispravan potez.")

        # Izmena tabele prema izabranom potezu
        new_board[x][y:y + 3] = '   '  # Uklanjanje figure sa starog mesta

        # Ažuriranje pozicije figure na steku
        new_stacks[stack_index]['position'] = (x, y)

        # Postavljanje figure na novo mesto
        new_board[x][y:y + 3] = f' {self.current_player} '

        return new_board, new_stacks

    def generate_moves(self):
        valid_moves = []

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                for direction in ['GL', 'GD', 'DL', 'DD']:
                    for stack_index in range(len(self.stacks)):
                        move = ((i, j), stack_index, direction)
                        #is_valid = self.is_valid_move(move)
                        is_valid, processed_move = self.is_valid_move(move)
                        if is_valid:
                            valid_moves.append(move)

        return valid_moves

    def switch_player(self):
        # Implementirajte funkciju za promenu igrača
        self.current_player = 'B' if self.current_player == 'W' else 'W'

    def are_neighbors_empty(self, x, y):
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < len(self.board) and 0 <= j < len(self.board[0]) and self.board[i][j] != ' ':
                    return False
        return True

    def is_valid_stack_move(self, x, y, direction):
        # Provera da li polje postoji na tabli
        if not (0 <= x < len(self.board)) or not (0 <= y < len(self.board[0])):
            return False

        # Provera da li su susedna polja prazna
        if direction == 'GL' and (x - 1 < 0 or self.board[x - 1][y] != '   '):
            return False
        elif direction == 'GD' and (x + 1 >= len(self.board) or self.board[x + 1][y] != '   '):
            return False
        elif direction == 'DL' and (y - 1 < 0 or self.board[x][y - 1] != '   '):
            return False
        elif direction == 'DD' and (y + 1 >= len(self.board[0]) or self.board[x][y + 1] != '   '):
            return False

        return True

# Primer upotrebe
game = ByteGame(8)
game.start_game()