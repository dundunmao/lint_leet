/**
 * Created by eva on 1/20/16.
 */
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var obj = {};
    for(var i = 0; i < nums.length; i++){
        obj[nums[i]] = obj[nums[i]] + 1 || 1;
        if(obj[nums[i]] > 1) return true;
    }
    return false;
};
nums = [1,2,3,3,4,5]
a = containsDuplicate(nums)
console.log(a);