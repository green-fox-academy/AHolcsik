# Given a string, compute recursively a new
# string where all the 'x' chars have been removed.

old = 'x'
new = ''

def x_to_y(string, old, new):
    if string == '':
        return ''
    elif string[:len(old)] == old:
        return new + x_to_y(string[len(old):], old, new)
    else:
        return string[0] + x_to_y(string[1:], old, new)

print(x_to_y('xanadu', old, new))
