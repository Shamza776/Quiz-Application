#solving simple python problems
'''Write a Python program that calculates and prints the area of a rectangle.
 You can take the length and width as input from the user. '''
#area of a rectangle
'''def area_rectangle():
    length = int(input('enter preferred length: '));
    width = int(input('enter preferred breadth: '));
    return length * width;
result = area_rectangle();
print('The area is: ', result);  '''

'''Problem 2: String Manipulation
Write a function that takes a string and prints the reversed version of that string.'''
'''def reverse_string():
    string = "Nicole"
    print(string[::-1]);
reverse_string(); '''

'''Problem 3: Lists and Loops
Given a list of numbers, write a Python program to find and print the sum of all the elements in the list.'''
'''numbers = [1,2,3,4,5,6];
total = 0
for x in numbers:
    total += x;
print(total);  '''

'''Problem 4: Conditional Statements
Write a program that takes a number and prints whether it's positive, negative, or zero.'''
''' def define_number(num):
    #num = float(input("Enter a number: "))
    if (num > 0):
        print('number is positive');
    elif (num < 0):
        print('number is negative');
    else:
        print('the number is zero');
    #print(num);
define_number(0); '''

'''Problem 5: File Handling
Create a text file with some lines of text. Write a Python program to read the contents of the file and print each line.'''
'''import os
from io import open 
import time
import shutil
path = 'C:\\Users\\PROBOOK 430\\Desktop\\py.txt';
if (os.path.exists):
    print('it exists')
else:
    print('does not exists')

text = 'heyy youuuu\n this is text im writing in the new text document'
file = open('py.txt' , 'w')
file.write(text)
#time.sleep(10)
file_append = open('py.txt', 'a')
file_append.write('\n appending some more text')
file = open('py.txt', 'r')
file_contents = file.read()
file.close()
#copying the file contents
copied_file= shutil.copy('py.txt' , "C:\\Users\\PROBOOK 430\\Desktop\\copied.txt")
print(file_contents) '''

#sum of even no.
'''def sum_even():
    num = int(input("Enter the range for which u want to check the sum of even nos :"))
    count = 0
    sum = 0
    for i in range(1,num+1):
        if(i % 2 == 0):
            sum+=i
            return sum
        
print(sum_even())'''

###ksh to dollars
'''def currencyConverter ():
    ksh = int(input('enter amount in ksh: '))
    dollars = ksh * 100 
    print(dollars)
currencyConverter()'''

##quess the word


