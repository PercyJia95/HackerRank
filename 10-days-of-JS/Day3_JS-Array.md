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

**Sample Input **

```
5
2 3 6 6 5
```

**Sample Output **

```
5
```

**Explanation **

Given the array *nums* = [2,3,6,6,5] , we see that the largest value in the array is 6 and the second largest value is 5. Thus, we return 5 as our answer.

### Solution:

```
function getSecondLargest(nums) {
    let length = nums.length;
    let round_counter = 0;
    let largest = 0;
    let second_largest = 0;
    for (let e of nums) {
        //console.log("e: "+ e + "\n");
        if (e > largest) {
            second_largest = largest;
            largest = e;
            //console.log(second_largest + "\n");
        } else if (e > second_largest && e != largest) {
            second_largest = e;
            //console.log(second_largest + "\n")
        }
    }
    return second_largest;
}
```

### Study Note

The JavaScript Array object is a global object that is used in the construction of arrays; which are high-level, list-like objects.

###### *Create an array*: `var a = ['first', 'second'];`

###### *Access an array item, index into the array*: 

```
let a = ['first','second'];
let first = a[0];
let last = a[a.length-1];
```

###### *Append to the end of an array*: `a.push('third')`;

###### *Add to the front of an array*: `a.unshift('zero')`;

###### *Get and remove an item*:

*from the end of array* `let removed = a.pop()     //pop from the end`  

*from the front of array* `let removed = a.shift()   //shift left to remove the front item` 

###### *Get index of an item in the array* 

```javascript
use function indexOf() of the array object: let position = a.indexOf('second');
```

###### *Remove an item by the index indicated* 

##### <u>important</u>

```
var a = ['first', 'second', 'third', 'fourth', 'fifth'];
let position = 1;
let elementsToRemove = 2;

a.splice(position, elementsToRemove); //"position" tell the index of the array for which the  
									  // the removing action starts.
									  //"elementsToRemove" tell How many elements are to be 
									  //removed.

console.log('Modified Array:', a);
```

```
Output:
Modified Array: [ 'first', 'fourth', 'fifth' ]
```



###### *Copy an array*:

```
var a = ['first', 'second', 'third', 'fourth'];

// Shallow copy array 'a' into a new object
let b = a.slice();
```

**SO, What is shallow copy ???**

###### *Sort an array* 

into an asceding order

```
var a = array; 	
a.sort(); 		//This would sort the array into ascending lexicographical order using a
			    //built-in
			    //Ascending lexicographical order is the left smaller ascii value of
			    //word always get a first placement ahead of other larger ones
For example
var a = ['c', 'a', 'd', 'b', 'aa'];
var b = [9, 2, 13, 7, 1, 12, 123];
would sort into the order
a: [ 'a', 'aa', 'b', 'c', 'd' ]
b: [ 1, 12, 123, 13, 2, 7, 9 ]
```

into a desceding order 

**??? a.sort((x, y) => x < y); ????** **descending lexicographical**

```
var a = ['c', 'a', 'd', 'b', 'aa'];

// Sort in descending lexicographical order using a compare arrow function
a.sort((x, y) => x < y); ????

console.log('a:', a);
```

```
Output:
a: [ 'd', 'c', 'b', 'aa', 'a' ]
```

###### *Iterate over an array*

We can use the *for…of* statement to iterate over an array.

This type of statement creates a loop that lets you iterate over iterable objects such as *Array*, *String*, *Set*, and *Map*.

```
var a = ['first', 'second', 'third', 'fourth'];

for (let e of a) {
    console.log('e:', e);
}
```

```
Output:
e: first
e: second
e: third
e: fourth
```

###### *Foreach function applying to array*:

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

###### 