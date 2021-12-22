class Solution:
    def intToRoman(self, num):
        def get_representation(num):
            symbol_table={
                1:"I",
                5:"V",
                10:"X",
                50:"L",
                100:"C",
                500:"D",
                1000  :"M",    
            }
            if num < 4:
                return symbol_table[1]*num
            if 4 <= num <6 :
                return symbol_table[1]+symbol_table[5] if num == 4 else symbol_table[5]
            if 5< num < 9 :
                return symbol_table[5]+symbol_table[1]
            pass