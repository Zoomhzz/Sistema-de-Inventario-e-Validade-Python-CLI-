from random import randint

produtos = {}

def cadastro_produto():
    codigo = randint(1000, 9999)
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço: "))
    quantidade = int(input("Informe a quantidade: "))
    produtos[codigo] = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
    print(f"Produto cadastrado! Código: {codigo}")
    return codigo

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for codigo, p in produtos.items():
        print(f"Código: {codigo} | Nome: {p['nome']} | Preço: {p['preco']} | Quantidade: {p['quantidade']} | "
              f"Sessão: {p.get('sessao', 'N/A')} | Validade: {p.get('dataValidade', 'N/A')}")

def pesquisar_produto():
    codigo = int(input("Informe o código de barras: "))
    if codigo in produtos:
        print(produtos[codigo])
    else:
        print("Produto não encontrado.")

def atualizar_produto():
    codigo = int(input("Informe o código de barras: "))
    if codigo in produtos:
        nome = input("Novo nome: ")
        preco = float(input("Novo preço: "))
        quantidade = int(input("Nova quantidade: "))
        produtos[codigo].update({'nome': nome, 'preco': preco, 'quantidade': quantidade})
        print("Produto atualizado.")
    else:
        print("Produto não encontrado.")
