# Шифр Виженера с повторяющимся ключом
def fix_key_encode(key: str, opentext: str):  # повторение короткого лозунга зашифровка
    ''.join(opentext.upper().split())
    #  представляем ключ и текст как массив индексов
    key_as_int = [ord(i) for i in key.upper()]
    opentext_int = [ord(i) for i in ''.join(opentext.upper().split())]
    cipher = ''

    #  производим зашифрование
    for n in range(len(opentext)):
        result = (opentext_int[n] + key_as_int[n % len(key)]) % 26
        cipher += chr(result + 65)
        # 65 мы добавляем потому что в кодировке utf-8 буква а стоит на 65 позиции,
        # b - на 66, и т.д.
    return cipher


def fix_key_decode(key: str, cipher: str):  # повторение короткого лозунга расшифровка
    #  представляем ключ и текст как массив индексов
    key_as_int = [ord(i) for i in key.upper()]
    text_int = [ord(i) for i in "".join(cipher.upper().split())]
    opentext = ''

    #  производим расшифровку
    for n in range(len(text_int)):
        result = (text_int[n] - key_as_int[n % len(key)]) % 26
        opentext += chr(result + 65)
        # + 65 мы добавляем потому что в кодировке utf-8 буква а стоит на 65 позиции,
        # b - на 66, и т.д.
    return opentext


# Шифр Виженера с самоключом по открытому тексту
def autokey_by_opentxt_encode(key: str, text: str):
    #  предобработка ключа и текста
    key = key.upper()
    text = "".join(text.upper().split())
    #  вычисление сдвига
    a = len(text) - len(key)
    new_text = text[:a]
    #  формирование гаммы
    gamma = key + new_text
    gamma = "".join(gamma.split())
    #  представление гаммы и текста как массив индексов
    gamma_as_int = [ord(i) for i in gamma]
    text_int = [ord(i) for i in text]
    ciphertext = ''

    #  производим шифровку
    for n in range(len(text)):
        result = (text_int[n] + gamma_as_int[n % len(gamma)]) % 26
        ciphertext += chr(result + 65)
    return ciphertext


def autokey_by_opentxt_decode(key: str, cipher: str):
    #  предобработка входных данных
    cipher = cipher.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    #  представление ключа и текста в виде массива индексов
    gamma_as_int = [ord(i) - 65 for i in key]
    cipher_as_int = [ord(i) - 65 for i in cipher]
    opentxt_int = [] # расшифрованный текст в виде массива индексов
    opentxt = ""

    #  производим расшифровку сначала части текста, которая равна длине ключа
    for i in range(len(gamma_as_int)):
        opentxt_ind = (cipher_as_int[i] - gamma_as_int[i]) % 26
        opentxt_int.append(opentxt_ind)
        opentxt += chr(opentxt_ind + 65)

    #  производим расшифровку по полученной части открытого текста
    for j in range(len(gamma_as_int), len(cipher_as_int)):
        opentxt_ind = (cipher_as_int[j] - opentxt_int[j - len(gamma_as_int)]) % 26
        opentxt_int.append(opentxt_ind)
        opentxt += chr(opentxt_ind + 65)
    return opentxt


# Шифр Виженера с самоключом по шифр тексту
def autokey_by_ciphertxt_encode(key: str, txt: str):
    #  предобработка входных данных
    txt = txt.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    #  представляем гамму и текст как массив индексов
    gamma_as_int = [ord(i) - 65 for i in key]
    txt_as_int = [ord(i) - 65 for i in txt]
    ciphertxt_int = []
    ciphertxt = ""

    #  производим шифровку сначала части текста, которая равна длине ключа
    for i in range(len(gamma_as_int)):
        ciphertxt_ind = (txt_as_int[i] + gamma_as_int[i]) % 26
        ciphertxt_int.append(ciphertxt_ind)
        ciphertxt += chr(ciphertxt_ind + 65)

    #  производим шифровку по полученной части шифр текста
    for j in range(len(gamma_as_int), len(txt_as_int)):
        ciphertxt_ind = (txt_as_int[j] + ciphertxt_int[j - len(gamma_as_int)]) % 26
        ciphertxt_int.append(ciphertxt_ind)
        ciphertxt += chr(ciphertxt_ind + 65)
    return ciphertxt


def autokey_by_ciphertxt_decode(key: str, ctext: str):
    #  предобработка входных данных
    key = key.upper()
    ctext = "".join(ctext.upper().split())
    #  вычисление сдвига
    a = len(ctext) - len(key)
    cnew_text = ctext[:a]
    #  формирование гаммы
    gamma = key + cnew_text
    gamma = "".join(gamma.split())
    #  представляем гамму и текст как массив индексов
    gamma_as_int = [ord(i) for i in gamma]
    ctext_int = [ord(i) for i in ctext]
    otext = ''

    #  производим расшифровку
    for n in range(len(ctext)):
        result = (ctext_int[n] - gamma_as_int[n % len(gamma)]) % 26
        otext += chr(result + 65)
    return otext


# menu
key_input = input("Введите ключ: ")
text_input = input("Введите текст для шифровки/расшифровки: ")
choice_var = int(input("Выберите вариант шифровки | 1 -- повторение ключа, 2 -- самоключ по открытому тексту, "
                       "3 -- самоключ по шифр тексту | Ваш выбор: "))
choice_act = int(input("1 -- шифровка, 2 -- расшифровка | Ваш выбор: "))

if choice_act == 1:
    if choice_var == 1:
        print("Шифр текст с повторяющимся ключом: ", fix_key_encode(key_input, text_input))
    elif choice_var == 2:
        print("Шифр текст с самоключом по открытому тексту: ", autokey_by_opentxt_encode(key_input, text_input))
    elif choice_var == 3:
        print("Шифр текст с самоключом по шифр тексту: ", autokey_by_ciphertxt_encode(key_input, text_input))
elif choice_act == 2:
    if choice_var == 1:
        print("Открытый текст с повторяющимся ключом: ", fix_key_decode(key_input, text_input))
    elif choice_var == 2:
        print("Открытый текст с самоключом по открытому тексту: ", autokey_by_opentxt_decode(key_input, text_input))
    elif choice_var == 3:
        print("Открытый текст с самоключом по шифр тексту: ", autokey_by_ciphertxt_decode(key_input, text_input))
else:
    print("Введены некорректные данные!")