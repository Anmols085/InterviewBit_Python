class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        out_a = list()
        size = len(A)*len(A[0])
        count = 0
        min_r, max_r = 0, len(A)
        min_c, max_c = 0, len(A[0])
        while min_r<max_r and min_c<max_c:
            for i in range(min_c, max_c):
                out_a.append(A[min_r][i])
                count += 1
            # print(out_a, min_r, max_r)
            # break
            min_r += 1
            for i in range(min_r, max_r):
                out_a.append(A[i][max_c-1])
                count += 1
            max_c -= 1
            # print(out_a)
            # break
            if max_r > min_r:
                for i in range(max_c-1, min_c-1, -1):
                    out_a.append(A[max_r-1][i])
                    count += 1
            max_r -= 1
            # print(out_a)
            # break
            if min_c < max_c:
                for i in range(max_r-1, min_r-1, -1):
                    out_a.append(A[i][min_c])
                    count += 1
            min_c += 1
            # print(out_a)
            # break
        return out_a


A = [
  [133, 241, 22, 258, 187, 150, 79, 207, 196, 401, 366, 335, 198],
  [401, 55, 260, 363, 14, 318, 178, 296, 333, 296, 45, 37, 10],
  [112, 374, 79, 12, 97, 39, 310, 223, 139, 91, 171, 95, 126]
]

sol = Solution()
print(sol.spiralOrder(A))
