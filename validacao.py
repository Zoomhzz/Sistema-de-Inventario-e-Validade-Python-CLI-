from random import randint
from produtos import produtos

def data_de_validade():
    codigo = int(input("Informe o código de barras: "))
    if codigo in produtos:
        dia = randint(1, 31)
        mes = randint(1, 12)
        ano = randint(2023, 2025)
        validade = f"{dia:02d}/{mes:02d}/{ano}"
        produtos[codigo]['dataValidade'] = validade
        print("Validade registrada.")
    else:
        print("Produto não encontrado.")

def sistema_checagem_descarte():
    codigo = int(input("Informe o código de barras: "))
    if codigo in produtos:
        validade = produtos[codigo].get('dataValidade')
        if validade:
            print(f"Validade: {validade}")
            if validade < "01/01/2024":
                print("Produto vencido. Descartar.")
            else:
                print("Produto válido.")
        else:
            print("Validade não registrada.")
    else:
        print("Produto não encontrado.")
