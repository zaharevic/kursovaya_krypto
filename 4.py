def get_d(e, z): # Получение d
    q_big = [1, 0]
    q_lit = []
    n = 2

    print("Воспользуемся расширенным алгоритмом Евклида:")
    elem_1 = e
    elem_2 = z
    flag = True
    while flag:
        q_lit.append(elem_1 // elem_2)
        print(f"{elem_1}={elem_2}*{q_lit[-1]}+{elem_1 - elem_2 * q_lit[-1]}")
        elem_1, elem_2 = elem_2, elem_1 % elem_2
        flag = (0 != elem_2)

    print(f"\nНайдем Q_n:")
    q = 1
    while q != z:
        q = q_lit[n - 2] * q_big[n - 1] + q_big[n - 2]
        print(f"{q_lit[n - 2]} * {q_big[n - 1]} + {q_big[n - 2]} = {q}")
        q_big.append(q)
        n += 1

    n = len(q_lit) - 2
    q_n = q_big[-2]
    d = (-1) ** n * q_n
    print(f"\nВычислим d = (-1)^n * Q_n = (-1)^{n} * {q_n} = {d}")
    if d < 0:
        print(f"\nТак как d у нас получилось отрицательным, то мы воспользуемся формулой, чтобы привести d к положительному числу.\n"
              f"z = {z}; d = {d} + {z} = {z + d}")
        d = z + d
    print("-" * 30)
    return d


def get_z(p, q): # Получение z
    return (p - 1) * (q - 1)


def message_delimer(message, n): # Делит сообщение на блоки
    length = 0
    res = list()

    while n > 10:
        n = int(n / 10)
        length += 1

    arr = list()
    tmp = list()
    for i in message:
        tmp.append(i)
        if len(tmp) == length:
            arr.append(tmp)
            tmp = []
    if tmp not in arr and tmp != []:
        arr.append(tmp)

    for i in arr:
        tmp = ""
        for j in i:
            tmp += j
        res.append(int(tmp))
    return res


def cipher(mess, e, n): # Шифрование
    c_big = list()

    for j in mess:
        c_big.append(pow(j, e, n))
    return c_big


def decipher(cipher, d, n): # Дешифрование
    m = list()

    for j in cipher:
        m.append(pow(j, d, n))
    return m


def main():
    p = 47
    q = 101
    e = 83
    message = "234 616 141 136 234 616 748".replace(" ", "")
    n = p * q

    print("-" * 30 + f'\nДано:\np={p}\nq={q}\ne-{e}\nСообщение:{message}\n' + "-" * 30)

    # 1
    z = get_z(p, q)
    print(f"1. Найдем z = (p-1)(q-1) и n = pq\nz={z}\nn={n}\n" + "-" * 30)

    # 2
    print(f"2. Найдем секретный ключ d в результате решения сравнения: de mod z = 1")
    d = get_d(e, z)

    # 3
    print(
        f"3. Разобьем сообщение на блоки mi, которые должны иметь длину, меньшую, чем n = pq = {p}*{q} = {n}\nПолучившиеся болки:")
    message_del = message_delimer(message, n)
    print(message_del)
    print("-" * 30)

    # 4
    print(f"4. Затем шифруем блоки: Ci = mi^e mod n\nПолучим криптограмму:")
    c_big = cipher(message_del, e, n)
    print(*c_big)

    # 5
    print(
        "-" * 30 + f'\n5. Для дешифрования нужно выполнить возведение в степень, используя ключ дешифрования d, т.е mi = Ci^d mod n')
    de = decipher(c_big, d, n)
    print(f"Получившиеся расшифрованное сообщение: {de}\n" + "-" * 30)

    print(f'ОТВЕТ:\nПОЛУЧИВШИЙСЯ ШИФРОТЕКСТ: {c_big}\nРАСШИФРОВАННОЕ СООБЩЕНИЕ: {de}\n' + "-" * 30)


if __name__ == "__main__":
    main()
