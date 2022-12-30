'''
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.

'''

# def arr_sum(n):
#   sum = 0
#   for x in n:
#     if len(n) != 0:
#       sum += x
#   return sum
#   #   elif len(n) == 0:
#   # return sum


# i = []

# print (arr_sum(i))

'''
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
'''

# def string_to_number(s):
#     a = None
#     for i in s.split():
#         a = i[0::1]
#     return a
#     pass

# text = "-7"
# print(string_to_number(text))

# def string_to_number(s):
#     print (int(s))

# i = "456473"
# string_to_number(i)

'''
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
'''

# def past(h, m, s):
    # Good Luck!


'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

'''
# #Soln 1
# def likes(names):
    
#   if len(names) == 0:
#     return ("no one likes this")
#   elif len(names) <=1:
#     return(f"{names[0]} likes this")
#   elif len(names) <=2:
#     return(f"{names[0]} and {names[1]} like this")
#   elif len(names) <=3:
#     text = "{}, {} and {} like this"
#     return( text.format(names[0], names[1], names[2]))
#   else:
#     return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# #Soln 2
# def likes(names):
#   if len(names) <= 0:
#     text = 'no one likes this'
#     print(text)

#   elif len(names) <= 1:
#     text = '{} likes this'
#     print(text.format(names[0]))

#   elif len(names) <= 2:
#     text = '{} and {} like this'
#     print(text.format(names[0], names[1]))

#   elif len(names) <= 3:
#     text = '{}, {} and {} like this'
#     print(text.format(names[0], names[1], names[2]))

#   else:
#     text = '{}, {} and {} others like this'
#     print(text.format(names[0], names[1], len(names) - 2))

# ll = ['gold', 'Tayo', 'Gideon', 'Loki', 'Kilo', 'Milo']
# likes(ll)


'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

#Soln1
# words = "Geeks for Geeks"
# print(reverse_words(words))

# def reverse_words(text):
#   print(' '.join([i[-1::-1] for i in text.split(" ")]))

# words = "Geeks for Geeks"
# reverse_words(words)

'''
We need a function that can transform a number(integer) into a string.
What ways of achieving this do you know?
'''

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

# def number_to_string(num):
#   return(str(num))

# print(number_to_string(120))

##Sum of positive numbers in an array
#Soln 1 -(not fully efficient)
# def positive_sum(arr):
#   # Your code here
#   num_to_sum = []
#   for i in arr:
#     if i > 0:
#       num_to_sum.append(i)
#   return(sum(num_to_sum))
      
# num = [-23, 60, 41, 8, -41, -59, 84, 55, 73, 86, -65, 5, 9, -85, -56, -34, 93, 36, -8, -65, 91, 31, -42, 65, 66, -80, -97, -39, 58, -12, -90, 68, 99, -67, 83, 6, 67, 55, -58, 78, -98, 27, -99, 7, -88, -77, 31, 44, 27, -8, 94, 80, -78, -6, 9, -75, -9, -58, -81, -32, 49, -60, -10, -59, 64, 30, 87, 11, -12, 77, -8, -34, 35, 32, -70, -39, -70, 42, 93, -46, -92, -27, -82, 81, 33, -77, 12, -31, -31, -75, 69, -13, -56, -87, -40, -87, 16]
# print(positive_sum(num))

# #Soln 2
# def positive_sum(arr):
#   # Your code here
#   return sum(x for x in arr if x > 0)

'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]
'''
# def count_positives_sum_negatives(arr):
#   sum = 0
#   itl = []
#   for n in arr:
#     if n > 0:
#       sum += 1
#   itl.append(sum)
#   return sum

# new = (10, -10, 20, 3, -7)
# print (count_positives_sum_negatives(new))

# def count_positives_sum_negatives(arr):
#   a = 0
#   b = sum(x for x in arr if x < 0)


#   for i in arr:
#     if i >= 0:
#       a = a + 1
#   c = [a, b]
#   return c

# kicks = [2, 2, 3, 6, 7, 8, -2, -8, -9, -6, 1]
# print(count_positives_sum_negatives(kicks))

# def count_positives_sum_negatives(arr):
#   a = 0
#   b = sum(x for x in arr if x < 0)
#   c = []

#   for i in arr:
#     if len(arr) == 0:
#       c = list()

#     elif i > 0:
#       a = a + 1
#     c = [a, b]
#   return c

'''
Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.

'''

# def sum_array(a):
#     sum = 0
#     for x in a:
        
#         if len(a) != 0:
#             sum += x
#         else:
#             pass
#     return sum

'''
We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
'''

# def string_to_number(s):
#     print (int(s))

# i = "456473"
# string_to_number(i)


'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""
'''
# def maskify(cc):
#   if len(cc) < 4:
#     return cc
#   else:
#     #return ([i[-1::-1] for i in cc.replace(cc[0:n], replacement)])
#     return ((len(cc) - 4) * '#' + cc[-4:])

# cc = '2453467378444'
# print(maskify(cc))


'''While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
C#: MorseCode.Get(".--") (returns string)
F#: MorseCode.get ".--" (returns string)
Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because it's no longer used and kept only for old solutions.
Elm: MorseCodes.get : Dict String String
Haskell: morseCodes ! ".--" (Codes are in a Map String String)
Java: MorseCode.get(".--")
Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
Racket: morse-code (a hash table)
Rust: MORSE_CODE
Scala: morseCodes(".--")
Swift: MorseCode[".--"] ?? "" or MorseCode[".--", default: ""]
C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"
NASM: a table of pointers to the morsecodes, and a corresponding list of ascii symbols
All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.

