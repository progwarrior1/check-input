def checkpin(pin):
    if len(pin) == 4 and pin != '1234' and pin[0] != pin[1]:
        return True
    else:
        return False


def checkpass(password):
    flag1 = False
    flag2 = False
    for i in password:
        if i in 'абвгдеёжзийклмнопрстуфцзъхчщшыюяэ' or i in 'abcdefghijklmnopqrstuvwxyz':
            flag1 = True
            continue
        if i in '12345678910':
            flag2 = True
            continue
    if len(password) >= 8 and flag1 and flag2:
        return True
    else:
        return False


def checkmail(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False


def checkname(name):
    allowed_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    for char in name:
        if char.lower() not in allowed_chars:
            return False
    return True
