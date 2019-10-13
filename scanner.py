import os, sys
import tokens
import tester

"""                      ws     c     d     =     <     >    <=    >=    ==     :     +     -     *     /     %     .     (     )     ,     {     }     ;     [     ]   eof    unk """
fsa_table         = [ [   0,    1,    2,    3,    4,    5,    6,    7,    8,    9,   10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20,   21,   22,   23,   -1,   -2],
                      [1000,    1,    1, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000], # id
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

def get_tokens(state, literal, line):
    state_token = tokens.Token()
    for i in xrange(0,24):
        if state == 1:
           for k in keywords:
               if keywords.has_key(literal):
                   state_token.identity = keywords.get(k)
                   state_token.instance = literal
                   state_token.location = line
        if final_states.has_key(state):
            state_index = final_states.get(state)
            state_token.identity = state_index
            state_token.instance = literal
            state_token.location = line
    return state_token

def get_column(datum):
    value = symbols.get(datum)
    if symbols.has_key(datum):
        return value
    elif datum.isalpha():
        return 1
    elif datum.isdigit():
        return 2
    elif datum.isspace():
        return 0
    else:
        return 24

def driver(f):
    this_state = 0
    next_state = 0
    tk = tokens.Token()
    literal = ""
    line = 1

    while this_state < 1000 and this_state > -1:
        fpos = f.tell()
        datum = f.read(1)
        if datum == '#':
            while True:
                datum = f.read(1)
                if datum == '\n':
                    line = line + 1
                    break
        fsa_state = get_column(datum)
        if fsa_state == -2:
            print "SCANNER ERROR: Illegal character '%s' on line %d" % (datum,line) 
            return tokens.Token(tokens.token_ids.token_names[36],'bad token',line)
        next_state = fsa_table[this_state][fsa_state]
        if next_state >= 1000 or next_state == -1 or next_state == -2:
            if datum == '\n':
                line = line + 1
            if next_state >= 1000:
                tk = get_tokens(next_state, literal, line)
                tk.location = line
                f.seek(fpos, os.SEEK_SET)
                return tk                
            if next_state == -1:
                tk.identity = tokens.token_ids.token_names[35]
                tk.instance = 'EOF'
                tk.location = line
                return tk
            if next_state == -2:
                print "SCANNER ERROR: Illegal character '%s' on line %d" % (datum,line)
                tk.identity = tokens.token_ids.token_names[36]
                tk.instance = 'bad token'
                tk.location = line 
                return tk
        else:
            unit = datum
            if unit.isspace() == False:
                literal += unit
            if len(literal) > 7:
                print "SCANNER ERROR: Illegal keyword '%s' on line %d" % (datum,line) 
                return tokens.Token(tokens.token_ids.token_names[36],'illegal size',line)
            this_state = next_state
    return tokens.Token(tokens.token_ids.token_names[36],'bad token',line)