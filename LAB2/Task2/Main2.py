from Task2.Constants2 import COMMANDS, ERRORS, CONTAINER_OUTPUT
from Task2.Constants2 import LOAD_DATA, INPUT_COMMAND, INPUT_USERNAME
from Task2.Container2 import MyContainer
from Task2.ErrorHandler2 import ErrorHandler
from Task2.ContainerOutputHandler2 import ContainerOutputHandler


def task2_main():
    container = handle_username_input()
    handle_data_load(container)
    handle_command_input(container)


def handle_username_input():
    while True:
        username = input_username()

        if type(username) == type(""):
            return MyContainer(username)
        else:
            match username:
                case ERRORS.EMPTY_INPUT:
                    ErrorHandler.handle_empty_input()

                case _:
                    ErrorHandler.handle_unexpected_error()


def handle_data_load(container):
    while True:
        check_state = ContainerOutputHandler.HandleContainerOutput(load_data(container))

        if check_state == ERRORS.VALID:
            return


def handle_command_input(container):
    while True:
        commandExpression = input_command(container)

        if type(commandExpression) == type(ERRORS.EMPTY_INPUT):
            match commandExpression:
                case ERRORS.EMPTY_INPUT:
                    ErrorHandler.handle_empty_input()
                case ERRORS.UNEXPECTED_ERROR:
                    ErrorHandler.handle_unexpected_error()
                case ERRORS.INVALID_COMMAND:
                    ErrorHandler.handle_invalid_command()
        else:
            command = commandExpression[0]
            args = commandExpression[1][0:]

            match command:
                case COMMANDS.ADD:
                    ContainerOutputHandler.HandleContainerOutput(container.add(args))

                case COMMANDS.REMOVE:
                    ContainerOutputHandler.HandleContainerOutput(container.remove(args))

                case COMMANDS.FIND:
                    ContainerOutputHandler.HandleContainerOutput(container.find(args))

                case COMMANDS.LIST:
                    container.list()

                case COMMANDS.GREP:
                    ContainerOutputHandler.HandleContainerOutput(container.grep(args))

                case COMMANDS.SAVE:
                    ContainerOutputHandler.HandleContainerOutput(container.save())

                case COMMANDS.LOAD:
                    ContainerOutputHandler.HandleContainerOutput(container.load_data())

                case COMMANDS.EXIT:
                    ContainerOutputHandler.HandleContainerOutput(container.wanna_save())
                    return

                case COMMANDS.SWITCH:
                    ContainerOutputHandler.HandleContainerOutput(container.switch(args))

                case COMMANDS.HELP:
                    container.help()

                case _:
                    ErrorHandler.handle_invalid_command()


def input_command(container):
    command = input(INPUT_COMMAND)

    check_state = is_empty_input(command)

    match check_state:
        case ERRORS.EMPTY_INPUT:
            return ERRORS.EMPTY_INPUT

        case ERRORS.VALID:
            pass

        case _:
            return ERRORS.UNEXPECTED_ERROR

    command = command.split()
    if COMMANDS.CONTAINS(command[0]):
        return COMMANDS.GETITEM(command[0]), command[1:]
    else:
        return ERRORS.INVALID_COMMAND


def input_username():
    username = input(INPUT_USERNAME)

    check_state = is_empty_input(username)
    if check_state == ERRORS.VALID:
        return username
    else:
        return check_state


def load_data(container):
    answer = input(f"{LOAD_DATA} ({COMMANDS.AGREE.value}/{COMMANDS.DISAGREE.value}) ")

    match answer:
        case COMMANDS.AGREE.value:
            return container.load_data()

        case COMMANDS.DISAGREE.value:
            return CONTAINER_OUTPUT.VALID

        case _:
            return CONTAINER_OUTPUT.UNEXPECTED_ERROR


def is_empty_input(input_line):
    if not input_line:
        return ERRORS.EMPTY_INPUT
    else:
        return ERRORS.VALID
