
try:
    fh = open("writeTest.txt","w")
    fh.write("This is some test data")
except:
    print("Error:\nAn error occured writting  the file")
else:
    print("File written")
