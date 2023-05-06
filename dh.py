dh = 90
th = 180
f = dh + th
print('f',"=",f)

try :
 j = dh / 0
 print(j)
except ZeroDivisionError :
 print('the integer cannot divided by zero')
finally 
print('got executed')
