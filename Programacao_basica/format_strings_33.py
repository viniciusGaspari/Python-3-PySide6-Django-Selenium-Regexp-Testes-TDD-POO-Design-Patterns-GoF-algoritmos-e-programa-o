a = 'A'
b = 'B'
c = 1.1

formato = 'a = {arg0}, a = {arg0}, b = {arg1}, c = {arg2:.2f}'.format(
    arg0 = a, 
    arg1 = b, 
    arg2 = c
)

print(formato)