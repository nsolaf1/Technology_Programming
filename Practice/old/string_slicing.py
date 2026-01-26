# 1. Extracting Substrings
text = "PythonProgramming"
result = text[:6]  # "Python"
print(result)


# Reversing a String
word = "Hello"
result = word[::-1]  # "olleH"
print(result)


# Skipping Characters
phrase = "abcdefghijklmnop"
result = phrase[::2]  # "acegikmo"
print(result)

# Extracting Last N Characters
sentence = "DataScience"
result = sentence[-4:]  # "ence"
print(result)

#  Middle Substring
data = "MachineLearning"
result = data[7:12]  # "Learn"
print(result)


# First and Last Character
string = "abcdefg"
result = string[0] + string[-1]  # "ag"
print(result)


# Remove First and Last Character
word = "Python"
result = word[1:-1]  # "ytho"
print(result)


# Alternating Characters
code = "programming"
result = code[::2]  # "pormig"
print(result)


# Extract Domain Name
email = "student@university.com"
result = email[email.index("@")+1 : email.index(".")]  # "university"
print(result)


# Check for Palindrome
palindrome = "madam"
result = palindrome == palindrome[::-1]  # True
print(result)


