from random import randint
def infomaçao():
    print("""[ 1 ] Escolher um número
[ 2 ] Tabuada do 1 a 10
[ 3 ] A tubada de um número aleatorio""")



while True:
    infomaçao()
    try:
        opc = int(input("Opção: "))
    except:
        print("opção invalida!")
    else:
        if opc == 1:
            n = int(input("Número: "))
            for c in range(1, 11):
                print(f'{c} x {n} = {c*n}')
        elif opc == 2:
            for c in range(1, 11):
                for i in range(1, 11):
                    print(f'{c} x {i} = {c*i}')
                print()
        elif opc == 3:
            n = randint(1, 10)
            for c in range(1, 11):
                print(f'{c} x {n} = {c*n}')
        else:
            break