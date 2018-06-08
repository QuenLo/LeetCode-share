/**
 * @param {number[]} nums
 * @return {boolean}
 */
var checkPossibility = function(nums) {
  let adjusted = false;
  for(let i = 0; i < nums.length; i++) {
    if(nums[i] > nums[i + 1]) {
      if(adjusted) {
        return false;
      }
      if(nums[i + 2] && nums[i + 1] <= nums[i + 2]) {
        if(nums[i - 1] && (nums[i - 1] > nums[i + 2] || nums[i - 1] > nums[i + 1]) && nums[i] > nums[i + 2]) {
          return false;
        }
      } else if(!nums[i + 2]) {
        
      } else {
        // nums[i + 1] > nums[i + 2]
        return false;
      }
      adjusted = true;
    }
  }
  return true;
};
