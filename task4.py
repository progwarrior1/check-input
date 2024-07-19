from func import *


def main():
    print('дай мне на проверку данные')
    print('сечас проверим пин')
    n = checkpin(input())
    pin, email_, name_, pass_ = 0, 0, 0, 0
    while pin == 0:
        if n == True:
            print('все верно')
            pin += 1
        else:
            print('нужно кое что потправить')
            n = checkpin(input())
    print('сейчас поверим твой пароль')
    n2 = checkpass(input())
    while pass_ == 0:
        if n2 == True:
            print('все верно')
            pass_ += 1
        else:
            print('нужно кое что потправить')
            n2 = checkpass(input())
    print('сейчас поверим твой почту')
    n3 = checkmail(input())
    while email_==0:
        if n3 == True:
            print('все верно')
            email_+=1
        else:
            print('нужно кое что потправить')
            n3 = checkmail(input())
    print('сейчас поверим твой имя')
    n4 = checkname(input())
    while name_==0:
        if n4 == True:
            print('все верно')
            name_+=1
        else:
            print('нужно кое что потправить')
            n4 = checkname(input())


main()
