 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import os

def main():
    print '\033[95m[1] Addition'
    print '\033[95m[2] Subtraction'
    print '\033[95m[3] Multiplication'
    print '\033[95m[4] Division'
    print '\033[95m[5] Exit'

    option = input('~~>')

    if option == 1:
        os.system('cls || clear')
        print '\033[93m[ Addition ]'
        AdditionNumb1 = input('\033[94mEnter the first digit: ')
        AdditionNumb2 = input('\033[94mEnter the second digit: ')
        additionAnswer = int(AdditionNumb1) + int(AdditionNumb2)

        print('{0} + {1} = {2}'.format(AdditionNumb1, AdditionNumb2, additionAnswer))

    if option == 2:
        os.system('cls || clear')
        print '\033[93m[ Subtraction ]'
        SNumb1 = input('\033[94mEnter the first digit: ')
        SNumb2 = input('\033[94mEnter the second digit: ')
        SAnswer = int(SNumb1) - int(SNumb2)

        print('{0} - {1} = {2}' .format(SNumb1, SNumb2, SAnswer))

    if option == 3:
        os.system('cls || clear')
        print '\033[93m[ Multiplication ]'
        MultiplicationNumb1 = input('\033[94mEnter the first digit: ')
        MultiplicationNumb2 = input('\033[94mEnter the second digit: ')
        multiplicationAnswer = int(MultiplicationNumb1) * int(MultiplicationNumb2)

        print('{0} × {1} = {2}' .format(MultiplicationNumb1, MultiplicationNumb2, multiplicationAnswer))

    if option == 4:
        os.system('cls || clear')
        print '\033[93m[ Division ]'
        DivisionNumb1 = input('\033[94mEnter the first digit: ')
        DivisionNumb2 = input('\033[94mEnter the second digit: ')
        DivisionAnswer = int(DivisionNumb1) / int(DivisionNumb2)

        print('{0} ÷ {1} = {2}' .format(DivisionNumb1, DivisionNumb2, DivisionAnswer))

    if option == 5:
        os.system('cls || clear')
        print '\033[93m[ EXIT ]'
        exit()
main()
