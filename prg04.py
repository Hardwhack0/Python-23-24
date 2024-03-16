for row in range(8):
    for col in range(8):
        # Zjištění, zda je součet řádku a sloupce sudý nebo lichý
        if (row + col) % 2 == 0:
            print('0', end=' ')
        else:
            print('1', end=' ')
    print()