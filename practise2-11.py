#!/usr/bin/env python

a = [] 
Sum = 0
for i in range(5):
    b = int(input("n%d = " % (i + 1)))
    a.append(b)
    
select = input('''(1).Sum
                  (2).Average
                  (3).Exit
               ''')
while True:
    if select == 1:
        Sum = sum(a)
    print 'Sum = ', Sum
    elif select == 2:
        Average = float(sum(a))/len(a)
    print  'Average = ', Average
    elif select == 3:
        break
    else:
        print 'Please input again'
