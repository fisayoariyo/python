# Only a few Values are False

''' If you have an object that is made from a class with a __len__ funtion that returns 0 or False
'''
#Example
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))


