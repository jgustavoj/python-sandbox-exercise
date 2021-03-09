# Python has functions for creating, reading, updating, and deleting files.


# Open a file 

myFile = open('myFile.txt', 'w')

# get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode) 

# write to file
myFile.write('I love python')
myFile.write(' and JavaScript')
myFile.close()

# append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()


# read from file 
myFile = open('myFile.txt', 'r+')
text = myFile.read(10)
print(text)