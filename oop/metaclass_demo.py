class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass
	
L = MyList()
L.add(1)
print(L)

L2 = list()
L2.append(2)
print(L2)
#L2.add(1)