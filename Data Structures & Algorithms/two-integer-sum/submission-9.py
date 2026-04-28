class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        mas = []
        mas = [[temp, i] for i, temp in enumerate(nums)]
        mas.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            it = mas[i][0] + mas[j][0]
            if it == tar: 
                a = min(mas[i][1], mas[j][1])
                b = max(mas[i][1], mas[j][1])
                return [a, b]
            elif it > tar: 
                j -= 1
                continue
            i += 1
        return []
            

                