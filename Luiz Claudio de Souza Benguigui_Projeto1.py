import json
import os.path
import sys

def obter_dados():
    
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    OPÇÃO 1 do MENU 
    '''
    ...
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    ...
    lista_categorias = []

    for produto in dados:

        categoria_lida = produto["categoria"]

        if categoria_lida not in lista_categorias:
            lista_categorias.append(categoria_lida)
    
    return sorted(lista_categorias)
    
def listar_por_categoria(dados, categoria):
    '''
    OPÇÃO 2 do MENU 
    '''
    ...
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    ...

    lista_por_categoria = []

    for produto in dados:

        if produto["categoria"] == categoria:
            lista_por_categoria.append(produto)

    return lista_por_categoria

def produto_mais_caro(dados, categoria):
    '''
    OPÇÃO 3 do MENU 
    '''
    ...
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    
    nova_lista = listar_por_categoria(dados, categoria)
    nova_lista.sort(key= lambda precos: float(precos["preco"]), reverse=True)
    
    # Retorna o dicionário do produto na posição inicial 
    # da lista de dicionários ordenada de forma DECRESCENTE
    return nova_lista[0]


def produto_mais_barato(dados, categoria):
    '''
    OPÇÃO 4 do MENU 
    '''
    ...
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    ...
    nova_lista = listar_por_categoria(dados, categoria)
    nova_lista.sort(key= lambda precos: float(precos["preco"]))
    
    # Retorna o dicionário do produto na posição inicial 
    # da lista de dicionários ordenada de forma CRESCENTE
    return nova_lista[0]

    
def top_10_caros(dados):
    '''
    OPÇÃO 5 do MENU 
    '''
    ...
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    ...

    dados.sort(key= lambda precos: float(precos["preco"]), reverse=True)
    
    # Retorna a lista com 10 primeiros dicionários dos produtos 
    # da lista de dicionários ordenada de forma CRESCENTE
    return dados[:10]

def top_10_baratos(dados):
    '''
    OPÇÃO 6 do MENU 
    '''
    ...
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    ...

    dados.sort(key= lambda precos: float(precos["preco"]))

    # Retorna a lista com 10 primeiros dicionários dos produtos 
    # da lista de dicionários ordenada de forma DECRESCENTE
    return dados[:10]

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    ...
    # Exibe as opções do Menu e solicitar a seleção do usuário:
    exibe_menu()
    opcao = obtem_selecao()
    
    # Executa a função referente à seleção do usuário
    while opcao != 0:

        if opcao == 1:
            lista_categorias = listar_categorias(dados)
            imprime_categorias(lista_categorias, f"Lista das {len(lista_categorias)} Categorias")

        elif opcao == 2:
            encontrada, categoria_digitada = obtem_categoria(dados)
            if encontrada:
                lista_por_categoria = listar_por_categoria(dados,categoria_digitada)
                imprime_lista(lista_por_categoria, "Lista de " + str(len(lista_por_categoria)) + " Produtos da Categoria " + categoria_digitada)

        elif opcao == 3:
            encontrada, categoria_digitada = obtem_categoria(dados)
            if encontrada:
                imprime_dict(produto_mais_caro(dados,categoria_digitada),'Produto mais caro da Categoria ' + categoria_digitada)

        elif opcao == 4:
            encontrada, categoria_digitada = obtem_categoria(dados)
            if encontrada:
                imprime_dict(produto_mais_barato(d,categoria_digitada),'Produto mais barato da Categoria ' + categoria_digitada)

        elif opcao == 5:
            imprime_lista(top_10_caros(dados),'Lista dos 10 Produtos mais caros')
        
        elif opcao == 6:
            imprime_lista(top_10_baratos(dados),'Lista dos 10 Produtos mais baratos')

        exibe_menu()
        opcao = obtem_selecao()
            
    print("\n")
    print("Obrigado por utilizar nosso sistema!")

def exibe_menu():

    # Exibe as opções de Menu
    print("\n1. Listar categorias")
    print("2. Listar produtos de uma categoria")
    print("3. Produto mais caro por categoria")
    print("4. Produto mais barato por categoria")
    print("5. Top 10 produtos mais caros")
    print("6. Top 10 produtos mais baratos")
    print("0. Sair\n")

def obtem_selecao():
    
    '''
    Essa função solicita ao usuário que informe uma opção do Menu
    Até que o mesmo selecione uma opção válida
    Retorna as opção válida selecionada
    '''
    ...
    selecao = input("Digite sua opção: ")
    while selecao.isdigit() == False or (int(selecao) >=0 and int(selecao) <=6) == False:
        print("\n")
        print(f"OPÇÃO '{selecao}' INVÁLIDA!\n")
        selecao = input("Digite sua opção: ")

    return int(selecao)
    
    
def obtem_categoria(dados):

    '''
    O parâmetro "dados" é a lista de dicionários representando os produtos.
    Essa função solicita ao usuário que informe uma categoria
    Valida se a categoria existe. Permite digitar '0' para retornar
    Retorna :se a categoria é válida e a categoria válida digitada
    '''
    ...

    categoria_encontrada = True
    categoria_digitada = input("Digite a categoria ou ´0´ para retornar: ")
    lista_categorias = listar_categorias(dados)

    while categoria_digitada not in lista_categorias:
        categoria_encontrada = False
        if categoria_digitada == '0':
            break
        else:
            print("\n")
            categoria_encontrada = True
            print(f"CATEGORIA '{categoria_digitada}' INVÁLIDA!\n")
            categoria_digitada = input("Digite a categoria ou ´0´ para sair: ")
            lista_categorias = listar_categorias(dados)
    
    return categoria_encontrada, categoria_digitada

def imprime_categorias(lista_a_imprimir, titulo = ""):

    # Imprime a lista de categorias recebida 
    if titulo != "":
        print(f"\n{titulo}")
 
    for elemento in lista_a_imprimir:
        print(f'{elemento}')

def imprime_lista(lista_a_imprimir, titulo = ""):

    # Imprime a lista informada de dicionários de produtos 
    if titulo != "":
        print(f"\n{titulo}")
    print("{:<40} {:<10} {:<15}".format("Identificador", "Preço", "Categoria"))
    for dado in lista_a_imprimir:
        imprime_dict(dado, titulo = "")

def imprime_dict(dict_a_imprimir, titulo = ""):

    # Imprime o dicionário do produto informado
    if titulo != "":
        print(f"\n{titulo}")
        print("{:<40} {:<10} {:<15}".format("Identificador", "Preço", "Categoria"))
    print("{:<40}".format(dict_a_imprimir['id']), "{:<10}".format(dict_a_imprimir['preco']), "{:<15}".format(dict_a_imprimir['categoria']))
        
d = obter_dados()
menu(d)