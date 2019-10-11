import os, sys
import tokens
import tester

"""              ws     c     d     =     <     >    <=    >=    ==     :     +     -     *     /     %     .     (     )     ,     {     }     ;     [     ]   eof    up    """
fsa_table = [ [   0,    1,    2,    3,    4,    5,    6,    7,    8,    9,   10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20,   21,   22,   23,   -1,   -2],
              [1000,    1,    1, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,    1], # id
              [1001, 1001,    2, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001, 1001], # int
              [1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002, 1002], # =
              [1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003, 1003], # <
              [1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004, 1004], # >
              [1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005, 1005], # <=
              [1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006], # >=
              [1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007], # ==
              [1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008, 1008], # :
              [1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009, 1009], # +
              [1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010, 1010], # -
              [1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011, 1011], # *
              [1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012, 1012], # /
              [1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013, 1013], # %
              [1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014, 1014], # .
              [1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015, 1015], # (
              [1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016, 1016], # )
              [1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017, 1017], # ,
              [1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018, 1018], # {
              [1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019, 1019], # }
              [1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020, 1020], # ;
              [1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021, 1021], # [
              [1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022, 1022], # ]
            ]

final_states = {
    1000 : 'ID_tk',
    1001 : 'INT_tk',
    1002 : 'ASSIGN_tk',
    1003 : 'LT_tk',
    1004 : 'GT_tk',
    1005 : 'LT_EQ_tk',
    1006 : 'GT_EQ_tk',
    1007 : 'EQ_tk',
    1008 : 'COLON_tk',
    1009 : 'PLUS_tk',
    1010 : 'MINUS_tk',
    1011 : 'ASTERISK_tk',
    1012 : 'FSLASH_tk',
    1013 : 'MODULO_tk',
    1014 : 'DOT_tk',
    1015 : 'LPAREN_tk',
    1016 : 'RPAREN_tk',
    1017 : 'COMMA_tk',
    1018 : 'LBRACE_tk',
    1019 : 'RBRACE_tk',
    1020 : 'SEMICOLON_tk',
    1021 : 'LBRACKET_tk',
    1022 : 'RBRACKET_tk',
    -1   : 'EOF_tk',
}

keywords = {
    'start'   : 'START_tk',
    'stop'    : 'STOP_tk',
    'iter'    : 'ITER_tk',
    'void'    : 'VOID_tk',
    'var'     : 'VAR_tk',
    'return'  : 'RETURN_tk',
    'in'      : 'IN_tk',
    'out'     : 'OUT_tk',
    'program' : 'PROGRAM_tk',
    'cond'    : 'COND_tk',
    'then'    : 'THEN_tk',
    'let'     : 'LET_tk',
}

symbols = {
    '='  : 2,
    '<'  : 3,
    '>'  : 4,
    '<=' : 5,
    '>=' : 6,
    '==' : 7,
    ':'  : 8,
    '+'  : 9,
    '-'  : 10,
    '*'  : 11,
    '/'  : 12,
    '%'  : 13,
    '.'  : 14,
    '('  : 15,
    ')'  : 16,
    ','  : 17,
    '{'  : 18,
    '}'  : 19,
    ';'  : 20,
    '['  : 21,
    ']'  : 22,
}

def get_tokens(state, lexe, lineno):
    state_token = tokens.Token()
    s_value = final_states.get(state)
    k_value = keywords.get(lexe)
    if s_value != None:
        state_token.identity = s_value
        state_token.instance = lexe
        state_token.location = lineno
    if k_value != None:
        state_token.identity = k_value
    return state_token

def get_symbol(datum):
    value = symbols.get(datum)
    if value == None:
        return -2
    else:
        return value 

def get_column(datum):
    if datum.isalpha():
        if datum.isupper():
            return 25
        return 1
    elif datum.isdigit():
        return 2
    elif datum.isspace():
        return 0
    else:
        get_symbol(datum)


def filter(fn, lineno):
    with open(fn) as fp:
        while True:
            datum = fp.read(1)
            return datum, lineno
            if not datum:
                print "%s,'%s',%d" % (tokens.token_ids.token_names[35],'eof',lineno)
            elif datum == '\n':
                lineno += lineno
            elif datum == '#':
                while True:
                    datum = fp.read(1)
                    if datum == '\n':
                        lineno += lineno
                        break

def driver(fn, lineno):
    active_state = 0
    future_state = 0
    unit = ' '
    lexe = ""
    with open(fn) as fp:
        while True:
            datum = fp.read(1)
            return datum, lineno
            if not datum:
                print "%s,'%s',%d" % (tokens.token_ids.token_names[35],'eof',lineno)
            elif datum == '\n':
                lineno += lineno
            elif datum == '#':
                while True:
                    datum = fp.read(1)
                    if datum == '\n':
                        lineno += lineno
                        break
    while active_state < 1000 and active_state > -1:


        fsa_column = get_column(datum)
        if fsa_column == -2:
            print "SCANNER ERROR: Illegal character '%s' on line %d" % (datum,lineno) 
            return tokens.Token(tokens.token_ids.token_names[36],'bad token',lineno)
        future_state = fsa_table[active_state][fsa_column]
        print future_state

        if future_state >= 1000 or future_state == -1 or future_state == -2:
            if future_state == -1:
                return tokens.Token(tokens.token_ids.token_names[35],'eof',lineno)
            if future_state == -2:
                print "SCANNER ERROR: Illegal character '%s' on line %d" % (datum,lineno) 
                return tokens.Token(tokens.token_ids.token_names[36],'illegal ID',lineno)
            return get_tokens(future_state, lexe, lineno)
        else:
            if unit.isspace() == False:
                lexe += unit
            if len(lexe) > 7:
                print "SCANNER ERROR: Illegal keyword '%s' on line %d" % (lexe,lineno) 
                return tokens.Token(tokens.token_ids.token_names[36],'illegal size',lineno)
            active_state = future_state
    return tokens.Token(tokens.token_ids.token_names[36],'scanner failed to return token',lineno)