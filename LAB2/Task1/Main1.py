from Task1.Utilities1 import get_sentences_amount, get_not_declarative_sentences_amount, \
    get_average_sentence_length, get_average_word_length, n_grams

from Task1.Constants1 import TEST_FILE_PATH, AGREE, DISAGREE


def task1_main():
    text = get_text()
    print(text)

    sentences_amount(text)
    not_declarative_sentences_amount(text)
    average_sentence_length(text)
    average_word_length(text)
    NGrams(text)

    return 0


def get_text():
    with open(TEST_FILE_PATH) as f:
        text = f.read()

    return text


def sentences_amount(text):
    print(f"{get_sentences_amount(text)} - amount of sentences")


def not_declarative_sentences_amount(text):
    print(f"{get_not_declarative_sentences_amount(text)} - amount of non-declarative sentences")


def average_sentence_length(text):
    print(f"{get_average_sentence_length(text)} - average length of the sentence")


def average_word_length(text):
    print(f"{get_average_word_length(text)} - average length of the word")


def NGrams(text):
    while True:
        inp = input(f"Do you want to enter N and K? ({AGREE}/{DISAGREE})\n")

        if inp != AGREE and inp != DISAGREE:
            print("Try again\n")
        elif inp == AGREE:
            N = input_N()
            K = input_K()
            break
        else:
            N = 4
            K = 10
            break

    n_grams_list = n_grams(text, N, K)

    if len(n_grams_list) < K:
        print("K are bigger, then amount of  N-grams\n")

    print(f"top-{K} repeated {N}-grams in the text:")

    for n_gram in n_grams_list:
        print(n_gram)


def input_N():
    while True:
        try:
            N = int(input(f'Enter N: '))
        except:
            print(f"N must be an positive integer.\n")
        else:
            if N <= 0:
                print(f"N must be an positive integer.\n")
            else:
                return N


def input_K():
    while True:
        try:
            K = int(input(f'Enter K: '))
        except:
            print(f"K must be an positive integer.\n")
        else:
            if K <= 0:
                print(f"K must be an positive integer.\n")
            else:
                return K