Good luck!

After you complete this kata, you may try yourself at Decode the Morse code, advanced.
'''

#TBC


'''
Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.

For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.

If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.
'''
#Solution
# def break_chocolate(n, m):
#   if (n > 0) and (m > 0):
#     return (n*m) -1
#   else:
#     return 0


# print(break_chocolate(9,4))


'''
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
'''

#Soln
# def divisors(integer):
#   factors = []
#   for number in range(2, integer):
#     if integer % number == 0:
#       factors.append(number)
#   return factors if factors else f'{integer} is prime'
  



#   def divisors(integer):
#     return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

# print(divisors(111))

'''
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''

#Soln

# def sum_two_smallest_numbers(numbers):
#   smallest_no = []
#   no_counter = 0
#   while no_counter <= 1:
#     smallest_no.append(min(numbers))
#     numbers.remove(min(numbers))
#     no_counter +=1
#   return sum(smallest_no)

# print(sum_two_smallest_numbers([19, 89, 6, 6, 77]))



'''
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).

Note
consecutive strings : follow one after another without an interruption
'''

#Soln
# def longest_consec(strarr, k):
#   largest_word = []
#   for i in strarr:
#     largest_word.append(len(i))
#   words = sorted(zip(strarr, largest_word), key = lambda x:x[1])
#   for n,m in words:
#   #   #print(n)
#   print(words[:-1] + words[:-2])
#     #return sum(sorted(words) [:-k])
#   #   strarr.remove(max(len(i)))
#   # return largest_word

# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 
# k = 2



# def longest_consec(strarr, k):
#   long_str = []
#   str_counter = 0
#   if len(strarr) == 0 or 0 < k < 2 or len(strarr) < k:
#     return long_str
#   while str_counter <= k - 1:
#     m = max(strarr, key=len)
#     long_str.append(m)
#     print(long_str)
#     strarr.remove(m)
#     print(long_str)
#     str_counter += 1    
#   return ''.join(long_str[:k])




#(reversed.join))

#if len(strarr) <= k or k < 2:


# def longest_consec(strarr, k):
#   long_str = []
#   str_counter = 0
#   if len(strarr) < k or len(strarr) == 0 or k < 0 :
#     return long_str
#   while str_counter < k:
#     m = max(strarr, key=len)
#     long_str.append(m)
#     strarr.remove(m)
#     str_counter += 1    
#   #return ' '.join(long_str[:k])
#   return ' '.join(filter(None, strarr))

# print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -5))


'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

# def solution(s):
#   split_letters = []
#   for i in s.upper:
#     #if i in s.upper():
      # caps += i
      # a = s.split(i)[0]
      # b = s.split(i)[1]
      # return a + " " + i + b

# print(solution("breakCamelCase"))

# def solution (s):
#   return (s.str.split("")

#print (solution ("helloWorld")

# def solution(s):
#   for i, j in enumerate(s):
#     # if i in s.upper():
#     #   s.append(i)
#     #   a = s.split(i)[0]
#     #   b = s.split(i)[1]
#       #return a + " " + b
#     print(i,j)
# print (solution ("helloWorld"))


# def solution(s):
#     new_s = ""
#     for i in s:
#         if (i.isupper()):
#             new_s +="*"+i
#         else:
#             new_s +=i
#     print(new_s)
#     new_ss = new_s.split("*")
#     new_sss = new_ss.remove('')
    
#     return new_sss

# print(solution("helloWorld"))

#s = "breakCamelCase"
# def solution(s):
#   split_letter = []
#   for i in s:
#     if (i.isupper()):
#       ss +="*"+i
#       split_letter.append(i)
#       print(split_letter)
#   for j, k in enumerate(split_letter):
#     if k in s:
#       s.split(k)
#       return s.split(k)
#       #s.split(split_letter[0])
          
# print(solution("breakCamelCase"))

# def solution(s):
#   split_letter = []
#   #new_s = ""
#   for i in s:
#     if i in s.upper():
#         split_letter.append(i)
#         #print(split_letter)
#   for j, k in enumerate(split_letter):
#     if k in s:
#         #print(new_s)
#         a = s.split(k)
#         #return ''.join(s.split(k))
#         return a[0] + " " + split_letter[0] + a[1] + " " +split_letter[1] + a[2]

# print(solution("breakCamelCase"))

'''test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")
'''


def solution(s):
  split_letter = []
  for i in s:
    if i in s.upper():
      split_letter.append(i)
      #print(split_letter)
  len_cap = len(split_letter)
  for j, k in enumerate(split_letter):
    if k in s:
      a = s.split(k)
      len_split = len(a)
      if len_split - len_cap == 1:
          return a[len_split - len_split] + " " + \
                  split_letter[len_cap - len_cap] + a[len_split - (len_split - 1)] + " " + \
                  split_letter[len_cap - (len_cap -1)] + a[len_split - (len_split - 1 - 1)]

      else:
          return s
        
print(solution("breakCamelCase"))
