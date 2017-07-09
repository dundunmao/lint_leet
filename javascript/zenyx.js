




x = findMax(1, 123, 500, 115, 44, 88);
function findMax() {
    var i, max = 0;
    for (i = 0; i < arguments.length; i++) {
        if (arguments[i] > max) {
            max = arguments[i];
        }
    }
    return max;
}
var x = myFunction(4, 3);

(function () {
    var x = "Hello!!";      // 我将调用自己
})();
a = 5 + null
b ="5" + null
c ="5" - 1
d ="5" + 1
function myFunction(a, b) {
    return a * b;
}

////////////////////////////////////////////////////////////////////////

// Your previous JavaScript content is preserved below:
 // input = "Racecar"  output: true
 function validatePalindrome(input_str){
   //validate input
   if(typeof(input_str)!='string'){
         return false
   }
   //implement algorithm to check a palindrome
   for(var i = 0; i < input_str.length/2; i ++){
         if(input_str[i].toLowerCase() != input_str[input_str.length-i-1].toLowerCase()){
               return false
     }
   }
   //return default result
   return true
 }

 //testing
 //case 1: wrong type inpit
 console.log(validatePalindrome(3234));

 //case 2: empty string
 console.log(validatePalindrome(''));

 //case 3: normal string but not a palindrome
 console.log(validatePalindrome('sadhjk'));

 //caes 4: a palindrome string
 console.log(validatePalindrome('abcdcba'));

 //caes 5: 'Racecar' => false expected
 console.log(validatePalindrome('Racecar'));
