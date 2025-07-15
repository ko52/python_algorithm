import random

# ボゴソートは、使用されることはほとんど少ない
# 非効率的なソートアルゴリズム

def in_order(numbers: list) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False
    return True

def bogo_sort(numbers: list) -> list[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bogo_sort(nums))
    # print(bogo_sort([3, 2, 1, 5, 8]))