class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hash = {}
        for i in range(len(list1)):
            hash[list1[i]] = [i]
        for j in range(len(list2)):
            if hash.has_key(list2[j]):
                hash[list2[j]].append(j)
        result = []
        min = float('inf')
        for key,value in hash.items():
            if len(value) == 2:
                if value[0] + value[1] < min:
                    result = [key]
                    min = value[0] + value[1]
                elif value[0] + value[1] == min:
                    result.append(key)
        return result
if __name__ == "__main__":
    a = ["Shogun", "Piatti", "Tapioca Express", "Burger King", "KFC"]
    b = ["Piatti", "Shogun", "The Grill at Torrey Pines", "Burger King","Hungry Hunter Steakhouse"]
    x = Solution()
    print x.findRestaurant(a,b)