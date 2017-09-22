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
# (-1, 0, 1)
#
# (-1, -1, 2)


# two pointer + sort
class Solution(object):
    def threeSum(self, nums):
        result = []
        if nums is None or len(nums) <= 2:
            return result
        nums.sort()
        # 以每个nums[i]为根基，往后找两个数。如果nums[i]之前算过了，就pass
        for i in range(0, len(nums) - 2):  # 记得这里要“-2”
            if i > 0 and nums[i] == nums[i - 1]:  # 避免跟上一轮重复，i>0是保证第一轮就是i=0时不做这步
                continue
            j = i + 1  # 算i后面那段的two sum，two pointer 做法。
            k = len(nums) - 1
            while j < k:  # 每轮开始就检查是否和为0，检查完之后把j,k放到该放的位置，等到下一轮检查
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:  # 找到了
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:  # 避免重复
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:  # 避免重复
                        k -= 1
                elif sum < 0:
                    j += 1  # 如果三个数的sum比0小,j就往后窜
                else:
                    k -= 1  # 如果三个数的sum大于0,k就往前窜
        return result



# hash，不用sort
class Solution2:
    def threeSum(self, numbers):
        # write your code here
        if numbers is None or len(numbers) <= 2:
            return None
        result = []
        for i in range(len(numbers) - 2):
            group = self.sum_two(numbers[:i]+numbers[i+1:], -numbers[i])
            for ele in group:
                ele.append(numbers[i])
                ele.sort()
                tup = tuple(ele) #之所以要变tuple因为后面需要把它set了。
                result.append(tup)
        # 这里的result是以array为element的array。数字可以被set，array不可以被set。
        # 同理还有array不可以当hash的key
        # 所以这里result内的element要变成tuple
        ans = list(set(result))
        return sorted(ans)

    def sum_two(self, nums, target):
        dic = {}
        #循环nums数值，并添加映射
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dic:
                res.append([target - nums[i], nums[i]])
            dic[nums[i]] = True
        #无解的情况
        return res

#     hash + sort 超级不好想，不要看
class Solution1(object):
    def threeSum(self, numbers):
        if numbers is None or len(numbers) <=2:
            return []
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
if __name__ == '__main__':

    # A = [-7,-1,-2,-3,-4,-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-5]
    # A = [1,0,-1,-1,-1,-1,0,1,1,1]
    # A = [0,0,0,0]
    A = [-1,0, 1, 2, -1, -4]
    s = Solution_hash()
    print s.threeSum(A)