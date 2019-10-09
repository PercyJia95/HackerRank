**Objective**

In this challenge, we practice implementing *inheritance* and use JavaScript *prototypes* to add a new method to an existing prototype. Check out the attached *Classes* tutorial to refresh what we've learned about these topics.

**Task**

We provide the implementation for a *Rectangle* class in the editor. Perform the following tasks:

1. Add an *area* method to *Rectangle*'s prototype.

2. Create a

    

   Square

    

   class that satisfies the following:

   - It is a subclass of *Rectangle*.
   - It contains a constructor and no other methods.
   - It can use the *Rectangle* class' *area* method to print the area of a *Square* object.

Locked code in the editor tests the class and method implementations and prints the *area* values to STDOUT.

## Solution



## Study Note

#### Functional Classes

Functional Classes are using functions to simulate the behavior of classes。

1. Define a normal JavaScript function.
2. Create an object by using the `new` keyword.
3. Define properties and methods for a created object using the `this` keyword.

```
function Fruit (type) {								// Here the function Fruit is created as 
    this.type = type;								// an class, it definded its property and 
    this.color = 'unknown';							// methods by using the 'this' keyword. So
    this.getInformation = getFruitInformation;		// its two properties are 'type' and 
}													// 'color' and one method 																	// getFruitInformation is a method will
													// be defined down there.
function getFruitInformation() {
    return 'This ' + this.type + ' is ' + this.color + '.';
}

let lime = new Fruit('Mexican lime');
console.log(lime.getInformation());

lime.color = 'green';
console.log(lime.getInformation());
```

```
Output:
This Mexican lime is unknown.
This Mexican lime is green.
```

We can also define the getInformation function internally:

```
function Fruit (type) {
    this.type = type;
    this.color = 'unknown';
    this.getInformation = function() {
        return 'This ' + this.type + ' is ' + this.color + '.';
    }
}
```

#### The Prototype Property

There is a drawback of internally defining a function for a class. For example, the function internally define above for getInformation is created every time when the Fruit class is instantiated.

To fix that 