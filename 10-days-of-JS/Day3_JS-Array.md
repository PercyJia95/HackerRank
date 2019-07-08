**Objective**

In this challenge, we learn about *Arrays*.

**Task**

Complete the *getSecondLargest* function in the editor below. It has one parameter: an array, *nums* , of  *n* numbers. The function must find and return the second largest number in *nums*.

**Input Format**

Locked stub code in the editor reads the following input from stdin and passes it to the function: 

The first line contains an integer, *n*, denoting the size of the *nums* array. 
The second line contains *n* space-separated numbers describing the elements in *nums*.

**Constraints**

- 1 ≤ n ≤ 10
- 0 ≤ numsi ≤ 100, where numsi is the number at index .
- The numbers in nums are not distinct.

**Output Format**

Return the value of the second largest number in the  array.

**Sample Input 0**

```
5
2 3 6 6 5
```

**Sample Output 0**

```
5
```

**Explanation 0**

Given the array = [2,3,6,6,5] , we see that the largest value in the array is 6 and the second largest value is 5. Thus, we return 5 as our answer.

### Study Note

The JavaScript Array object is a global object that is used in the construction of arrays; which are high-level, list-like objects.

*create an array*: `var a = ['first', 'second'];`

*access an array item, index into the array*: 

```
let a = ['first','second'];
let first = a[0];
let last = a[a.length-1];
```

*foreach function applying to array*:

```
var a = ['first', 'second'];
a.foreach(function(e,i,array)){
    //'i' is the index
    //'e' is the element
    console.log(i+' '+e);
}

Output:
0 first
1 second
```

*append to the end of an array*: `a.push('third')`;

*add to the front of an array*: `a.unshift('zero')`;

get and remove an item*:

*from the end of array* `let removed = a.pop()`  <!--(pop from the end)-->

*from the front of array* `let removed = a.shift()` <!--shift left to remove the front item-->

*Get index of an item in the array* 

```javascript
use function indexOf() of the array object: let position = a.indexOf('second');
```

*remove an item by the index indicated*

### Solution:



