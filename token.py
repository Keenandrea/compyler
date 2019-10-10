from utils import enum

token_identities = enum(
    'START_tk',
    'STOP_tk',
    'ITER_tk',
    'VOID_tk',
    'VAR_tk',
    'RETURN_tk',
    'IN_tk',
    'OUT_tk',
    'PROGRAM_tk',
    'COND_tk',
    'THEN_tk',
    'LET_tk',
    'ASSIGN_tk',
    'LT_tk',
    'GT_tk',
    'LT_EQ_tk',
    'GT_EQ_tk',
    'EQ_tk',
    'COLON_tk',
    'PLUS_tk',
    'MINUS_tk',
    'ASTERISK_tk',
    'FSLASH_tk',
    'MODULO_tk',
    'DOT_tk',
    'LPAREN_tk',
    'RPAREN_tk',
    'COMMA_tk',
    'LBRACE_tk',
    'RBRACE_tk',
    'SEMICOLON_tk',
    'LBRACKET_tk',
    'RBRACKET_tk',
    'ID_tk',
    'INT_tk',
    'EOF_tk',
    'ERROR_tk',
)

class Token:
    def __init__(self, tokenIdentity = None, tokenInstance = None, tokenLocation = 1):
        self._tokenIdentity = tokenIdentity
        self._tokenInstance = tokenInstance
        self._tokenLocation = tokenLocation

    @property
    def tokenIdentity(self):
        return self._tokenIdentity
    
    @property
    def tokenInstance(self):
        return self._tokenInstance

    @property
    def tokenLocation(self):
        return self._tokenLocation

    @tokenIdentity.setter
    def tokenIdentity(self, tpid):
        self._tokenIdentity = tpid

    @tokenInstance.setter
    def tokenInstance(self, tstr):
        self._tokenInstance = tstr

    @tokenLocation.setter
    def tokenLocation(self, tloc):
        self._tokenLocation = tloc