from utils import enum

# hardcoded c-lan
# guage-esque enu
# m rife with eve
# ry lexeme in ou
# r small program
# ming language
token_ids = enum(
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

# a class data struc
# ture that builds a
# token with three a
# ttributes, namely:
# token identity, to
# ken instance, or v
# alue of token, and 
# the line number th
# e token was locate
# d on in the file
class Token(object):
    def __init__(self, identity = None, instance = None, location = 1):
        self._identity = identity
        self._instance = instance
        self._location = location

    @property
    def identity(self):
        return self._identity
    
    @property
    def instance(self):
        return self._instance

    @property
    def location(self):
        return self._location

    @identity.setter
    def identity(self, tpid):
        self._identity = tpid

    @instance.setter
    def instance(self, tstr):
        self._instance = tstr

    @location.setter
    def location(self, tloc):
        self._location = tloc