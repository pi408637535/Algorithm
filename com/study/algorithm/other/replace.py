
def replace(str, old_s, new_s, times=None):

    if not times:
        times = len(str)

    i = 0
    n = 0
    c = len(old_s)
    res = []
    while i < len(str) and n < times:
        if str[i:i+c] == old_s:
            res.append( str[:i] + new_s  )
            str = str[i+c:]
            i = 0
            n += 1
        else:
            i += 1

    return "".join(res)

if __name__ == '__main__':
    s = "**aa*abc*tt*tt*"
    new_s = replace(s, '*', "TTT")
    print(new_s)
    print(s.replace("*","TTT"))
    print(s[12:])
    print(s[14:])
