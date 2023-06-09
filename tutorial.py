import sqlite3
import os
import time
import winsound


class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.address = ""

    def add(self):
        running = True
        while running:
            os.system("cls")
            print("-------------ADICIONE UM NOVO CONTATO-------------")
            print("PRECIONE A TECLA SHIFT + Q PARA CANCELAR")
            print()

            temp_name = input("Name: ")
            if len(temp_name) != 0 and temp_name != "Q".upper():
                db = sqlite3.connect("connection")
                cursor = db.cursor()
                cursor.execute("SELECT Name FROM contacts")
                results = cursor.fetchall()
                for i in results:
                    if temp_name in i:
                        print("ESTE CONTATO JA EXISTE NO NOSSO BANCO DE DADOS")
                        time.sleep(3)
                        self.add()
                self.name = temp_name
                temp_name = ""

                time.sleep(0.20)
                self.phone = input("Phone :")
                time.sleep(0.20)
                self.address = input("Address :")

                cursor.execute(""" INSERT INTO contacts\
                                (Name, Phone, Address)VALUES(?,?,?)""",
                               (self.name, self.phone, self.address))

                db.commit()
                add_more = input(
                    "DESEJA ADICIONAR OUTRO CONTATO ? (Y/N) :")
                if add_more == "y".lower():
                    continue
                else:
                    db.close()
                    running = False
                    print("SAINDO DO MENU")
                    time.sleep(2)
                    self.menu()
            elif temp_name == "Q".upper():
                print("SAINDO DO MENU PRINCIPAL")
                time.sleep(2)
                self.menu()
            else:
                winsound.Beep(3000, 100)
                winsound.Beep(3000, 100)
                print("FAVOR PREENCHER TODOS OS CAMPOS ")
                time.sleep(3)

    def update(self):
        pass

    def remove(self):
        pass

    def get_list(self):
        count = 0
        count_2 = 0
        db = sqlite3.connect("connection")
        cursor = db.cursor()
        os.system("cls")
        print("-------------CONTATOS--------------")

        time.sleep(0.50)
        cursor.execute("SELECT Name, Phone, Address FROM contacts")
        results = cursor.fetchall()
        for row in results:
            time.sleep(0.50)
            count += 1
            count_2 += 1
            print(count_2, row)
            if count == 5:
                input("PRECIONE QUALQUER TECLA PARA CONTINUAR")
                count = 0
                print()
            print()
            print("FINAL DOS RESULTADOS")
            print()
            print("PRECIONE QUALQUER TECLA PARA CONTINUAR")
            option = input(
                "APERTE (A) PARA ATUALIZA, D PARA DELETAR M PARA MENU :")
            if option == "a".lower():
                self.update()

            elif option == "d".lower():
                self.remove()

            elif option == "m".lower():
                self.menu()

    def terminate(self):
        pass

    def menu(self):
        os.system("cls")
        winsound.Beep(2000, 50)
        print("-------------Menu----------------")
        time.sleep(0.05)
        print()
        print("1 :) add")
        time.sleep(0.05)

        print("2 :) Remove")
        time.sleep(0.05)

        print("3 :) Update")
        time.sleep(0.05)

        print("4 :) List")
        time.sleep(0.05)

        print("5 :) Terminate")
        print()

        opcao = input("SELECIONE UMA ACAO :")
        if opcao == "1":
            self.add()
        elif opcao == "2":
            self.remove()

        elif opcao == "3":
            self.update()

        elif opcao == "4":
            self.get_list()

        elif opcao == "5":
            self.terminate()

        else:
            winsound.Beep(2500, 100)
            print("ERROR, TENTA NOVAMENTE AS OPCOES 1-5")
            time.sleep(2)
            self.menu()

    def main(self):
        os.system("cls")
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(3)
            winsound.Beep(2000, 50)
            print("CONECTADO AO BANCO DE DADOS")
            time.sleep(3)
            self.menu()
        else:
            print("ESTA CONEXAO  NAO EXISTE")
            print()
            time.sleep(3)
            WindowsError(2000, 50)

            print("CRIANDO NOVA CONEXAO COM O BANCO DE DADO")
            time.sleep(3)
            db = sqlite3.connect("connection")

            cursor = db.cursor()
            cursor.execute("""CREATE TABLE contacts
                            (Name TEXT, Phone TEXT, Address TEXT)""")

            winsound.Beep(2000, 50)
            print()

            print("Conexao criada com sucesso")
            print("Conectado com sucesso")
            time.sleep(3)
            self.menu()

        self.menu()


contacts_manager = Manager()
contacts_manager.main()
