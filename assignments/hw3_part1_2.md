Homework Assignment 3:

Part 1:

1. Person refers to a class variable. It has global scope.

2. person is an object that is an instance of the class Person. It has global scope. 

3. surname is an attribute of the class Person.

4. self: The initializer always takes self as as its first parameter and it refers to the object being created.

5. age (the function name) is a method in class Person. It has local scope within that class.

6. age (the variable used inside the function) is a variable within a method age. It has local scope within method age.

7. self.email: this is an attribute of the class. It has local scope.

8. person.email: this is an attribute of the object. It has global scope.


Part 2:

1. ans = [(i, j) for i in range(3) for j in range(4)]
   print(ans)


2. ans = map(lambda x: x * x, filter(lambda x: x % 2 == 0, range(5)))
print(list(ans))

'''
python 2 : map used to return a list.
python 3 : map returns an object.
https://stackoverflow.com/questions/40015439/why-does-map-return-a-map-object-instead-of-a-list-in-python-3
...   



  
