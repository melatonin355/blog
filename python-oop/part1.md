OOP Python
===


Think of an object as a container.
- contains data (state)
- contans functions (behavior)

```
______________________________________
/                                      \
|         Object: my_car               |
|                                      |
|         State:                       |
|           - brand: Ferrari 
 model = 599

acceralte 
brake 
steer 
```
## dot notation


```
           _________________
          |    my_car       |
          |_________________|
          | brand : Ferrari |
          | model : 599     |
          |_________________|
  
  Dot notation:    my_car.brand -> Ferrari
  
  Method call:     my_car.accelerate(10)
```

- Creating objects
- define and set state
- define and implement behvaior


# Notes on Python Class Attributes and getattr()

In Python, a class is a blueprint for creating objects that have certain attributes and methods. A class can have both class-level attributes and instance-level attributes. 

## Class Attributes
Class attributes are defined outside of any methods within a class, and they are shared by all instances of that class. 

In the code provided, `MyClass` is a Python class with two class-level attributes: `language` and `version`. `language` is set to `'python'` and `version` is set to `'3.6'`. 

## Accessing Class Attributes
To access class attributes, you can use dot notation or the built-in function `getattr()`. 

Dot notation is used to access attributes directly from the class, like so:
```
print(MyClass.language) # output: python
```

To use `getattr()`, pass in the name of the class and the name of the attribute you want to access:
```
print(getattr(MyClass, 'version')) # output: 3.6
```

If you try to access an attribute that does not exist using `getattr()`, you can specify a default value to be returned:
```
print(getattr(MyClass, 'version2', 'does not exist')) # output: does not exist
```

## Using __name__ to Access Class Name
The double underscore method `__name__` is a built-in attribute of Python classes. It returns the name of the class as a string. You can use it like so:
```
print(MyClass.__name__) # output: MyClass
```

This can be useful if you want to dynamically access a class by its name.


