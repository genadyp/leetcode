import pytest
from solution import Solution


@pytest.mark.parametrize(["nums", "target", "expected"],
                          [([2,7,11,15], 9, [0, 1]), ([3, 2, 4], 6, [1,2]), ([3,3], 6, [0,1])])
def test_solution(nums: list[int], target: int, expected: list[int]):
    solution = Solution()
    assert solution.twoSum(nums=nums, target=target) == expected
