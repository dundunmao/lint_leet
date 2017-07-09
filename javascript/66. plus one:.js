/**
 * Created by eva on 1/20/16.
 */
var plusOne = function(digits) {
    var sum = 0;
    var i =0;
    while (digits.length> 0){
        sum += digits.pop()*Math.pow(10,i);
        i++
    }
    sum +=1;

    newList = [];
    for (var j in sum.toString()){
    newList.push(parseInt(sum.toString()[j]));
    }
    return newList;
};
digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3];
a = plusOne(digits)
console.log(a)

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