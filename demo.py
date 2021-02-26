from serialkeys import Serialkeys


print('Simple case \n')
generator = Serialkeys()
keys = generator.generate(4)
for key in keys: 
    print (key)
    
print('')
print('More complex usage \n')
generator = Serialkeys(digits=9, _delimeter="/", _chunksize=3, _alphabet="1234567890")
keys = generator.generate(4)
for key in keys: 
    print (key)