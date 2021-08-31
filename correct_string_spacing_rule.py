nut_length = float(input("Insert nut width in mm : "))
bass_string_clearance = float(input("Insert bass string clearance in mm : "))
treble_string_clearance = float(input("Insert treble string clearance in mm : "))
nofstrings = int(input("Insert total number of strings : "))
remaining_length = nut_length - bass_string_clearance - treble_string_clearance
remaining_length = round(remaining_length,3)
#remaining_length = round(float(input("Measure space between two outer strings : ")),3)
adding_factor = float(input("Insert adding factor : "))

#print("Remaining length in the nut :",remaining_length)

starting_distance = 4.0
string_spacing_set = [0]

adding = -1
i=0
while(adding<100.00):
    adding = round(starting_distance + i * adding_factor,3)
    string_spacing_set.append(adding)
    i+=1

#print(len(string_spacing_set))    
#print(string_spacing_set)

slack = (nofstrings-1) * adding_factor
minimum = round(remaining_length - slack,3)

index1 = -1
index2 = -1

ending_point = nofstrings-1

for i in range(1,len(string_spacing_set)-ending_point):
    total = 0
    for j in range(i,i+ending_point):
        total += string_spacing_set[j]
        total = round(total,3)
        #print(total)
    if (total>=minimum)and(total<remaining_length):
        index1 = i
    if (total == remaining_length):
        index2 = i
        break
    elif (total>remaining_length):
        #print("not enough space")
        break

if (index2>index1) :
    index = index2
else :
    #index = index1+1
    index = index1

#print(total)
#print(index)
#print(string_spacing_set[index])
total = 0
for i in range(index,index+ending_point):
    total += string_spacing_set[i]
#print(round(total,3))

if (index != index2) :
    sub = remaining_length - total
    division = sub/ending_point
    #print(sub,division)
    for i in range(index,index+ending_point) :
        #print(string_spacing_set[i])
        string_spacing_set[i] += division
        #print(string_spacing_set[i])

check = 0
for i in range(ending_point):
    check += string_spacing_set[index+i]
if check == remaining_length :
    print("String spacing is correct")
    
print("From top to bottom the string spacing is :")
for i in range(int(ending_point-1)):
    print(str(round(string_spacing_set[index+i],3)) + " mm")
input()
