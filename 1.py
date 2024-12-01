alphabet = [
    "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П",
    "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ы", "Ъ", "Э", "Ю", "Я",
]

def get_table(mess): # Создание шифрующей таблицы
    table = list()
    letters = list()

    for i in mess:
        if i not in letters and i in alphabet:
            letters.append(i)
    for i in alphabet:
        if i not in letters and i in alphabet:
            letters.append(i)

    tmp = list()
    for i in letters: # Создание таблцы 8х4
        tmp.append(i)
        if len(tmp) == 8:
            table.append(tmp)
            tmp = []
    if tmp not in table and tmp != []:
        table.append(tmp)
    return table

def split_message(message): # Разделение сообщения на биграммы
    res = list()
    tmp = list()

    for i in message:
        if i not in tmp and i in alphabet:
            tmp.append(i)
        if len(tmp) == 2:
            res.append(tmp)
            tmp = []
    if tmp not in res and tmp != []:
        tmp.append("А") # В случае нечетного количества букв добавляется символ "А"
        res.append(tmp)

    return res

def get_position(table, let): # Получение координат буквы в таблице
    for i in range(len(table)):
        if let in table[i]:
            for j in range(len(table[i])):
                if table[i][j] == let:
                    return [i,j]


def cipher(spl_mess, table): # Шифрование
    res = list()

    for i in spl_mess:
        pos = list()
        for j in i:
            pos.append(get_position(table, j))
        first = pos[0]
        second = pos[1]
        a = ""

        if first[0] != second[0] and first[1] != second[1]:
            a = table[first[0]][second[1]]
            a += table[second[0]][first[1]]
        elif first[0] != second[0] and first[1] == second[1]:
            a = table[(first[0] + 1) % 4][first[1]]
            a += table[(second[0] + 1) % 4][second[1]]
        elif first[0] == second[0] and first[1] != second[1]:
            a = table[first[0]][(first[1] + 1) % 8]
            a += table[second[0]][(second[1] + 1) % 8]

        res.append(a)
    return res

def print_table(table): # Вывод шифрующей таблицы
    res = "-" * 33
    for i in table:
        res += "\n|"
        for j in i:
            res += " " + j + " " + "|"
    res += "\n" + "-" * 33
    print(res)


def main():
    message = "Конфиденциальность данных это статус предоставляемый данным и определяющий требуемую степень их защиты."
    message =  message.upper().replace(" ", "").replace("Ё", 'Е') # Приводит сообщение в нужную форму
    key = "ПОДЗЕМЕЛЬЯ"
    key = key.upper() # Приводит ключ в нужную форму

    print("-" * 30 + f"\nДано:\nСообщение = {message}\nКлюч = {key}\n" + "-" * 30)

    print(f"1. Разобьем этот текст на биграммы:")
    # 1
    spl_message = split_message(message)
    bigrams = ""
    for i in spl_message:
        for j in i:
            bigrams += j
        bigrams += " "
    print(bigrams + "\n" + "-" * 30)


    #2
    print(f"Таблица шифрования:")
    table = get_table(key)
    print_table(table)
    print("2. Данная последовательность биграмм открытого текста преобразуется с помощью шифрующей таблицы в следующую последовательность биграмм шифртекста")
    data = cipher(spl_message, table)
    print(*data)
    print("-" * 30)
    print(f"ОТВЕТ, ПОЛУЧИВШИЙСЯ ШИФРОТЕКСТ:")
    print(*data)
    print("-" * 30)

if __name__ == "__main__":
    main()
