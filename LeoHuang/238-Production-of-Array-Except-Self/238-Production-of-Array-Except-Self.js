/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  // make the production of all items in nums
  let totalProduct = nums.reduce(function(total, num) {
    return total * num;
  });
  // check whether nums contains 0 or not
  if(totalProduct) {
    return nums.map(num => {
      return totalProduction / num;
    });
  } else {
    // if nums contains 0 
    // use methods not in O(n)
    totalProduct = [];
    nums.forEach(function(currentValue, index, arr) {
      totalProduction.push(arr.filter(function(item, idx) {
        return idx != index;
      }).reduce(function(total, num) {
        return total * num;
      }));
    });
    return totalProduct;
  }
};
