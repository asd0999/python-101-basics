# Use an import statement at the top
import random

word_file = "file:///Users/.../words.txt" #enter file path
word_list = []
pass_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
		    word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    for i in range(3):
        pass_list.append(random.choice(word_list))
    password = pass_list[0]+pass_list[1]+pass_list[2]
    print (password)
#    return (str(pass_list[0])+str(pass_list[1])+str(pass_list[2]))
    for i in range(3):
        pass_list.pop()

generate_password()

#suggested solution
def generate_password_1():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

#OR
def generate_password_2():
    return str().join(random.sample(word_list,3))

