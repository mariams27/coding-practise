from collections import defaultdict as dd

'''
1.1 Is Unique: Implement an algorithm to determine if a string has all unique 
characters. What if you cannot use additional data structures?
Hints: #44, #7 7 7, #732
'''
# TODO: potential bit array solution to come back and try to implement
# TODO: implement an inplace sorting on strings??

def is_unique(string):
    # basic way
    # time: O(c)
    # space: O(n)
    # c = the number of chars in the charachter set # e.g. ascii -> c = 256
    seen = set()
    for i in string: # O(c)
        if i in seen: # O(1)
            return False
        else:
            seen.add(i)
    return True

def is_unique2(string):
    # Time: O(n)
    # Space: O(n)
    noDuplicates = set(string)
    return len(noDuplicates) == len(string)

def is_unique3(string):
    # no extra data structures
    # Time: O(nlogn)
    # Space: O(1)
    string = sorted(string) # O(nlogn)
    for i in range(len(string) - 1): # O(c)
        if string[i] == string[i+1]:
            return False
    return True


'''
1.2 Check Permutation: Given two strings, write a method to decide if one is a 
permutation of the other.
Hints: #7, #84, #722, #737
_pg 193
'''
def is_permutation1(str1, str2):
    # Time: O(nlogn)
    # Space: O(n)

    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)
    
    return str1 == str2

def is_permutation(str1, str2):
    # Time: O(n)
    # Space: O(n)

    if len(str1) != len(str2):
        return False

    chars1 = dd(int)
    for i in str1:
        chars1[i] += 1
    
    chars2 = dd(int)
    for i in str2:
        chars2[i] += 1

    for char in chars1:
        if chars2[char] != chars1[char]:
            return False
    
    return True


'''
1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may 
assume that the string has sufficient space at the end to hold the additional 
characters, and that you are given the "true" length of the string. (Note: If 
implementing in Java, please use a character array so that you can perform this 
operation in place.)

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
Hints: #53, # 118
90
'''
def urlify(string, length):
    replacement = "%20"
    replace = False

    for i in length:
        if replace and string[i-1] == replacement[0]:
            string[i] = replacement[1]
        elif replace and string[i-1] == replacement[1]:
            string[i] = replacement[2]
            replace = False
        
        if string[i] == ' ':
            string[i] = replacement[0]
            replace = True
    
    return ''.join(string)

'''
1.4

Palindrome Permutation: Given a string, write a function to check if it is a 
permutation of a palindrome. A palindrome is a word or phrase that is the same 
forwards and backwards. A permutation is a rearrangement of letters. The palindrome 
does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
Hints: #106, #121, #134, #136
'''

'''
1.5
One Away: There are three types of edits that can be performed on strings: insert 
a character, remove a character, or replace a character. Given two strings, write a 
function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
Hints:#23, #97, #130
'''

'''
1.6
String Compression: Implement a method to perform basic string compression using the 
counts of repeated characters. For example, the string aabcccccaaa would become 
a2blc5a3. If the "compressed" string would not become smaller than the original string, 
your method should return the original string. You can assume the string has only 
uppercase and lowercase letters (a - z).

Hints:#92, #110
'''

'''
1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the
image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in 
place?
Hints: #51, # 100
'''

'''
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column are set to 0.
Hints:#17, #74, #702
'''

'''
1.9 String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a 
substring of another. Given two strings, sl and s2, write code to check if s2 is a 
rotation of sl using only one call to isSubstring (e.g., "waterbottle" is a rotation
of "erbottlewat").
Hints: #34, #88, # 7 04
'''