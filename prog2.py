# # A program 

# import sys
# from collections import Counter 


# #pass in number of words as first argument 
# try:
#     num_words = int(sys.argv[1])
# except: 
#     print ("usage:most_common_words.py num_words")
#     sys.exit(1) #non-zero exit code indicates error 
    
# counter = Counter(word.lower()                 #Lowercase words
#     for line in sys.stdin
#     for word in line.strip().split()
#     if word)
    
# for word, count in counter .most_common(num_words):
#     sys.stdout.write(str(count))
#     sys.stdout.write("\t")
    
#     sys.stdout.write(word)
#     sys.stdout.write("\n")


from collections import namedtuple
#Define Student using namedtuple
Student = namedtuple("Student", ["name", "age", "marks"])
s1 = Student("Anita", 21, 85)
print(s1)                           #Student(name='Anita', age='21', marks="85")
print(s1.name)                      #Access by name -> Anita
print(s1[2])                        #Access by index -> 85
print(s1.age)