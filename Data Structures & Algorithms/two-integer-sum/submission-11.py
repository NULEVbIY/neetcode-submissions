class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        hash_map = {}

        for i, temp in enumerate(nums):
            hash_map[temp] = i

        for i, temp in enumerate(nums):
            need = tar - temp
            if need in hash_map and i != hash_map[need]:
                return [i, hash_map[need]]

            

                