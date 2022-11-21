import requests
import json


def get_word_random():
    word_request = requests.get('https://api.dicionario-aberto.net/random')
    word_random = json.loads(word_request.content)
    return word_random["word"]


class MysteriousWord:
    def __init__(self):
        self.get_word = get_word_random()
        self.letters_list = list(len(self.get_word) * '{}'.format('_'))
        self.letters_digit = []
        self.chances = 10

    def search_word(self):
        print('Descubra a palavra misteriosa!\n')
        print(f'A palavra ministeriosa possue {len(self.get_word)} letras...')

        while True:
            if self.chances == 0:
                print('Suas chances acabaram... Tente novamente!')
                exit()

            get_letter = input(f'\nDigite uma letra: ').lower()

            if len(get_letter) > 1:
                print('Digite apenas uma letra...')
                continue

            if get_letter.isalpha():
                if get_letter in self.letters_digit:
                    print(f'\nLetra "{get_letter.upper()}" já utilizada, digite outra...')
                    print(f'Você possue {self.chances} chances.\n')

                if get_letter not in self.get_word:
                    self.letters_digit.append(get_letter)
                    self.chances -= 1
                    print(f'\nLetra "{get_letter.upper()}" não encontrada, digite outra...')
                    print(f'Você possue {self.chances} chances.\n')

                for letter in range(len(self.get_word)):
                    if get_letter in self.get_word[letter]:
                        self.letters_list[letter] = get_letter
                        self.letters_digit.append(get_letter)
                        formatted_word = ''.join([str(item) for item in self.letters_list]).upper()
                        print(formatted_word, '\n')

                print('Qual ação realizar?')
                get_option_word = input('[1] Digitar letra [2] Chutar palavra ')

                match get_option_word:
                    case '1':
                        self.chances -= 1
                        print(f'\nVocê possue {self.chances} chances.')
                        continue
                    case '2':
                        digit_word = input('Digite a palavra: ')
                        if digit_word == self.get_word:
                            print('Parabéns, você descobriu a Palavra Misteriosa!')
                            exit()
                        else:
                            self.chances -= 1
                            print('Palavra incorreta, tente novamente...')
                            print(f'Você possue {self.chances} chances.')
                            continue
                    case _:
                        print('Digite apenas ações válidas!', '\n')
                        continue

            else:
                print('Digite apenas letras.')
                continue


game = MysteriousWord()
game.search_word()
