# PROJETO FINAL - PYTHON

# Nome do programa
print("\nLIVRARIA DIGITAL - O ÚNICO DESTINO DOS VILÕES É A MORTE")
print()

# Introdução
print("Bem-vindo(a) à nossa livraria digital dedicada a 'O único Destino dos Vilões é a Morte', onde você pode adquirir todos os volumes disponíveis dessa obra repleta de drama, fantasia e reviravoltas.")
print()

# Sinopse
print("Sinopse:")
print()
print("Cha Siyeon se vê presa em um jogo de simulação de namoro — no modo difícil. Em vez de jogar como a adorada heroína, ela está presa no papel da vilã, Penelope Eckhart, onde todos os finais possíveis levam à sua morte.\nPara sobreviver, ela deve usar seu conhecimento interno do jogo para navegar pelo mundo perigoso, conquistar a afeição dos personagens masculinos e evitar as inúmeras maneiras de encontrar um fim trágico.")
print()

# Dicionário com os volumes e seus respectivos preços
volumes = {
    1: 98.32,
    2: 79.90,
    3: 82.18,
    4: 69.90,
    5: 98.37,
    6: 89.93,
    7: 102.10
    }

# Exibe lista de volumes e seus preços formatados
print("--------------------------------------------------------")
print()
print("LISTA DE VOLUMES E PREÇOS:")
print()
for num, preco in volumes.items():
    print(f"Volume {num} - R$ {preco:.2f}")
print()
print("--------------------------------------------------------")
print()

# Inicializa o carrinho de compras
carrinho = []

# Loop para adicionar volumes ao carrinho
while True:
    try:
        produto = input("Digite o número do volume que deseja comprar (ou 'fim' para encerrar): ")
        if produto.lower() == "fim":
            break
        volume = int(produto)
        if volume in volumes:
            carrinho.append((volume, volumes[volume]))
            print(f"Volume {volume} adicionado ao carrinho.")
        else:
            print("Volume inexistente. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

# Verifica se o carrinho está vazio e exibe a mensagem de encerramento ou o resumo da compra
if not carrinho:
    print("Nenhum volume foi comprado. Obrigado pela visita!")
else:
    print()
    print("--------------------------------------------------------")
    print("                  RESUMO DA COMPRA                      ")
    print()
    for vol, preco in carrinho:
        print(f"Volume {vol} - R$ {preco:.2f}")

    preco_total = sum(preco for _, preco in carrinho)
    print()
    print("--------------------------------------------------------")
    print(f"TOTAL A PAGAR:                     R$ {preco_total:.2f}")
    print("--------------------------------------------------------")
    print()
    print()

    # Menu de forma de pagamento
    print("--------------------------------------------------------")
    print("                  Efetuar Pagamento                     ")
    print("--------------------------------------------------------")
    print()
    print("Selecione uma forma de pagamento:")
    print()
    print("1. Cartão de débito")
    print("2. Cartão de crédito")
    print("3. Boleto")
    print("4. Pix")
    print()
    print("--------------------------------------------------------")
    print()
    
    # Seleciona forma de pagamento
    opcao = input("Digite o número da opção de pagamento: ")
    
    if opcao == "1":
        print("Pagamento via cartão de débito selecionado.")
    elif opcao == "2":
        print("Pagamento via cartão de crédito selecionado.")
    elif opcao == "3":
        print("Pagamento via boleto selecionado.")
    elif opcao == "4":
        print("Pagamento via pix selecionado.")
    else:
        print("Opção inválida. Pagamento em dinheiro na entrega.")
        
    # Recebe o pagamento e calcula o troco
    while True:
        try:
            pagamento = float(input("\nDigite o valor pago: R$ "))
            if pagamento < preco_total:
                print("Valor insuficiente. Tente novamente.")
            else:
                troco = pagamento - preco_total
                print(f"TROCO:               R$ {troco:.2f}")
                break
        except ValueError:
            print("Por favor, digite um valor válido.")
            
    # Mensagem final
    print("\nObrigado por comprar com a gente. Volte sempre e aproveite a leitura!")