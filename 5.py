def gcd(a, b): # Определение НОД
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, mod): # Поиск обратного mod
    t, new_t = 0, 1
    r, new_r = mod, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("Обратного элемента не существует")
    if t < 0:
        t += mod
    return t

def main():
    p = 29
    g = 4
    x = 10
    y = pow(g, x, p)
    m_hash = 3
    k = 5
    print("-" * 30 + f"\nДано P = {p}\nG = {g}\nX = {x}\nY = G ^ (x) mod P = {g} ^ {x} mod {p} = {y}\nХэш = {m_hash}\nk = {k}\n" + "-" * 30)

    print(f"1. Убедимся, что числа K и (P – 1) являются взаимно простыми")
    if gcd(k, p - 1) != 1:
        raise ValueError(f"K ({k}) и (P-1) ({p - 1}) не взаимно простые.")
    print(f"НОД(K, P-1) = НОД({k}, {p}-1) = 1\n" + "-" * 30)

    print(f"2. Вычисляем a = G^K mod P и b, решая уравнение m = (X * a + K * b) mod (P-1)")
    a = pow(g, k, p)
    print(f"a = G ^ K mod P = {g}^{k} mod {p} = {a}")

    print(f"Выражаем b:\nm = {m_hash}, a = {a}, X = {x},  K = {k}, P = {p}")
    print("b = ((m - X * a) * mod_inverse(K, P-1)) mod (P-1).")
    mod_inv_k = mod_inverse(k, p - 1)
    b = ((m_hash - x * a) * mod_inv_k) % (p - 1)
    print(f"b = (({m_hash} - {x} * {a}) * {mod_inv_k}) mod {p - 1} = {b}\n" + "-" * 30)

    print(f"3.Приняв подписанное сообщение и открытый ключ Y = {y}, получатель вычисляет хэш-значение для сообщения M : m = {m_hash}, а затем вычисляет два числа:")
    a1 = (pow(y, a, p) * pow(a, b, p)) % p
    print(f"Y^(a)*a^(b)(mod P) = {y}^{a} * {a}^{b} mod {p} = {a1}")
    a2 = pow(g, m_hash, p)
    print(f"G^m mod P = {g}^{m_hash} mod {p} = {a2}\n" + "-" * 30)

    if a1 == a2:
        print(f"4. {a1} = {a2}\nТак как эти два целых числа равны, принятое получателем сообщение признается подлинным\n" + "-" * 30)
        print("ОТВЕТ: ЧИСЛА РАВННЫ, ЗНАЧИТ СООБЩЕНИЕ ПОДЛИННОЕ!\n" + "-" * 30)


if __name__ == "__main__":
    main()