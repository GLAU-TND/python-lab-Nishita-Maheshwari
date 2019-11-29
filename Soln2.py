try:
    n=int(input('Enter no: ')) + input()
    
    n.count()
except(AttributeError):
    print('OOPS! Attribute Error occurred')
except(TypeError):
    print('OOPS! Type Error occurred')
except(ValueError):
    print('OOPS! Value Error occurred')
