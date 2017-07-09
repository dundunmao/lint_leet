class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            layer = []
            index = 0
            while index <= i:
                if index - 1 < 0:
                    left = 0
                else:
                    left = result[i - 1][index - 1]
                if index >= len(result[i - 1]):
                    right = 0
                else:
                    right = result[i - 1][index]
                layer.append(left + right)
                index += 1
            result.append(layer)
        return result


if __name__ == "__main__":
    # nums = [5, 2, 6, 1]
    numRows = 4
    s = Solution()
    print s.generate(numRows)
