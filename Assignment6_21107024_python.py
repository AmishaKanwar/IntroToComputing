# Question 1
def is_perfect(num: int):
    """ Check whether the number is a perfect no. or not"""
    i = 1
    sum_of_div = 0
    while i < num:
        if num % i == 0:
            sum_of_div += i
        i += 1
    if num <= 1:
        print(f"{num} is not a perfect number.")
    elif sum_of_div == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")
    
is_perfect(28)
is_perfect(6)
is_perfect(7)

# Question 2
def is_palindrome(input_str: str):
    """Check if the given string is a palindrome"""
    input_str1 = input_str.replace(' ', '')
    rev_str = input_str1[::-1]
    if rev_str == input_str1:
        print(f"{input_str} is a palindrome.")
    else:
        print(f"{input_str} is not a palindrome.")

is_palindrome(input("Enter a string to check whether it's a palindrome or not: "))

# Question 3
def pascals_triangle(n: int):
    """Prints first n rows of Pascal's Triangle"""
    for i in range(n):
        print(' ' * (n-i), end = '')
        # compute power of 11
        print(' '.join(map(str, str(11 ** i))))

pascals_triangle(int(input("Enter no. of rows: ")))

# Question 4
def is_pangram(input_str: str):
    lst1 = [chr(i) for i in range(65, 90)]
    str1 = input_str.upper()
    for i in lst1:
        result = i in str1
        if result == True:
            answer = 'yes'
            continue
        else:
            answer = 'no'
    print(f"Is the input string ({input_str}) a pangram? {answer}")

is_pangram(input("Enter a string to check whether it's a pangram or not: ")) 

# Question 5
def alpha_sort(sequence: str):
    """Sorting hyphen-separated sequence of words alphabetically"""
    items = [n for n in sequence.split('-')]
    items.sort()
    print('-'.join(items))

alpha_sort(input("Enter a hyphen-separated sequence of words: "))


# Question 6
def student_data(student_id: int, student_name = None, student_class = None):
    """prints student_id, student_name and student_class"""
    print(f"Student ID: {student_id}, Name: {student_name}, Class: {student_class}")

student_data(21107024, 'Amisha', 'Mech')
student_data(16107189)

# Question 7

class Student:
    pass

class Marks:
    pass

amisha = Student()
yash = Student()
krushi = Student()
krushi_physics = Marks()
amisha_python = Marks()
yash_maths = Marks()

print("Check whether the created instances are of the said classes or not.")
print(isinstance(amisha, Student))
print(isinstance(yash, Student))
print(isinstance(krushi_physics, Marks)) 
print(isinstance(amisha_python, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object)) 

# Question 8

# python class to find 3 elements that sum to 0 in a given array 
class array_elements: 
    def __init__(self, arr):
        # Instance Variable    
        self.arr = arr
    
    def elements_zerosum(self):
        found = False
        n = len(self.arr) 
        # sorting array elements
        self.arr.sort()
  
        for i in range(0, n-1):
      
            # initialize left and right
            l = i + 1
            r = n - 1
            x = self.arr[i]
            while (l < r):
          
                if (x + self.arr[l] + self.arr[r] == 0):
                    # print elements if it's sum is zero
                    print(x, self.arr[l], self.arr[r])
                    l += 1
                    r -= 1
                    found = True
              
  
                # If sum of three elements is less than zero then the increment is in left
                elif (x + self.arr[l] + self.arr[r] < 0):
                    l += 1
  
                # if sum is greater than zero than 0 then decrement in right side
                else:
                    r -= 1
          
        if (found == False):
            print("No Triplet Found")
  
  

obj1 = array_elements(arr = [0, -1, 2, -3, 1])
array_elements.elements_zerosum(obj1)

obj2 = array_elements(arr = [-25, -10, -7, -3, 2, 4, 8, 10])
array_elements.elements_zerosum(obj2)

# Question 9
class bracket_str:
   def is_valid_parentheses(self, str1):
        stack, p_char = [], {"(": ")", "{": "}", "[": "]"}
        for bracket in str1:
            if bracket in p_char:
                stack.append(bracket)
            elif len(stack) == 0 or p_char[stack.pop()] != bracket:
                return False
        return len(stack) == 0

print(bracket_str().is_valid_parentheses("(){}[]"))
print(bracket_str().is_valid_parentheses("()[{)}"))
print(bracket_str().is_valid_parentheses("()"))
print(bracket_str().is_valid_parentheses("([)]"))
