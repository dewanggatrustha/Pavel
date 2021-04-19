# Pengimportan Library sly
from sly import Lexer

# Membuat kelas Lexer
class PavelLexer(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

# Pendifinisian tokens
    IF = r'NAKNU'
    PRINT = r'TOKKE'
    THEN = r'TRUSTO'
    ELSE = r'NEKRA'
    FOR = r'NGGOKI'
    FUN = r'NEK'
    TO = r'NGASI'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = PavelLexer()
    env = {}
    while True:
        try:
            text = input('Pavel >> ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)