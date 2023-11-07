import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-fp", "--filepath", help="File path", default="")
parser.add_argument("-l", "--language", help="Language", default="")
parser.add_argument("-o", "--offset", help="Offset", default="", type=int)
args = parser.parse_args()


def caesar_cipher(original_text, offset, language):
    match language:
        case "russian":
            dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        case "english":
            dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        case _:
            print("Unsupported language, choose between Russian and English")
            exit(0)
    res, n = [], ""
    for i, letter in enumerate(original_text, start=1):
        if not letter.isalpha():
            res.append(letter)
            continue
        if letter.isupper():
            n = dictionary_upper
        else:
            n = dictionary

        place = n.find(letter)
        if place == -1:
            print("Error of the declared and actual languages in %d".format(i))
        if 0 <= place + offset < len(n):
            res.append(n[place + offset])
        elif place + offset >= len(n):
            res.append(n[(place + offset) % (len(n))])
        elif place + offset < 0:
            res.append(n[(place + offset) % len(n)])

    return ''.join(res)


if __name__ == '__main__':
    if len(args.filepath) != 0:
        with open(args.filepath, encoding = 'utf-8', mode = 'r') as fp:
            text = fp.read()
        out = caesar_cipher(text, args.offset, args.language.lower())
        with open("files/cesar_out.txt", encoding = 'utf-8', mode = 'w') as fp:
            fp.write(out)
        print(out)
    else:
        print("Enter a file path with -fp argument")
