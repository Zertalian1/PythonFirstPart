import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-fp", "--filepath", help="File path", default="")
args = parser.parse_args()


def is_correct_brackets(brackets_seq):
    while '()' in brackets_seq:
        brackets_seq = brackets_seq.replace('()', '')
    if not brackets_seq:
        print("Correct")
        return
    print("Incorrect")


if __name__ == '__main__':
    if len(args.filepath) != 0:
        with open(args.filepath, 'r') as fp:
            text = fp.read()
    else:
        text = input("Enter a sequence of brackets: ")
    is_correct_brackets(text)
