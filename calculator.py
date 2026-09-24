while True:
    human = input()
    if human == '+':
        print('NUMBER 1?')
        human1 = int(input())
        print('NUMBER 2?')
        human2 = int(input())
        print('OKAY: ',human1 + human2)
    elif human == '-':
        print('NUMBER 1?')
        human1 = int(input())
        print('NUMBER 2?')
        human2 = int(input())
        print('OKAY: ',human1 - human2)
    elif human == '*':
        print('NUMBER 1?')
        human1 = int(input())
        print('NUMBER 2?')
        human2 = int(input())
        print('OKAY: ',human1 * human2)
    elif human == '/':
        print('NUMBER 1?')
        human1 = int(input())
        print('NUMBER 2?')
        human2 = int(input())
        if human2 == 0:
            print('MATH ERROR')
        else:
            print('OKAY: ',human1 / human2)
    else:
        print('NO COMMAND')

