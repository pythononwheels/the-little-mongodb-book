#
# what is left to do
#

counter = 0
file1 = "./en/mongodb.markdown"
file2 = "./de/mongodb.markdown"

with open(file1, 'r') as f:
   for line in f:
       counter += 1
counter_orig = counter

counter = 0
with open(file2, 'r') as f:
   for line in f:
       counter += 1
counter_me = counter

print ("Lines to translate	: ", str(counter_orig))
print ("Lines translatd		: ", str(counter_me))
print(40*"-")
print(" lines left: " + str( counter_orig - counter_me) + "  percent done: " + 
	str( (counter_me / counter_orig) * 100))

