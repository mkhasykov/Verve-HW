from typing import List


def get_prod_two(nums: List[int], target: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    diffs = set()
    for num in nums:
        diff = target - num
        if diff in diffs:
            return num * diff
        else:
            diffs.add(num)

            
def get_prod_three(nums: List[int], target: int) -> int:
    """
    Time complexity: O(n**2)
    Space complexity: O(n)
    
    At each step we solve previous problem
    with corresponding target sum
    """
    for i, num in enumerate(nums):
        prod_two = get_prod_two(nums[i + 1:], target - num)
        if prod_two:
            return num * prod_two          


def read_data(data_path: str) -> List[int]:
    with open(data_path, "r") as f:
        data = [int(str_) for str_ in f.readlines()]
    return data


if __name__ == "__main__":
    DATA_PATH = "./dataset.txt"
    nums = read_data(DATA_PATH)
    print(f"part one answer: {get_prod_two(nums, 2020)}")
    print(f"part two answer: {get_prod_three(nums, 2020)}")
