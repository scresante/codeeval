import sys, string

def board_generator():
    global board
    board = []
    for i in range(8):
        for n in range(8):
            board.append(string.ascii_lowercase[n] + str(i + 1))
    return(board)

def all_possible_moves(position):
    a = 1
    b = 2
    letpos = string.ascii_lowercase.find(position[0])
    numpos = int(position[1])
    all_possible = []
    all_possible.append(string.ascii_lowercase[letpos - a] + str(numpos + b))
    all_possible.append(string.ascii_lowercase[letpos - a] + str(numpos - b))
    all_possible.append(string.ascii_lowercase[letpos + a] + str(numpos + b))
    all_possible.append(string.ascii_lowercase[letpos + a] + str(numpos - b))
    all_possible.append(string.ascii_lowercase[letpos - b] + str(numpos + a))
    all_possible.append(string.ascii_lowercase[letpos - b] + str(numpos - a))
    all_possible.append(string.ascii_lowercase[letpos + b] + str(numpos + a))
    all_possible.append(string.ascii_lowercase[letpos + b] + str(numpos - a))
    result = []
    for item in all_possible:
        if item in board:
            result.append(item)
    return(' '.join(sorted(result)))

board_generator()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(all_possible_moves(test))
test_cases.close()
