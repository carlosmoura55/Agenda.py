agenda = []
def cadastrar_contato():
    nome = input("Digite o nome do contato: ")
    email = input("Digite o email do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contato = {
        "Nome": nome,
        "Email": email,
        "Telefone": telefone
    }
    agenda.append(contato)
    print("Contato cadastrado com sucesso!")

def buscar_por_nome():
    nome = input("Digite o nome para buscar: ")
    encontrados = []
    for contato in agenda:
        if contato["Nome"]:
            encontrados.append(contato)
    if encontrados:
        print("Contatos encontrados por nome:")
        for contato in encontrados:
            print(f"Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
    else:
        print("Nenhum contato encontrado por nome.")

def buscar_por_email():
    email = input("Digite o email para buscar: ")
    encontrados = []
    for contato in agenda:
        if contato["Email"]:
            encontrados.append(contato)
    if encontrados:
        print("Contatos encontrados por email:")
        for contato in encontrados:
            print(f"Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
    else:
        print("Nenhum contato encontrado por email.")

def buscar_por_telefone():
    telefone = input("Digite o telefone para buscar: ")
    encontrados = []
    for contato in agenda:
        if contato["Telefone"] == telefone:
            encontrados.append(contato)
    if encontrados:
        print("Contatos encontrados por telefone:")
        for contato in encontrados:
            print(f"Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
    else:
        print("Nenhum contato encontrado por telefone.")

def listar_contatos():
    if agenda:
        print("Contatos cadastrados:")
        for contato in agenda:
            print(f"Nome: {contato['Nome']}, Email: {contato['Email']}, Telefone: {contato['Telefone']}")
    else:
        print("Nenhum contato cadastrado.")

# Menu de opções
while True:
    print("\nOpções:")
    print("1 - Cadastrar contato")
    print("2 - Buscar por nome")
    print("3 - Buscar por email")
    print("4 - Buscar por telefone")
    print("5 - Contatos cadastrados")
    print("6 - Sair")

    escolha = input("Escolha uma opção (1/2/3/4/5/6): ")

    if escolha == '6':
        print("Encerrando a agenda.")
        break

    if escolha not in ('1', '2', '3', '4', '5'):
        print("Opção inválida. Tente novamente.")
        continue

    if escolha == '1':
        cadastrar_contato()
    elif escolha == '2':
        buscar_por_nome()
    elif escolha == '3':
        buscar_por_email()
    elif escolha == '4':
        buscar_por_telefone()
    elif escolha == '5':
        listar_contatos()