from arrays import Array


def run():
    arreglo = Array(5)
    
    for i in range(len(arreglo)):
        arreglo[i] = i + 1

    print(arreglo.__len__())

    print(arreglo.__list__())

    print(arreglo.__iter__())

    print(arreglo.__getitem__(4))

    arreglo.__setitem__(2,200)
    print(arreglo.__list__())

    arreglo.__replace__()
    print(arreglo.__list__())

    print(arreglo.__sumArrays__())

if __name__ == '__main__':
    run()