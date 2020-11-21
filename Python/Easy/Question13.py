#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#Symbol       Value
#I =            1
#V =            5
#X =            10
#L =            50
#C =            100
#D =            500
#M =            1000
#For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#    I can be placed before V (5) and X (10) to make 4 and 9. 
#    X can be placed before L (50) and C (100) to make 40 and 90. 
#    C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.
#Difficulty: Easy

values = [["I",1],["V",5],["X",10],["L",50],["C",100],["D",500],["M",1000]]
options = [["IV",4],["IX",9],["XL",40],["XC",90],["CD",400],["CM",900]]
class Solution:
    def romanToInt(self, s: str) -> int:
        counter = 0
        s = s
        for index in range(0,6):
            option = options[index]
            if (s != s.replace(option[0], "")):
                counter += option[1]
                s = s.replace(option[0],"")
        for index in range(0,7):
            currValue = values[index]
            for index in range(0,len(s)):
                if s[index] == currValue[0]:
                    counter += currValue[1]
        return(counter)

#Runtime: 56 ms, faster than 15.35% of Python3 online submissions for Roman to Integer.
#Memory Usage: 14.4 MB, less than 10.73% of Python3 online submissions for Roman to Integer.
