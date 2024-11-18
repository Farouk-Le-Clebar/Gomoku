import protocol

def is_position_in_list(position, position_list):
    return position in position_list

def define_best_tale_to_play(board):
    best_empty_positions = []
    max_x = protocol.rows
    max_y = protocol.cols

    for x in range(20):
        for y in range(20):
            if board[x][y] == 1:
                if y + 1 < max_y and board[x][y + 1] == 0 and not is_position_in_list((x, y + 1), best_empty_positions):
                    best_empty_positions.append((x, y + 1))
                if y - 1 >= 0 and board[x][y - 1] == 0 and not is_position_in_list((x, y - 1), best_empty_positions):
                    best_empty_positions.append((x, y - 1))
                if x + 1 < max_x and board[x + 1][y] == 0 and not is_position_in_list((x + 1, y), best_empty_positions):
                    best_empty_positions.append((x + 1, y))
                if x - 1 >= 0 and board[x - 1][y] == 0 and not is_position_in_list((x - 1, y), best_empty_positions):
                    best_empty_positions.append((x - 1, y))
                if x + 1 < max_x and y + 1 < max_y and board[x + 1][y + 1] == 0 and not is_position_in_list((x + 1, y + 1), best_empty_positions):
                    best_empty_positions.append((x + 1, y + 1))
                if x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1] == 0 and not is_position_in_list((x - 1, y - 1), best_empty_positions):
                    best_empty_positions.append((x - 1, y - 1))
                if x + 1 < max_x and y - 1 >= 0 and board[x + 1][y - 1] == 0 and not is_position_in_list((x + 1, y - 1), best_empty_positions):
                    best_empty_positions.append((x + 1, y - 1))
                if x - 1 >= 0 and y + 1 < max_y and board[x - 1][y + 1] == 0 and not is_position_in_list((x - 1, y + 1), best_empty_positions):
                    best_empty_positions.append((x - 1, y + 1))
    return best_empty_positions