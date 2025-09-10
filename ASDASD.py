def rot13(message):
    res = []
    ru_lower = [chr(el) for el in range(ord('а'), ord('я') + 1)]
    ru_upper = [chr(el) for el in range(ord('А'), ord('Я') + 1)]
    en_lower = [chr(el) for el in range(ord('a'), ord('z') + 1)]
    en_upper = [chr(el) for el in range(ord('A'), ord('Z') + 1)]

    for char in message:
        if char in en_lower:
            index = (en_lower.index(char) + step) % 26
            new_char = en_lower[index]
            res.append(new_char)
        elif char in en_upper:
            index = (en_upper.index(char) + step) % 26
            new_char = en_upper[index]
            res.append(new_char)

        elif char in ru_lower:
            index = (ru_lower.index(char) + step) % 32
            new_char = ru_lower[index]
            res.append(new_char)

        elif char in ru_upper:
            index = (ru_upper.index(char) + step) % 32
            new_char = ru_upper[index]
            res.append(new_char)
        else:
            res.append(char)

    return ''.join(res)


step = int(input('Какой шаг сдвига ? '))
text = input('Введите текст, который нужно зашифровать ')
print(rot13(text))
