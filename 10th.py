# identity operator
a = 20
b = 20
print ('a=',a,':',id(a), 'b=',b,':',id(b))
if ( a is b ):
    print ("a and b have same identity")
else:
    print ("a and b do not have same identity")
b = 30
print ('b=',b,':',id(b))
if ( a is not b ):
    print ("a and b do not have same identity")
else:
    print ("a and b have same identity")
