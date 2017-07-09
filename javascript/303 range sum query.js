/**
 * Created by eva on 1/20/16.
 */
function NumArray(nums) {
    this.sums = [];
    var sum = 0;
    for (var i = 0; i < nums.length; i++) {
        sum += nums[i];
        this.sums.push(sum);
    }
}
//prototype用来再加一个function进去
NumArray.prototype.sumRange = function(i, j) {
    return this.sums[j] - (i > 0 ? this.sums[i - 1] : 0);
};