#!/usr/bin/python3
def multiple_returns(sentence):
    out = ()
    out += (len(sentence), )
    if len(sentence) > 0:
        out += (sentence[0], )
    else:
        out += (None, )
    return out
