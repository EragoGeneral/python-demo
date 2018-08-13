from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            # last为True是LIFO,即为堆栈，反之是FIFO，即为队列。
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set: ', (key, value))
        else:
            print('add: ', (key, value))

        OrderedDict.__setitem__(self, key, value) 
		
		
if __name__=='__main__':
    luod = LastUpdatedOrderedDict(3)
    luod['x'] = 1
    luod['x'] = 2
    luod['a'] = 1
    luod['b'] = 2
    luod['c'] = 3