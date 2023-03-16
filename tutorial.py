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
        print("-------------Menu----------------")
        print("1 :) add")

        print("2 :) Remove")

        print("3 :) Update")

        print("4 :) List")

        print("5 :) Terminate")

    def main(self):
        self.menu()


contacts_manager = Manager()
contacts_manager.main()
