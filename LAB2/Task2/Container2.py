import re
from json import load, dump
from re import match, compile
from Task2.Constants2 import COMMANDS, CONTAINER, CONTAINER_OUTPUT, SAVE_DATA, COMMANDS_LIST


class MyContainer:
    def __init__(self, userName):
        self.userName = userName
        self.user_container = []
        self.file = {}

        self.load_file()

    def add(self, arg):
        if not arg:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        if type(arg) == type(''):
            if arg not in self.user_container:
                self.user_container.append(arg)
        else:
            for element in arg:
                if element not in self.user_container:
                    self.user_container.append(element)

        return CONTAINER_OUTPUT.VALID

    def remove(self, element):
        if element:
            element = element[0]
        else:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        if element not in self.user_container:
            return CONTAINER_OUTPUT.NOTHING_TO_DELETE
        else:
            self.user_container.remove(element)
            return CONTAINER_OUTPUT.VALID

    def find(self, arg):
        if not self.user_container:
            return CONTAINER_OUTPUT.EMPTY_CONTAINER
        if not arg:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        if type(arg) == type(''):
            if arg not in self.user_container:
                return CONTAINER_OUTPUT.NO_SUCH_ELEMENT
            else:
                print(arg)
                return CONTAINER_OUTPUT.VALID
        else:
            element_where_founded = 0
            for element in arg:
                if element in self.user_container:
                    print(element)
                    element_where_founded = 1

            if element_where_founded:
                return CONTAINER_OUTPUT.VALID
            else:
                return CONTAINER_OUTPUT.NO_SUCH_ELEMENT

    def list(self):
        print(self.user_container)

    def grep(self, reg):
        if not self.user_container:
            return CONTAINER_OUTPUT.EMPTY_CONTAINER
        if not reg:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS
        else:
            reg = reg[0]

        try:
            reg_match = [element for element in self.user_container if match(compile(reg), element)]
        except re.error:
            return CONTAINER_OUTPUT.INVALID_REGEX

        if reg_match:
            print("Matched elements: ")
            for elem in reg_match:
                print(elem)
            return CONTAINER_OUTPUT.VALID
        else:
            return CONTAINER_OUTPUT.NO_SUCH_ELEMENT

    def save(self):
        self.file[self.userName] = self.user_container

        with open(CONTAINER + "data.json", 'w') as file:
            dump(self.file, file)

        return CONTAINER_OUTPUT.VALID

    def load_file(self):
        with open(CONTAINER + "data.json", 'r') as file:
            self.file = load(file)

    def load_data(self):
        data = self.user_container
        self.load_file()

        if not self.file.get(self.userName):
            return CONTAINER_OUTPUT.EMPTY_CONTAINER

        self.add(self.file[self.userName])
        return CONTAINER_OUTPUT.VALID

    def wanna_save(self):
        while True:
            command = input(f"{SAVE_DATA} ({COMMANDS.AGREE.value}/{COMMANDS.DISAGREE.value})")
            if command == COMMANDS.AGREE.value:
                self.save()
                return CONTAINER_OUTPUT.VALID

            elif command == COMMANDS.DISAGREE.value:
                return CONTAINER_OUTPUT.VALID

    def switch(self, ListUserName):
        if not ListUserName:
            return CONTAINER_OUTPUT.EMPTY_ARGUMENTS

        self.wanna_save()
        self.user_container = []

        true_user_name = ListUserName[0]

        self.userName = true_user_name
        if self.userName not in self.file:
            self.user_container = []

        return CONTAINER_OUTPUT.VALID

    def help(self):
        print(COMMANDS_LIST)
