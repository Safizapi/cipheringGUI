with open("alphabet", "r", encoding="utf-8") as file:
    alph = list(file.readlines())

    cipher_dict = dict(zip(alph[0], alph[1]))
    decipher_dict = dict(zip(alph[1], alph[0]))


def encode(text: str) -> str:
    result = ""

    for symbol in text:
        if not (symbol in alph[0]) and symbol.isascii():
            result += symbol
        elif not (symbol in alph[0]) and not (symbol.isascii()):
            return "Error: unexpected symbol"
        else:
            result += cipher_dict[symbol]

    return result


def decode(text: str) -> str:
    result = ""

    for symbol in text:
        if not (symbol in alph[1]) and symbol.isascii():
            result += symbol
        elif not (symbol in alph[1]) and not (symbol.isascii()):
            return "Error: unexpected symbol"
        else:
            result += decipher_dict[symbol]

    return result
