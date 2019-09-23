x = 3.1415
list1 = ['some text',12,5.5,x ]
list2 = ["a", "b",x ]
list3 = list1 + list2
list4 = list( set(list1 + list2) )

try:
    
    tuple = {1,2,3,4,5}
    dict = {}
    fh = open("writeTest.txt","w")
    fh.write("This is some test data")

    dict['one'] = "This is one"
    dict[2]     = "This is two"

except:
    print("Error:\nAn error occured writting  the file")
else:   
    print("File written")
finally:
    print("eor")
    
print(dict)
print(tuple)
a = 'CAt dog'
print(a)
print tuple(a)