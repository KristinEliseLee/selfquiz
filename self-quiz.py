import random

allQs = []
askedQs = []

class Question():
    def __init__(self, text, options, answer):
        self. text = text
        self.options = options
        self.answer = answer


def loadQuestions(fileName):
    allQuestions = []
    with open(f'questions/{fileName}.txt') as file:
        text = ''
        options = []
        answer = ''
        for line in file.readlines():
            if line[0] == 'Q':
                # for multi-line questions, each line must start with Q, same with answer
                text += line[4:]
            elif line[0] == 'R':
                answer += line[4:]
            elif line[:3] != '---':
                options.append(line.rstrip())
            else:
                allQuestions.append(Question(text, options, answer))
                text = ''
                options = []
                answer = ''

    return allQuestions


def printMainMenu():
    print()
    print('To load files, type load')
    print('To start questions, type start')
    print('To quit, type quit')
    print()


def loadMenu():
    print()
    print('Load Questions')
    print()
    selection = ''
    while selection != 'menu':
        print()
        print('Please type the name of a file you wish to load(minus .txt), or type menu to return to main menu')
        selection = input()
        try:
            toAdd = loadQuestions(selection)
            allQs.extend(toAdd)
        except:
            print()
            print('Please check file name')

def askQuestions(qlist):
    if not qlist:
        print()
        print('No questions loaded')
        print()
        return 'menu'
    for q in qlist:
        print(q.text)
        for option in q.options:
            print(option)
        selection = input().lower()
        if selection == 'quit':
            return 'quit'
        if selection == "menu":
            return 'menu'

        print(q.answer)
        selection = input().lower()
        if selection == 'quit':
            return 'quit'
        if selection == "menu":
            return 'menu'


    print('Asked all questions. Returning to main menu')
    return selection





if __name__ == '__main__':
    selection = 'OK'
    while selection.lower() != 'quit':
        printMainMenu()
        selection = input().lower()

        if selection == 'load':
            loadMenu()

        elif selection == "start":
            random.shuffle(allQs)
            print('To quit at any time, type quit')
            selection = askQuestions(allQs)

    print('Thank you for playing. Goodbye')





