class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, a):
        carry, count_0 = 0, 0
        for i in range(len(a)):
            if a[i] == 0:
                count_0 += 1
            else:
                break
        if count_0 == len(a):
            return [1]
        else:
            a = a[count_0:len(a)]
        a.reverse()
        if a[0] == 9:
            carry, a[i] =1, 0
        else:
            a[0] += 1
        # print(a)
        for i in range(1, len(a)):
            if carry == 0:
                break
            else:
                if a[i] == 9:
                    carry, a[i] =1, 0
                else:
                    a[i] += 1
                    carry = 0
        if carry == 1:
            a.append(1)
        a.reverse()
        return a
