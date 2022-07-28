from lex import *


def main():
    input_exp = "IF+-123 9.8654*/"
    lexer = Lexer(input_exp)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()
