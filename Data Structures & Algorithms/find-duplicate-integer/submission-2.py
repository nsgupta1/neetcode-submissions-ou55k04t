class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        # Form linked list and detect the cycles intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Detect the start of the cycle using floyd's cycle detection algorithm
        temp = 0
        while True:
            slow = nums[slow]
            temp = nums[temp]
            if slow == temp:
                return slow




        