from produtos import produtos

def cadastrar_sessao(codigo):
    if codigo in produtos:
        sessao = input("Informe a sessão (ex: bebidas, limpeza): ")
        produtos[codigo]['sessao'] = sessao
        print("Sessão cadastrada.")
    else:
        print("Produto não encontrado.")
