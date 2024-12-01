def encrypt(m, k, n): # Зашифровка
    c = pow(m, k, n)
    print(f"C = M^K mod N = {m}^{k} mod {n} = {c}\n" + "-" * 30)
    return c


def decrypt(c, k_inv, n): # Расшифровка
    m = pow(c, k_inv, n)
    print(f"M = C^K* mod N = {c}^{k_inv} mod {n} = {m}\n" + "-" * 30)
    return m

def gcd(a, b): # Нахождение НОД
    while b:
        a, b = b, a % b
    return a

def mod_inverse(k, mod):
    # Проверяем, что K и mod взаимно просты
    if gcd(k, mod) != 1:
        raise ValueError("K и N-1 должны быть взаимно просты для существования обратного.")

    res = pow(k, -1, mod)
    return res

def main():
    n = 61
    g = 41
    k_a = 15
    k_b = 21
    m = 3
    print("-" * 30 + f"\nДано:\nN = {n}\ng = {g}\nK_A = {k_a}\nK_b = {k_b}\nm = {m}\n" + "-" * 30)

    print(f"1. Для того, чтобы иметь общий секретный ключ К, пользователи А и В сначала вычисляют значения частных открытых ключей:")
    y_a = pow(g, k_a, n)
    print(f"yA = g^k_a mod N = {g}^{k_a} mod {n} = {y_a}")
    y_b = pow(g, k_b, n)
    print(f"yB = g^k_b mod N = {g}^{k_b} mod {n} = {y_b}\n" + "-" * 30)

    print("2. После того, как пользователи А и В обменяются своими значениями yA и yВ , они вычисляют общий секретный ключ")
    k_a_ever = pow(y_b, k_a, n)
    print(f"K1 = (y_b)^k_a mod N = {y_b}^{k_a} mod {n} = {k_a_ever}")
    k_b_ever = pow(y_a, k_b, n)
    print(f"K2 = (y_a)^k_b mod N = {y_a}^{k_b} mod {n} = {k_b_ever}")
    if k_a_ever != k_b_ever:
        raise ValueError("Ключи не совпадают!")
    k = k_a_ever
    print(f"Общий секретный ключ: K = {k_a_ever}\n" + "-" * 30)

    print("3. Вычисление обратного ключа K*:")
    k_inv = mod_inverse(k, n - 1)
    print(f"K* = {k_inv}\n" + "-" * 30)

    print("4. Шифрование сообщения")
    c = encrypt(m, k, n)

    print("5. Расшифровка сообщения")
    m_dec = decrypt(c, k_inv, n)

    print(f"ОТВЕТ:\nЗАШИФРОВАННОЕ СООБЩЕНИЕ:{c}\nРАСШИФРОВАННОЕ СООБЩЕНИЕ:{m_dec}, СООБЩЕНИЕ = {m}")

if __name__ == "__main__":
    main()