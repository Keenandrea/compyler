import sys
import utils
import tokens
import scanner

# tester, or testScann
# er, will traverse th
# e specified file, ch
# aracter by character
# and return lexicogra
# phically analyzed to
# kens of the data fed
# into the scanner whi
# le it chugs along
def tester(fn):
    t = tokens.Token()
    line = 1
    with open(fn) as f:
        while True:
            t, line = scanner.driver(f,line)
            print "%s '%s' on line %d" % (t.identity, t.instance, t.location)
            if t.identity == tokens.token_ids.token_names[36]: break
            if t.identity == tokens.token_ids.token_names[35]: break