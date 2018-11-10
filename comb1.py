#!/usr/bin/python3
'''EPI DP 1st'''
import pdb
import copy

def count_all_comb(N, valids):
    c = [0] * (N+1)
    c[0] = 1
    for i in range(N+1):
        for v in valids:
            if i >= v:
                c[i] += c[i-v]
    print(c)
    return c[-1]

def count_uniq_comb(N, valids):
    c = [0] * (N+1)
    c[0] = 1
    for v in valids:
        for i in range(N+1):
            if i >= v:
                c[i] += c[i-v]
    print(c)
    return c[-1]

def get_all_comb(N, valids):
    c = [0] * (N+1)
    c[0] = 1
    combs = [[] for _ in range(N+1)]
    combs[0].append([])
    for i in range(N+1):
        for v in valids:
            if i >= v:
                c[i] += c[i-v]
#                pdb.set_trace()
                for prev_comb in combs[i-v]:
                    combs[i].append(copy.deepcopy(prev_comb + [v]))
#                combs[i].extend(copy.deepcopy(combs[i-v]))
#                for x in combs[i]:
#                    x.append(v)
    for i in range(N+1):
        assert len(combs[i]) == c[i]
    print(combs)
    return combs[-1]

print(count_all_comb(12, [2,3,7]))
print(count_uniq_comb(12, [2,3,7]))
N=12
all_combs = get_all_comb(N, [2,3,7])
for comb in all_combs:
    assert sum(comb) == N, print(str(comb) + ' is not ' + str(N))
