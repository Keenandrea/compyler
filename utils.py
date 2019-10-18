# pythonic enum hardcoded after
# the built-in datatype of c-la
# nguage enum data structure. w
# hat it is doing is both simpl
# e and complex, it is creating
# a new type definition as a mo
# dule that can be passed and i
# mported throughout the program
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    names = dict((value, key) for key, value in enums.iteritems())
    enums['token_names'] = names
    return type('Enum', (), enums)
