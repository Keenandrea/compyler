import sys
import utils
import tokens
import scanner

# token_types = [
#     'START_tk',
#     'STOP_tk',
#     'ITER_tk',
#     'VOID_tk',
#     'VAR_tk',
#     'RETURN_tk',
#     'IN_tk',
#     'OUT_tk',
#     'PROGRAM_tk',
#     'COND_tk',
#     'THEN_tk',
#     'LET_tk',
#     'ASSIGN_tk',
#     'LT_tk',
#     'GT_tk',
#     'LT_EQ_tk',
#     'GT_EQ_tk',
#     'EQ_tk',
#     'COLON_tk',
#     'PLUS_tk',
#     'MINUS_tk',
#     'ASTERISK_tk',
#     'FSLASH_tk',
#     'MODULO_tk',
#     'DOT_tk',
#     'LPAREN_tk',
#     'RPAREN_tk',
#     'COMMA_tk',
#     'LBRACE_tk',
#     'RBRACE_tk',
#     'SEMICOLON_tk',
#     'LBRACKET_tk',
#     'RBRACKET_tk',
#     'ID_tk',
#     'INT_tk',
#     'EOF_tk',
#     'ERROR_tk',
# ]

def tester(fn):
    t = tokens.Token()
    with open(fn) as f:
        while True:
            t = scanner.driver(f)
            if t.identity == tokens.token_ids.token_names[35]: break
            print "%s %s %d" % (t.identity, t.instance, t.location)