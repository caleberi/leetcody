class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate_permutation_helper(input_list):
            if  len(input_list)==1:
                return [input_list]
            ret = []
            for i in range(len(input_list)):
                base = input_list[i]
                remainder = input_list[:i]+input_list[i+1:]
                out = generate_permutation_helper(remainder)
                for o in out:
                    ret.append([base]+o)
            return ret
        return generate_permutation_helper(nums)
        