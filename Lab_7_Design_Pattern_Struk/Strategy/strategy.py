from piece import Knight,Bishop
from move_rules import KnightMove,BishopMove
import os









if __name__ == '__main__':
    knight_move = KnightMove(position=[(1, 0)])
    knight = Knight(knight_move.position, 'White', knight_move)
    bishop_move = BishopMove(position=[(2, 7)])
    bishop = Bishop(bishop_move.position, 'Black', bishop_move)

    os.system('CLS')
    choice = str(input("You want to start?\nYes or No: "))
    if choice.lower() == 'yes':
        os.system('CLS')
        knight.print_info()
        bishop.print_info()
        print('-----------------------------------------------------------------------')
        print('\n\nWhite turn\n\n')

        print(f"\nAvailable moves: {knight_move.get_all_moves()}")
        coord_knight = input('Enter x and y: ').split()
        print(knight.move([(int(coord_knight[0]), int(coord_knight[1]))]))

        print("\n\nBlack turn\n\n")

        print(f"\nAvailable moves: {bishop_move.get_all_moves()}")
        coord_bishop = input('Enter x and y: ').split()
        print(bishop.move([(int(coord_bishop[0]), int(coord_bishop[1]))]))

        print('\nGame Over, see you next time\n\n')