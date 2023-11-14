from teacherCRUD import TeacherCRUD

class CLI:
    def __init__(self):
        self.crud = TeacherCRUD('neo4j+s://50718b33.databases.neo4j.io','neo4j','vXKcrpKbrBxPdKmLAa9XRONWDGbpxq4w798kLVra3d4')

    def criar_professor(self):
        name = input("Digite o nome do professor: ")
        ano_nasc = int(input("Digite o ano de nascimento: "))
        cpf = input("Digite o CPF: ")

        self.crud.create(name, ano_nasc, cpf)
        print(f"Professor {name} criado com sucesso.")

    def buscar_professor(self):
        name = input("Digite o nome do professor a ser pesquisado: ")
        result = self.crud.read(name)

        if result:
            print("Resultado da Pesquisa:", result)
        else:
            print(f"Professor {name} não encontrado.")

    def atualizar_professor(self):
        name = input("Digite o nome do professor cujo CPF será atualizado: ")
        new_cpf = input("Digite o novo CPF: ")

        self.crud.update(name, new_cpf)
        print(f"CPF do Professor {name} atualizado com sucesso.")

    def deletar_professor(self):
        name = input("Digite o nome do professor a ser deletado: ")
        self.crud.delete(name)
        print(f"Professor {name} deletado com sucesso.")
    def menu(self):
        while True:
            print("-----------------------------")
            print("1. Criar Professor")
            print("2. Pesquisar Professor")
            print("3. Atualizar CPF do Professor")
            print("4. Deletar Professor")
            print("5. Sair")
            print("-----------------------------")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                self.criar_professor()
            elif choice == "2":
                self.buscar_professor()
            elif choice == "3":
                self.atualizar_professor()
            elif choice == "4":
                self.deletar_professor()
            elif choice == "5":
                self.crud.close()
                break
            else:
                print("Opção inválida. Tente novamente.")
