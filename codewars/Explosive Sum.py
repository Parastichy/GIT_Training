import numpy

def exp_sum(n):
    v = numpy.zeros(n + 1, dtype=int)
    v[0] = 1
    for x in range(1, n):
        b = numpy.zeros(n + 1, dtype=int)
        b[:] = v[:]
        for d in range(x, n + 1, x):
            b[d:] += v[:n - d + 1]
        v = b
    return v[n] + 1

if __name__ == '__main__':
    print(exp_sum(50))  # 204226
    print(exp_sum(80))  # 15796476
    print(exp_sum(100)) # 190569292