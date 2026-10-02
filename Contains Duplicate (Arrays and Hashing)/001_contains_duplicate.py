"""Contains Duplicate (NeetCode #1): one pass with a set, O(n) time, O(n) space."""


def has_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    assert has_duplicate([1, 2, 3, 1]) is True
    assert has_duplicate([1, 2, 3]) is False
    assert has_duplicate([]) is False
    assert has_duplicate([7, 7]) is True
    print("all tests pass")
