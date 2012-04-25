from paip import othello

def check(move, player, board):
    return othello.is_valid(move) and othello.is_legal(move, player, board)

def human(player, board):
    print othello.print_board(board)
    print 'Your move?'
    while True:
        move = raw_input('> ')
        if move and check(int(move), player, board):
            return int(move)
        elif move:
            print 'Illegal move--try again.'

def get_choice(prompt, options):
    print prompt
    while True:
        choice = raw_input('> ')
        if choice in options:
            return options[choice]
        elif choice:
            print 'Invalid choice.'

def get_players():
    print 'Welcome to OTHELLO!'
    options = {'human': human, 'computer': othello.random_strategy}
    black = get_choice('BLACK: human or computer?', options)
    white = get_choice('WHITE: human or computer?', options)
    return black, white

def main():
    black, white = get_players()
    board, score = othello.play(black, white)
    print 'Final score:', score
    print '%s wins!' % ('Black' if score > 0 else 'White')
    print othello.print_board(board)
