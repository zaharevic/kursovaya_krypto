alphabet = {
    "а": 1, "б": 2, "в": 3, "г": 4, "д": 5, "е": 6, "ж": 7, "з": 8,
    "и": 9, "й": 10, "к": 11, "л": 12, "м": 13, "н": 14, "о": 15, "п": 16,
    "р": 17, "с": 18, "т": 19, "у": 20, "ф": 21, "х": 22, "ц": 23, "ч": 24,
    "ш": 25, "щ": 26, "ь": 27, "ы": 28, "ъ": 29, "э": 30, "ю": 31, "я": 32
}

matrix1 = [[7, 4, 8], # Матрица
           [3, 1, 2],
           [6, 9, 5]]

def get_matrix_string(matrix, a = 1): # Подгатавливает строки для вывода матриц
    if a == 1:
        return (f'|{matrix[0][0]} {matrix[0][1]} {matrix[0][2]}|\n'
              f'|{matrix[1][0]} {matrix[1][1]} {matrix[1][2]}|\n'
              f'|{matrix[2][0]} {matrix[2][1]} {matrix[2][2]}|\n')
    else:
        return (f'|{matrix[0][0]}/{a}  {matrix[0][1]}/{a}  {matrix[0][2]}/{a}|\n'
              f'|{matrix[1][0]}/{a}  {matrix[1][1]}/{a}  {matrix[1][2]}/{a}|\n'
              f'|{matrix[2][0]}/{a}  {matrix[2][1]}/{a}  {matrix[2][2]}/{a}|\n')

def chars_to_number(chars): # Перевод буквы в число
    arr = list()
    for char in chars:
        arr.append(alphabet[char])
    return arr


def multiply_matrix_and_vector(vector, matrixx=None, determinant=1): # Умножение матрицы на вектор
    if matrixx is None:
        matrixx = matrix1
    res = list()

    for i in matrixx:
        tmp = 0
        for j in range(len(i)):
            tmp += i[j] * vector[j]
        res.append(int(tmp/determinant))
    return res


def cipher(): # Шифрование
    res = []
    t0 = "голова" # Сообщение
    print("-" * 30 + f"\nДано:\nT0: {t0}\nМатрица:\n{get_matrix_string(matrix1)}" + "-" * 30)
    print("Зашифровка:\n" + "-" * 30)

    if len(t0) == 6:
        t0_nums = chars_to_number(t0)
        print(f"1.Определим числовой эквивалент исходного слова как последовательность соответствующих порядковых номеров букв слова T0:\n"
            f"Tэ= {t0_nums}\n" + "-" * 30)

        b1 = t0_nums[0:3]
        b2 = t0_nums[3:6]
        print(f'2.Разобьем Тэ на два вектора:'
              f'B1:{b1} '
              f'B2:{b2}\n' + "-" * 30 )

        print("3.Умножим матрицы A на векторы B1 и B2")
        res.extend(a1 := multiply_matrix_and_vector(b1))
        res.extend(a2 := multiply_matrix_and_vector(b2))
        print(f"C1 = {a1}")
        print(f"C2 = {a2}\n" + "-" * 30)

        print(f'4.Зашифрованное слово запишем в виде последовательности чисел T1 = {res}\n'  + "-" * 30)
    else:
        raise ValueError("Ошибка! Длинна T0 не равна 6 символам!")
    return res


def get_determinant(matrix): # Получение определителя матрицы
    return (matrix[0][0] * matrix[1][1] * matrix[2][2] +
            matrix[0][1] * matrix[1][2] * matrix[2][0] +
            matrix[0][2] * matrix[1][0] * matrix[2][1] -
            matrix[0][2] * matrix[1][1] * matrix[2][0] -
            matrix[0][0] * matrix[1][2] * matrix[2][1] -
            matrix[0][1] * matrix[1][0] * matrix[2][2])


def algebraic_complement(matrix, row, col): # Получение алгебраического дополнения
    minor = []
    for i in range(3):
        if i != row:
            minor_row = []
            for j in range(3):
                if j != col:
                    minor_row.append(matrix[i][j])
            minor.append(minor_row)
    determinant = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
    return ((-1) ** (row + col)) * determinant


def adjugate_matrix(matrix): # Получение мартцы алгебраических дополнений
    adjugate = []
    for i in range(3):
        adjugate_row = []
        for j in range(3):
            complement = algebraic_complement(matrix, i, j)
            adjugate_row.append(complement)
        adjugate.append(adjugate_row)
    return adjugate


def transpose_matrix(matrix): # Получение транспонированой матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(matrix[i][j])
        transposed.append(transposed_row)

    return transposed


def decipher(arr): # Дешифрование
    print(f"Расшифровка:\n" + "-" * 30)
    res_arr = list()
    res = ""

    a1 = arr[0:3]
    a2 = arr[3:6]
    determinant = get_determinant(matrix1)
    print(f'1.Вычисляется определитель |A|= {determinant}\n' + "-" * 30)
    a_adj = adjugate_matrix(matrix1)
    print(f'2.Определяется присоединенная матрица A*, каждый элемент которой является алгебраическим дополнением элемента аij матрицы А:\n{get_matrix_string(a_adj)}' + "-" * 30)
    transponate_mat = transpose_matrix(a_adj)
    print(f'3. Получаем транспонированную матрицу At:\n{get_matrix_string(transponate_mat)}' + "-" * 30)
    print(f'4. Вычисляем обратную матрицу A^(-1):\n{get_matrix_string(transponate_mat, determinant)}' + "-" * 30)
    res_arr.extend(b1 := multiply_matrix_and_vector(a1, transponate_mat, determinant))
    res_arr.extend(b2 := multiply_matrix_and_vector(a2, transponate_mat, determinant))
    print(f'5.Определяются векторы В1 и В2: B1=A^(-1)C1, B2=A^(-1)C2:\nB1:{b1}\nB2:{b2}\n' + "-" * 30)
    for i in res_arr:
        for let, num in alphabet.items():
            if num == i:
                res += let
                break
    print(
        f'6.Получаем числовой эквивалент расшифрованного слова: Tэ: {res_arr}, который заменяется символами, в результате получается исходное слово: {res}\n' + "-" * 30)
    return res


def main():
    data = cipher()
    res = decipher(data)
    print(f"ОТВЕТ:\nПОЛУЧИВШИЙСЯ ШИФРОТЕКСТ: {data}\nРАСШИФРОВАННОЕ СООБЩЕНИЕ: {res}\n" + "-" * 30)


if __name__ == "__main__":
    main()
