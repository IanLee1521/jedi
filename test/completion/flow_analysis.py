def foo(x):
    if 1.0:
        return 1
    else:
        return ''

#? int()
foo(1)


#  Exceptions are not analyzed. So check both if branches
def try_except(x):
    try:
        if 0:
            return 1
        else:
            return ''
    except AttributeError:
        return 1.0

#? float() str()
try_except(1)


#  Exceptions are not analyzed. So check both if branches
def try_except(x):
    try:
        if 0:
            return 1
        else:
            return ''
    except AttributeError:
        return 1.0

#? float() str()
try_except(1)


# -----------------
# elif
# -----------------

def elif_flows1(x):
    if False:
        return 1
    elif True:
        return 1.0
    else:
        return ''

#? float()
elif_flows1(1)


def elif_flows2(x):
    try:
        if False:
            return 1
        elif 0:
            return 1.0
        else:
            return ''
    except ValueError:
        return set

#? str() set
elif_flows2(1)


def elif_flows3(x):
    try:
        if True:
            return 1
        elif 0:
            return 1.0
        else:
            return ''
    except ValueError:
        return set

#? int() set
elif_flows3(1)