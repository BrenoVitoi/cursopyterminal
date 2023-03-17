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
            print()
            self.name = input("Name :")
            time.sleep(0.20)
            self.phone = input("Phone :")
            time.sleep(0.20)
            self.address = input("Address :")
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO contacts\
                            (Name, Phone, Address)VALUES(?,?,?)""",
                           (self.name, self.phone, self.address))

            db.commit()
            add_more = input("DESEJA ADICIONAR OUTRO CONTATO ? (Y/N) :")
            if add_more == "y".lower():
                continue
            else:
                db.close()
                running = False
                print("SAINDO DO MENU")
                time.sleep(2)
                self.menu()

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
        print(results)
        time.sleep(0.100)

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
