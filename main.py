Estoque = ["pão de forma = sevenboys",
           "pão de forma = visconti",
           "pães artesanais = visconti" ]


def cadastro_de_produto():


    Nova = (input("Qual seria o produto + marca?     ")).lower().strip()


    if Nova in Estoque:


        print("esse produto já está na lista, por favor verificar e ajustar.")
    else:


        Estoque.append(Nova)

def Mostrar_Estoque():


    if len (Estoque) == 0:
        print("ainda Não tem produto")


    else:
        for Produto in Estoque:
         print(Produto)


def Remover_Produto():
    if len(Estoque) == 0:
        print("Ainda não tem produto.")
        return

    for numero, produto in enumerate(Estoque, start=1):
        print(numero, produto)

    escolha = input("Número do produto que deseja remover: ").strip()

    if escolha.isdigit():
        numero = int(escolha)
        if 1 <= numero <= len(Estoque):
            removido = Estoque.pop(numero - 1)
            print("Removido:", removido)
        else:
            print("Esse número não existe na lista.")
    else:
        print("Digite apenas o número.")

def modificar_Produto():
    if len(Estoque) == 0:
        print("Ainda não tem produto.")
        return

    for numero, produto in enumerate(Estoque, start=1):
        print(numero, produto)

    escolha = input("Número do produto que deseja modificar: ").strip()

    if escolha.isdigit():
        numero = int(escolha)
        if 1 <= numero <= len(Estoque):
            posicao = numero - 1
            print("\n1) Remover  2) Modificar")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                removido = Estoque.pop(posicao)
                print("Removido:", removido)
            elif opcao == "2":
                novo_produto = input("Qual será o novo produto? ").lower().strip()
                Estoque[posicao] = novo_produto
                print("Produto modificado!")
            else:
                print("Opção inválida.")
        else:
            print("Esse número não existe na lista.")
    else:
        print("Digite apenas o numero")

def Busca():

    for produto in Estoque:
        print(produto)

    Buscar = input("Qual produto vc estaria buscando?    ").lower().strip()

    if Buscar in Estoque:
        print(Buscar)

    else:
        print("Item n cadastrado")
        sim_ou_nao = input("s/n")

        if sim_ou_nao == "s":
            cadastro_de_produto()

        elif sim_ou_nao == "n":
            print("tenha um bom dia")

        else:
            print("opção invalida")

while True:
    print("\n1) Cadastrar  2) Mostrar  3) Remover  4) Modificar  5) Buscar  6) Sair")
    opcao = input("Escolha: ").strip()

    if opcao == "1":

        cadastro_de_produto()

    elif opcao == "2":

        Mostrar_Estoque()

    elif opcao == "3":

        Remover_Produto()

    elif opcao == "4":

        modificar_Produto()

    elif opcao == "5":

        Busca()

    elif opcao == "6":
        print("Até mais!")
        break
    else:
        print("Opção inválida.")