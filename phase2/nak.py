from lex import *
from parse import *
import sys


def main():
    print("                  nAk COMPILER                      ")
    print("                  ============                      ")

    if len(sys.argv) != 2:
        sys.exit("ERROR: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input_exp = inputFile.read()
        # input_exp = "hello.nak"

    lexer = Lexer(input_exp)
    parser = Parser(lexer)

    parser.program()
    print("Parsing completed..!")


main()
