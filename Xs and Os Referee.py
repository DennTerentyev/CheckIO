def checkio(game_result):
    g="".join(game_result)
    
    wins=( (0,3,6), #Left column
           (1,4,7), #Middle column
           (2,5,8), #Right column
           (0,1,2), #Top row
           (3,4,5), #Middle row
           (6,7,8), #Bottom row
           (0,4,8), #Left-hand diagonal
           (2,4,6) )#Right-hand diagonal
    
    for a,b,c in wins:
        if (g[a] in "XO") and ( g[a]==g[b]==g[c] ):
            return g[a]
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")



def checkio(game_result):
    field = game_result
    #horizontal
    for row in field:
        if row[0] == row[1] == row[2] and row[0] != ".":
            if row[0] == "X":
                return "X"
            elif row[0] == "O":
                return "O"
    #vertical
    rotated = zip(*field)
    for row in rotated:
        if row[0] == row[1] == row[2] and row[0] != ".":
            if row[0] == "X":
                return "X"
            elif row[0] == "O":
                return "O"
    #diagonal
    if field[0][0] == field[1][1] == field[2][2] and field[0][0] != ".":
        if field[0][0] == "X":
            return "X"
        elif field[0][0] == "O":
            return "O"
    if field[0][2] == field[1][1] == field[2][0] and field[0][2] != ".":
        if field[0][2] == "X":
            return "X"
        elif field[0][2] == "O":
            return "O"
    
    
    
    
    return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")]




    def checkio(game_result):
    
    #horizontal
    for row in game_result:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 'X'
            if row[0] == 'O':
                return 'O'
    
    #vertical
    rotatedboard = list(zip(*game_result))
    for row in rotatedboard:
        if row[0] == row[1] == row[2]:
            if row[0] == 'X':
                return 'X'
            if row[0] == 'O':
                return 'O'
                
                
    #diagonal check
    if game_result[0][0] == game_result[1][1] == game_result[2][2]:
        if game_result[0][0] == 'X':
            return 'X'
        if game_result[0][0] == 'O':
            return 'O'
    #other diagonal check
    rotated = list(zip(*game_result))
    if rotated[0][2] == rotated[1][1] == rotated[2][0]:
        if rotated[1][1] == 'X':
            return 'X'
        if rotated[1][1] == 'O':
            return 'O'

    #draw check
    boardSpots = 0
    boardx = 0
    boardo = 0
    for row in range(3):
        for column in range(3):
            if game_result[row][column] != '.':
                boardSpots += 1
            elif game_result[row][column] == 'X':
                boardx += 1
            elif game_result[row][column] == 'O':
                boardo += 1
    if boardSpots == 9 or boardx == boardo:
        return 'D'                
    
    
            
     

    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
