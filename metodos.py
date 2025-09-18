from operacoesbd import *

#Escolher tipo
types = { "1": "Reclamação", "2": "Sugestão", "3": "Elogio" }

def chooseType(types):
    while True:
        print("Escolha o tipo da manifestação:")
        print("1 - Reclamação")
        print("2 - Sugestão")
        print("3 - Elogio")
        option = input("Digite 1, 2 ou 3: ")
        if option in types:
            return types[option]
        else:
            print("Opção inválida. Tente novamente.")

#Listar
def listarManifestacoes(connection):
    sql = "SELECT * FROM manifestacoes"
    results = listarBancoDados(connection, sql)
    if results:
        for item in results:
            print(
                f"ID: {item[0]}, Tipo: {item[1]}, Título: {item[2]}, Descrição: {item[3]}, Autor: {item[4]}, Respondente: {item[5]}")
        print(f"\nTotal de manifestações: {len(results)}")
    else:
        print("Nenhuma manifestação cadastrada.")

#Nova manifestação
def registrarManifestacoes(connection):
    type_ = chooseType(types)
    title = input("Digite o titulo: ")
    description = input("Digite a descrição da manifestação: ")
    author = input("Digite o autor: ")
    respondent = input("Digite o respondente: ")
    sql = "INSERT INTO manifestacoes (tipo, titulo, descricao, autor, respondente) VALUES (%s, %s, %s, %s, %s)"
    data = (type_, title, description, author, respondent)
    new_id = insertNoBancoDados(connection, sql, data)
    if new_id:
        print(f"Manifestação registrada com sucesso! ID: {new_id}")

#Pesquisar por ID
def pesquisarPorID(connection):
    id_search = input("Digite o ID da manifestação: ")
    sql = "SELECT * FROM manifestacoes WHERE id = %s"
    results = listarBancoDados(connection, sql, (id_search,))
    if results:
        for item in results:
            print(
                f"ID: {item[0]}, Tipo: {item[1]}, Título: {item[2]}, Descrição: {item[3]}, Autor: {item[4]}, Respondente: {item[5]}")
    else:
        print("Nenhuma manifestação encontrada com esse ID.")

#Pesquisar por tipo
def pesquisarPorTipo(connection):
    type_search = chooseType(types)
    sql = "SELECT * FROM manifestacoes WHERE tipo = %s"
    results = listarBancoDados(connection, sql, (type_search,))
    if results:
        for item in results:
            print(
                f"ID: {item[0]}, Tipo: {item[1]}, Título: {item[2]}, Descrição: {item[3]}, Autor: {item[4]}, Respondente: {item[5]}")
        print(f"\nTotal de manifestações: {len(results)}")
    else:
        print("Nenhuma manifestação encontrada com esse tipo.")

#Atualizar manifestação
def atualizarManifestacao(connection):
    id_update = input("Digite o ID da manifestação que deseja atualizar: ")
    type_update = chooseType(types)
    title_update = input("Digite o novo titulo: ")
    description_update = input("Digite a nova descrição: ")
    author_update = input("Digite o novo autor: ")
    respondent_update = input("Digite o novo respondente: ")
    sql = "UPDATE manifestacoes SET tipo = %s, titulo = %s, descricao = %s, autor = %s, respondente = %s WHERE id = %s"
    changes = atualizarBancoDados(connection, sql,
                                  (type_update, title_update, description_update, author_update, respondent_update,
                                   id_update))
    if changes > 0:
        print("Manifestação atualizada com sucesso.")
    else:
        print("Nenhuma manifestação encontrada com esse ID.")

#Excluir manifestação
def excluirManifestacao(connection):
    id_delete = input("Digite o ID da manifestação que deseja excluir: ")
    sql = "DELETE FROM manifestacoes WHERE id = %s"
    changes = excluirBancoDados(connection, sql, (id_delete,))
    if changes > 0:
        print("Manifestação excluída com sucesso.")
    else:
        print("Nenhuma manifestação encontrada com esse ID.")