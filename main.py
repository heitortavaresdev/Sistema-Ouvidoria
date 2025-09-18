# ============================================================
# Sistema de Ouvidoria + BD MySQL - Heitor Queiroga Tavares
# ============================================================

from operacoesbd import *
from metodos import *

#Conexao com o BD
connection = criarConexao('localhost', 'root', 'Nobu2016.', 'ouvidoria')

#Menu
while True:
        print("\n===== MENU OUVIDORIA =====")
        print("1 - Listar manifestações")
        print("2 - Registrar nova manifestação")
        print("3 - Pesquisar manifestação por ID")
        print("4 - Pesquisar manifestações por tipo")
        print("5 - Atualizar uma manifestação")
        print("6 - Excluir uma manifestação")
        print("7 - Sair")

        try:
            option = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 7.")
            continue

#Listar manifestações
        if option == 1:
            listarManifestacoes(connection)

#Registrar manifestação
        elif option == 2:
            registrarManifestacoes(connection)

#Pesquisar por ID
        elif option == 3:
            pesquisarPorID(connection)

#Pesquisar por tipo
        elif option == 4:
            pesquisarPorTipo(connection)

#Atualizar alguma manifestação
        elif option == 5:
            atualizarManifestacao(connection)

#Exluir alguma manifestação
        elif option == 6:
            excluirManifestacao(connection)

#Sair do sistema
        elif option == 7:
            print("\nObrigado por utilizar! Saindo do sistema...")
            break

        else:
            print("Opção inválida. Escolha entre 1 e 7.")

#Encerra conexao com o BD
encerrarConexao(connection)