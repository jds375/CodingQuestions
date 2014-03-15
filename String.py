"""
Question: Substring Write a program to determine whether an input string x is 
a substring of another input string y. (For example, "bat" is a substring 
of "abate", but not of "beat".) 
"""

def hasSubstring(x, y):
    t = buildBacktrackArray(x)
    m = 0
    i = 0
    while (m + i < len(y)):
        if x[i] == y[m + i]:
            if i == len(x) - 1:
                return True
            i += 1
        else:
            m += i - t[i]
            if t[i] > -1: 
                i = t[i]
            else:
                i = 0
    return False

def buildBacktrackArray(x):
    t = [None] * len(x);
    t[0] = -1
    t[1] = 0
    iT = 2
    iW = 0
    while (iT < len(x)):
        if x[iT - 1] == x[iW]:
            iW += 1
            t[iT] = iW;
            iT += 1
        elif iW > 0:
            iW = t[iW]
        else:
            t[iT] = 0
            iT += 1
    return t
