def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    names = dict((value, key) for key, value in enums.iteritems())
    enums['token_names'] = names
    return type('Enum', (), enums)
