string = '111111aaaaaaa???????8888bbbbbb____a'
st = set(string)
# print(st)
# for i in st:
#    print(string.count(i), i, end=' ')


def serial_iter():
    first = string[0]
    count = 0
    counter = 1
    print('dkfj  herrred')
    for i in string:
        print (first, counter, len(string))
        if counter == len(string):
            pass
            #print(count, first, end=' ')

        elif first == i:
            count += 1

        else:
            #print(count, first, end=' ')
            count = 1
            first = i
           
        counter += 1
       

serial_iter()
