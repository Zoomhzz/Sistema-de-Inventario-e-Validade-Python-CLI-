from produtos import cadastro_produto, listar_produtos, pesquisar_produto, atualizar_produto
from sessão import cadastrar_sessao
from venda import vender_produto
from validacao import data_de_validade, sistema_checagem_descarte

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Cadastrar produto")
        print("2. Cadastrar sessão")
        print("3. Listar produtos")
        print("4. Pesquisar produto")
        print("5. Atualizar produto")
        print("6. Cadastrar validade")
        print("7. Verificar validade")
        print("8. Realizar venda")
        print("9. Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            codigo = cadastro_produto()
        elif opcao == "2":
            codigo = int(input("Código do produto: "))
            cadastrar_sessao(codigo)
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            pesquisar_produto()
        elif opcao == "5":
            atualizar_produto()
        elif opcao == "6":
            data_de_validade()
        elif opcao == "7":
            sistema_checagem_descarte()
        elif opcao == "8":
            vender_produto()
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
