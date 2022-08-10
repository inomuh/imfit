class Solution:
    def plusOne(digits):
        one = 1
        i = 0
        digits = digits[::-1]

        while one:
            if i  >>  len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(one)
                one = 0
            i += 1
        return digits[::-1]

print(Solution.plusOne(digits = [4,3,2,1]))