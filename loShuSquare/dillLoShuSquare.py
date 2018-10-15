# Hello World program in Python

def main():
    print(isLoShuSquare(createSquare()))


def isLoShuSquare(square):
    for col in range(0, len(square) - 1):
        rowSum = 0
        colSum = 0
        diagonalSum = 0
        rDiagonalSum = 0

        for row in range(0, len(square[col])):
            rowSum += square[col][row] #checks row sum
            colSum += square[row][col] #checks col sum
            diagonalSum += square[row][row] #checks diagonal sum
            rDiagonalSum += square[len(square) - 1 - row][len(square) - 1 - row] #checks diagonal from top right to bottom left

        if rowSum != colSum or colSum != diagonalSum or diagonalSum != rDiagonalSum:
            return False

    return True


def createSquare():
    square = []
    size = (int(input("Enter array size: ")))
    for row in range(0,size):
        square.append([])
        for col in range(0,size):
            square[row].append(int(input("Enter element at ("+(str(row))+","+(str(col))+"): ")))
        print()
    return square


main()

