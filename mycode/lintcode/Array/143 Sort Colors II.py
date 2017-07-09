# -*- encoding: utf-8 -*-
# 题目：给定一个有n个对象（包括k种不同的颜色，并按照1到k进行编号）的数组，将对象进行分类使相同颜色的对象相邻，并按照1,2，...k的顺序进行排序。
# You are not suppose to use the library's sort function for this problem.
# k <= n
# eg：给出colors=[3, 2, 2, 1, 4]，k=4, 你的代码应该在原地操作使得数组变成[1, 2, 2, 3, 4]
#解题：每次求array里的min和max, 然后扫描,所有的min放左边,max放右边,然后缩小array,然后重复以上
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        count = 0
        start = 0
        end = len(colors) - 1
        while count < k:
            mini = float('inf')
            maxi = float('-inf')
            for i in range(start, end+1):
                mini = min(mini, colors[i])
                maxi = max(maxi, colors[i])
            left = start
            right = end
            cur = left
            # cur从left走到right，如果找到了mini或maxi就跟left或right互换，保证所有的mini在左，所有maxi在右
            # 这里跟625partition array ii 很像
            while cur <= right:
                if colors[cur] == mini:
                    colors[left], colors[cur] = colors[cur], colors[left]
                    cur += 1
                    left += 1
                elif colors[cur] == maxi:
                    colors[cur], colors[right] = colors[right], colors[cur]
                    right -= 1
                else:
                    cur += 1
            #除掉了两个数，一个k个数。当所有数都除掉时，就跳出循环
            count += 2
            # 找到新的一段
            start = left
            end = right

#超时，并且k这个参数没用上
class Solution_self:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here
        array = colors
        i = 0
        j = len(colors) - 1
        round = 0
        while i < j:
            index1 = self.min_index(array, round)
            colors[i], colors[index1] = colors[index1], colors[i]

            array = colors[i:j + 1]
            index2 = self.max_index(array, round)
            colors[j], colors[index2] = colors[index2], colors[j]
            i += 1
            j -= 1
            array = colors[i:j + 1]
            round += 1
        return colors
    def min_index(self, array, round):
        index = 0
        flag = array[0]
        for i in range(1, len(array)):
            if array[i] < flag:
                flag = array[i]
                index = i
        return index + round

    def max_index(self, array, round):
        index = 0
        flag = array[0]
        for i in range(1, len(array)):
            if array[i] > flag:
                flag = array[i]
                index = i
        return index + round
if __name__ == "__main__":
    A = [3,2,3,3,4,3,3,2,4,4,1,2,1,1,1,3,4,3,4,2]
    target = 4

    s = Solution_self()

    print s.sortColors2(A, target)

