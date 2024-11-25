import mysql.connector

# Conexão com o banco de dados do Zoológico
conexao_banco = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="zoologico"
)
cursor = conexao_banco.cursor()

# Função para cadastrar novos registros no zoológico
def cadastrar():
    print("1- Cadastrar Animal")
    print("2- Cadastrar Funcionário")
    print("3- Cadastrar Habitat")
    print("4- Cadastrar Ingresso")
    print("5- Cadastrar Loja")
    print("6- Cadastrar Visitante")
    opcao = int(input("Escolha a opção de cadastro: "))

    if opcao == 1:
        nome = input("Nome do Animal: ")
        especie = input("Espécie: ")
        genero = input("Gênero: ")
        datanasc = input("Data de Nascimento ( Dia-Mês-Ano ): ")
        datachegada = input("Data de Chegada ( Dia-Mês-Ano ): ")
        origem = input("Origem: ")
        saude = input("Condição de Saúde: ")
        alimentacao = input("Tipo de Alimentação: ")
        idhabitat = int(input("ID do Habitat: "))
        comando_sql = f'''INSERT INTO animais (Nome, Especie, Genero, Datanasc, Datachegada, Origem, Saúde, Alimentacao, Idhabitat) 
                          VALUES ("{nome}", "{especie}", "{genero}", "{datanasc}", "{datachegada}", "{origem}", "{saude}", "{alimentacao}", {idhabitat})'''
    elif opcao == 2:
        nome = input("Nome do Funcionário: ")
        cargo = input("Cargo: ")
        datacontratacao = input("Data de Contratação ( Dia-Mês-Ano ): ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        comando_sql = f'''INSERT INTO funcionarios (Nome, Cargo, Datacontratacao, Email, Telefone) 
                          VALUES ("{nome}", "{cargo}", "{datacontratacao}", "{email}", {telefone})'''
    elif opcao == 3:
        tipo = input("Tipo de Habitat: ")
        tamanho = input("Tamanho: ")
        clima = input("Clima: ")
        comando_sql = f'INSERT INTO habitat (Tipo, Tamanho, Clima) VALUES ("{tipo}", "{tamanho}", "{clima}")'
    elif opcao == 4:
        tipo = input("Tipo de Ingresso: ")
        preco = float(input("Preço: "))
        datavalidade = input("Data de Validade ( Dia-Mês-Ano ): ")
        quantidade = int(input("Quantidade: "))
        desconto = int(input("Desconto: "))
        comando_sql = f'''INSERT INTO ingressos (Tipo, Preco, Datavalidade, Quantidade, Desconto) 
                          VALUES ("{tipo}", {preco}, "{datavalidade}", {quantidade}, {desconto})'''
    elif opcao == 5:
        nome = input("Nome da Loja: ")
        servico = input("Serviço oferecido: ")
        horario = int(input("Horário de funcionamento: "))
        comando_sql = f'INSERT INTO lojas (Nome, Servico, Horario) VALUES ("{nome}", "{servico}", {horario})'
    elif opcao == 6:
        nome = input("Nome do Visitante: ")
        datavisita = input("Data da Visita ( Dia-Mês-Ano): ")
        idingresso = int(input("ID do Ingresso: "))
        receita = float(input("Receita: "))
        email = input("Email: ")
        telefone = int(input("Telefone: "))
        comando_sql = f'''INSERT INTO visitantes (Nome, Datavisita, Idingresso, Receita, Email, Telefone) 
                          VALUES ("{nome}", "{datavisita}", {idingresso}, {receita}, "{email}", {telefone})'''
    else:
        print("Opção inválida.")
        return

    cursor.execute(comando_sql)
    conexao_banco.commit()
    print("Cadastro realizado com sucesso!")

# Função para alterar registros
def alterar():
    print("1- Alterar Animal")
    print("2- Alterar Funcionário")
    print("3- Alterar Habitat")
    print("4- Alterar Ingresso")
    print("5- Alterar Loja")
    print("6- Alterar Visitante")
    opcao = int(input("Escolha a opção de alteração: "))

    if opcao == 1:
        id_animal = int(input("ID do Animal: "))
        nova_saude = input("Nova Condição de Saúde: ")
        comando_sql = f'UPDATE animais SET Saúde = "{nova_saude}" WHERE Id = {id_animal}'
    elif opcao == 2:
        id_funcionario = int(input("ID do Funcionário: "))
        novo_cargo = input("Novo Cargo: ")
        comando_sql = f'UPDATE funcionarios SET Cargo = "{novo_cargo}" WHERE Id = {id_funcionario}'
    elif opcao == 3:
        id_habitat = int(input("ID do Habitat: "))
        novo_clima = input("Novo Clima: ")
        comando_sql = f'UPDATE habitat SET Clima = "{novo_clima}" WHERE Id = {id_habitat}'
    elif opcao == 4:
        id_ingresso = int(input("ID do Ingresso: "))
        novo_preco = float(input("Novo Preço: "))
        comando_sql = f'UPDATE ingressos SET Preco = {novo_preco} WHERE Id = {id_ingresso}'
    elif opcao == 5:
        id_loja = int(input("ID da Loja: "))
        novo_servico = input("Novo Serviço oferecido: ")
        comando_sql = f'UPDATE lojas SET Servico = "{novo_servico}" WHERE Id = {id_loja}'
    elif opcao == 6:
        id_visitante = int(input("ID do Visitante: "))
        nova_receita = float(input("Nova Receita: "))
        comando_sql = f'UPDATE visitantes SET Receita = {nova_receita} WHERE Id = {id_visitante}'
    else:
        print("Opção inválida.")
        return

    cursor.execute(comando_sql)
    conexao_banco.commit()
    print("Alteração realizada com sucesso!")

# Função para excluir registros
def excluir():
    print("1- Excluir Animal")
    print("2- Excluir Funcionário")
    print("3- Excluir Habitat")
    print("4- Excluir Ingresso")
    print("5- Excluir Loja")
    print("6- Excluir Visitante")
    opcao = int(input("Escolha a opção de exclusão: "))

    tabela = ["animais", "funcionarios", "habitat", "ingressos", "lojas", "visitantes"]
    if opcao in range(1, 7):
        id_registro = int(input("ID do registro para excluir: "))
        comando_sql = f'DELETE FROM {tabela[opcao - 1]} WHERE Id = {id_registro}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print("Registro excluído com sucesso!")
    else:
        print("Opção inválida.")

# Função para pesquisar registros
def pesquisar():
    print("1- Pesquisar Animais")
    print("2- Pesquisar Funcionários")
    print("3- Pesquisar Habitat")
    print("4- Pesquisar Ingressos")
    print("5- Pesquisar Lojas")
    print("6- Pesquisar Visitantes")
    opcao = int(input("Escolha a opção de pesquisa: "))

    tabela = ["animais", "funcionarios", "habitat", "ingressos", "lojas", "visitantes"]
    if opcao in range(1, 7):
        comando_sql = f'SELECT * FROM {tabela[opcao - 1]}'
        cursor.execute(comando_sql)
        resultados = cursor.fetchall()
        for registro in resultados:
            print(registro)
    else:
        print("Opção inválida.")

# Loop principal
while True:
    print("====================")
    print("1- Cadastrar")
    print("2- Alterar")
    print("3- Excluir")
    print("4- Pesquisar")
    print("5- Sair")
    print("====================")
    op = int(input("Digite o número referente à opção desejada no menu: "))

    if op == 1:
        cadastrar()
    elif op == 2:
        alterar()
    elif op == 3:
        excluir()
    elif op == 4:
        pesquisar()
    elif op == 5:
        break
    else:
        print("ERRO: Valor digitado inválido. Tente novamente...")