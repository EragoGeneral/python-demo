# -*- coding: utf-8 -*-

import itertools

def pi(N):
    #ns = itertools.count(1, 2)
    na = itertools.count(1,2)
    ns = list(itertools.takewhile(lambda x : x <= 2*N-1,na))
    sum = 0.0
    for i in range(N):
        sum += 4/(ns[i])*pow(-1, i)
    
    return sum
    
if __name__ == '__main__':
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    print(pi(20000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')


