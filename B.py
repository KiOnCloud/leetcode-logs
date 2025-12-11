import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()

        ones = [i for i, c in enumerate(s) if c == '1']
        if len(ones) == n:
            print(0)
            continue

        ans = 0

        for i, c in enumerate(s):
            if c == '0':
                import bisect
                pos = bisect.bisect_left(ones, i)
                right = ones[pos] - i if pos < len(ones) else float('inf')
                left = i - ones[pos-1] if pos > 0 else i - ones[-1] + n
                d = min(right, left)
                ans = max(ans, d)
        print(ans)


if __name__ == "__main__":
    solve()
