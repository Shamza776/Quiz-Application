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
print(file_contents) 
#moving the files
shutil.move('py.txt','C:\\Users\\PROBOOK 430\\Desktop\\moved.txt')
#deleting a file
os.remove('moved.txt') '''
''''''

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
#sum of odd no.
'''def sum_odd(odd_Num):
    #odd_Num = int(input('enter the range of numbers: '))
    sum_of_odd = 0
    for i in range(1, odd_Num):
        if (i%2 != 0):
            sum_of_odd += i
    return sum_of_odd
print(sum_odd(100))'''

'''create a single string from a list'''
'''list1 = ["hello", " Shamza", " ."," How"," are", " you"]
print("".join(list1))'''
'''find the common element in two lists'''
'''list1 = [2,3,4,5,6]
list2 = [7,8,9,0,2]
common = []
for i in list1:
    if i in list2:
        common.append(i)
        print(common)'''
'''check and count even no.'''
'''def count_evenNo():
    supposed_even_no = [1,2,3,4,5,6,7,8,9,0]
    print(max(supposed_even_no))
    count = 0
    for i in supposed_even_no:
        if (i % 2 == 0):
            count += 1
    return count
print(count_evenNo())'''
'''remove duplicates'''
'''def removeDuplicates():
    list1= [1,2,3,4]
    list2 = [3,4,5,6]
    newList = set(list1 + list2)
    print(newList)
removeDuplicates()'''
'''check for palindrome'''
'''def isPalindrome(string):
    string1 = string[::-1]
    if (string == string1):
        return True
    else:
        return False
print(isPalindrome('radar'))'''
'''a number as a parameter, return the sum of all natural that are multiples of 5,7 less than the no. provided in
the parameter'''
def multiples(num):
    sum_of_multiples = 0
    for i in range(1, num +1):
        if (i % 5 == 0) or (i % 7 == 0):
            sum_of_multiples += i
    return sum_of_multiples
print(multiples(20))
    

