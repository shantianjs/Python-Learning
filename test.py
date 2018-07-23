
def tra(st):
    res = st.split(' ')
    res = map(int, res)
    return list(res)


n = [tra('13 4 8 14 1'),
     tra('9 6 3 7 21'),
     tra('5 12 17 9 3')]

[print(i) for i in n[1]]
