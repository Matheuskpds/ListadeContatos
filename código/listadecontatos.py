contatos = [[0 for c in range(2)]for i in range(1000)]

def menu():
    print()
    print("\033[1;31;40m---------- MENU ----------\033[m")
    print("[1] adicionar novo contato")
    print("[2] ver lista de contatos")
    print("[3] pesquisar na lista de contatos")
    print("[4] para excluir um contato")
    print("[5] encerrar programa")
    print("\033[1;31;40m--------------------------\033[m")
    print()

cont = 0
while True:
    menu()
    resp = int(input())
    if resp == 5:
        break
    elif resp == 1:
        while True:
            resp2 = input("Adicionar novo contato? [S/N]").upper()
            if resp2 == 'N':
                break
            elif resp2 == 'S':
                print()
                contatos[cont][0] = input("Digite o nome do contato: ")
                contatos[cont][1] = int(input("Número: "))
                cont += 1
                print()
    elif resp == 2:
        print()
        for i in range(cont):
            for j in range(2):
                if contatos[i][j] != 0:
                    if j == 1:
                        print(contatos[i][j])
                    else:
                        print(contatos[i][j], ':',end=' ')
    elif resp == 3:
        while True:
            cont2 = 0
            print()
            pesquisa = str(input("Digite o nome do contato: "))
            for j in range(cont):
                if contatos[j][0] == pesquisa:
                    print("Contato encontrado: ")
                    print(contatos[j][0], ':', contatos[j][1])
                    cont2 += 1
                    break
            if cont2 == 0:
                print()
                print("Contato não encontrado")
            else:
                break
    elif resp == 4:
        resp4 = input("Qual contato deseja excluir? ")
        for c in range(cont):
            if contatos[c][0] == resp4:
                print("Contato encontrado:")
                print(contatos[c][0], ":", contatos[c][1])
                resp4 = input("Deseja mesmo excluir? [S/N]").upper()
                if resp4 == 'S':
                    del contatos[c]
                else:
                    break
             