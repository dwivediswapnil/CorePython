#FILE I/O
# open
import re 
string =" search inside of this text plz this !"
a = re.search('this',string)

#Where the string occurs.
print(a.span())

#Where the text starts.
print(a.start())

#What part of string there was a match.
print(a.group())

#If we do something that doesn't exist, it will give error

#Creating apattern that we want to check
pattern  = re.compile('this')
ap = pattern.search(string)
ap1 = pattern.findall(string)
ap2 = pattern.match(string) #will check the match for the searched string.
print(ap2)

#Advanced Patterns
pattern = re.compile('')
