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
        pass

    def update(self):
        pass

    def remove(self):
        pass

    def get_list(self):
        pass

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
                            (NAME TEXT, Phone TEXT, AdressTEXT)""")

            winsound.Beep(2000, 50)
            print()

            print("Conexao criada com sucesso")
            print("Conectado com sucesso")
            time.sleep(3)
            self.menu()

        self.menu()


contacts_manager = Manager()
contacts_manager.main()
