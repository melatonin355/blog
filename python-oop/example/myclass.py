class MyClass:
    language = 'python'
    version = '3.6'



print(MyClass.__name__)
print(getattr(MyClass, 'version2', 'does not exists'))

# Adding attributes to the class
MyClass.version2 = "3.42"
print(getattr(MyClass, 'version2', 'does not exists'))


print("test")
