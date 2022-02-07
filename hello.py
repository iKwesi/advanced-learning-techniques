def addthis(x: int, y: int):
    print(f"This is x: {x} and x-type {type(x)}")
    print(f"This is y: {y} and y-type: {type(y)}")
    try:
        result = x+y
    except TypeError as exception:
        print(f"The wrong type passed in is {exception}")
        result = int(x) + int(y)
        
    print(f"This is the result {result}")
    return result
    
print(addthis(1, 2))