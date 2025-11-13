import sys
from typing import List, Tuple, Dict, Set 

input = sys.stdin.readline 

def get_string() -> str:
    return input().strip()

def get_int() -> int:
    return int(input())

def get_ints() -> List[int]:
    return list(map(int, input().split()))

def get_floats() -> List[float]:
    return list(map(float, input().split()))

def get_list_strings() -> List[str]:
    return input().strip().split()

def get_list_ints_matrix(rows: int) -> List[List[int]]:
    matrix = []
    for _ in range(rows):
        matrix.append(get_ints())
    return matrix

def solve(nums, target):
    result_nums = {}
    for i, num in enumerate(nums):
        less_target = target - num;
        if(less_target in result_nums):
            return [result_nums[less_target], i]
        result_nums[i] = num

if __name__ == "__main__":
    nums = get_ints()
    target = get_int()
    solve([2,7,11,15], 9)