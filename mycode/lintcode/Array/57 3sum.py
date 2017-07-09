# coding:utf-8
# 给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。
#
#  注意事项
#
# 在三元组(a, b, c)，要求a <= b <= c。
#
# 结果不能包含重复的三元组。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：
#
# (-1, 0, 1)
#
# (-1, -1, 2)
class Solution:
    def threeSum(self, numbers):
        result = []
        if numbers is None or len(numbers) <=2:
            return result
        numbers.sort()
        for i in range(0,len(numbers)-2):
            if i > 0 and numbers[i] == numbers[i-1]: # avoid duplication
                continue
            j = i + 1                          # 用i来遍历,j为i下一个数,k为排尾的数
            k = len(numbers) - 1
            while j < k:
                if j > i + 1 and numbers[j] == numbers[j-1]: # avoid duplication
                    j += 1
                    continue
                if k < len(numbers) - 1 and numbers[k] == numbers[k+1]: # avoid duplication
                    k -= 1
                    continue
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    result.append([numbers[i], numbers[j], numbers[k]])
                if numbers[i] + numbers[j] + numbers[k] < 0:
                    j += 1 #如果三个数的sum比0小,j就往后窜
                else:
                    k -= 1 #如果三个数的sum比0大,k就往前窜

        return result


class Solution_hash:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) <=2:
            return None
        numbers.sort()
        result = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]: # avoid i duplication
                continue
            dic = {}
            for j in range(i+1, len(numbers)):
                if -numbers[i]-numbers[j] in dic:
                    # 避免这一轮的数对应的那个k-v pair里的value不是上一轮的的j
                    # 意思是如果两个重复的数都在里面,[-4,2,2,2,10],第一个'2'存dic里,第二个'2'符合条件,要保留,只有第三个2才需要skip
                    if j>i+1 and numbers[j] == numbers[j-1] and dic[-numbers[i]-numbers[j]]!=(j-1):
                        continue
                    result.append([numbers[i],-numbers[i]-numbers[j],numbers[j]])
                else:
                    dic[numbers[j]] = j
        return result

class Solution2:
    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) <= 2:
            return None
        result = []
        for i in range(len(numbers) - 2):
            group = self.sum_two(numbers, -numbers[i])
            if group is not None:
                group.append(numbers[i])
                if len(set(group)) == len(group):
                    result.append(group)
        return result


    def sum_two(self, numbers, target):
        dic = {}
        # 循环nums数值，并添加映射
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i]+ numbers[j]> target:
                j-=1
            elif numbers[i]+ numbers[j] < target:
                i+=1
            else:
                return [numbers[i], numbers[j]]
        # 无解的情况
        return None
if __name__ == '__main__':


    list = [-1,1,0]
    s = Solution2()
    print s.threeSum(list)