# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

old = 'x'
new = 'y'

def x_to_y(string, old, new):
    if string == '':
        return ''
    elif string[:len(old)] == old:
        return new + x_to_y(string[len(old):], old, new)
    else:
        return string[0] + x_to_y(string[1:], old, new)

print(x_to_y('xanadu', old, new))
