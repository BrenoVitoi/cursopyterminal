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
            self.list()

        elif opcao == "5":
            self.terminate()

        else:
            winsound.Beep(2500, 100)
            print("ERROR, TENTA NOVAMENTE AS OPCOES 1-5")
            time.sleep(2)

    def main(self):
        os.system("cls")
        self.menu()


contacts_manager = Manager()
contacts_manager.main()
