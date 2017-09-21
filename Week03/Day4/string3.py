# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".old = 'x'
# qwer => q*w*e*r

new = '*'

def x_to_y(string, new):
    if string == '':
        return ''
    elif len(string) == 1:
        return string [0]
    else:
        return string[0] + new + x_to_y(string[1:], new)

print(x_to_y('xanadu', new))
