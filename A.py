#!/usr/bin/env python3
import sys, math
from collections import deque

# ====================== FAST I/O & PARSERS ======================
def read_tokens():
    return sys.stdin.read().split()

def setup_reader():
    it = iter(read_tokens())
    ni = lambda: int(next(it))
    nf = lambda: float(next(it))
    ns = lambda: next(it)
    def nlist(n, f=int):
        return [f(next(it)) for _ in range(n)]
    def pair(f=int, g=int):
        return f(next(it)), g(next(it))
    def triple(f=int, g=int, h=int):
        return f(next(it)), g(next(it)), h(next(it))
    return ni, nf, ns, nlist, pair, triple


# ============================ SOLVE ============================
def solve():
    ni, nf, ns, nlist, pair, triple = setup_reader()
    t = ni()
    out = []
    for _ in range(t):
        n = ni()
        arr = nlist(n)
        max_so_far = arr[0]
        ops = 0
        for x in arr[1:]:
            if x < max_so_far:
                ops += 1
            else:
                max_so_far = x
        out.append(str(ops))
    print("\n".join(out))


# =========================== ENTRY ===========================
if __name__ == "__main__":
    solve()
