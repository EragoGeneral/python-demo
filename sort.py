L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name, reverse=True)
print(L2)	


def by_sore(t):
    return t[1]
L2 = sorted(L, key=by_sore, reverse=True)
print(L2)

L3 = sorted(L, key=lambda x:x[1], reverse=True)
print(L3)	