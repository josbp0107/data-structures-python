from arrays import Array
from matrix import ArrayTwoDimension


def run():
    arreglo = Array(5)

    matriz = ArrayTwoDimension(3,3)

    for i in range(len(arreglo)):
        arreglo[i] = i + 1

    print(arreglo.__len__())

    print(arreglo.__list__())

    print(arreglo.__iter__())

    print(arreglo.__getitem__(4)) # Representacion en memoria

    arreglo.__setitem__(2,200)
    print(arreglo.__list__())

    arreglo.__replace__()
    print(arreglo.__list__())

    print(arreglo.__sumArrays__())


    # Matrices

    print(matriz.__str__())
    matriz = [[row * column for column in range(matriz.get_width())] for row in range(matriz.get_height())]
    # for row in range(matriz.get_height()):
    #     for column in range(matriz.get_width()):
    #         matriz[row][column] = row * column
    print(matriz)

    
if __name__ == '__main__':
    run()