import re

# Question 1a
# This will print 'CIS211 twice' Once for each print statement
result = re.search(r'[A-Z]*211', "CIS210 CIS211 CIS212")
print(result.group(0))
print(result[0])

# Question 1b
# Print 'xyxy' 2 times
result = re.search(r'(xy){2}', 'xy xyxy xyxyxy')
print(result.group(0))
print(result[0])

# Question 1c
# print 'Cis211.' twice
result = re.match(r'[A-Z|a-z]+211\.', 'Cis211.  CIS210 CIS211')
print(result.group(0))
print(result[0])

# Question 1d
"""
The main difference between search and match is that match returns
if just the first expression is equal to our regular expression.
Search finds all the the matches in the entire expression that matches 
our regular expression.
"""

# Question 2
# will print a dictionary with 'course1' and 'course2' as keys
# with the strings Cis210 and CIS211 as the item for the keys
result = re.match(r"(?P<course1>[A-Z|a-z]*210) (?P<course2>.*211)",
                  "Cis210 CIS211 CIS212")
print(result.groupdict())

# Challenge
s = ['', 'ab', 'aabb', 'aaabbb', 'aaaabbbb']
for item in s:
    result = re.search(r"a*b*", item)
    print(result.group())