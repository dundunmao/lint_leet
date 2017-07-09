class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        result = [1, 1]
        for i in range(2, rowIndex+1):
            layer = []
            index = 0
            while index <= i:
                if index - 1 < 0:
                    left = 0
                else:
                    left = result[index - 1]
                if index >= len(result):
                    right = 0
                else:
                    right = result[index]
                layer.append(left + right)
                index += 1
            result = layer
        return result
if __name__ == "__main__":
    # nums = [5, 2, 6, 1]
    rowIndex = 3
    s = Solution()
    print s.getRow(rowIndex)