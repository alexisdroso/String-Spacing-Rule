nut_length = float(input("Insert nut width in mm : "))
bass_string_clearance = float(input("Insert outer bass string position in mm : "))
treble_string_clearance = float(input("Insert outer treble string position in mm : "))
nofstrings = int(input("Insert total number of strings : "))
remaining_length = round(nut_length - bass_string_clearance - treble_string_clearance, 3)
#remaining_length = round(float(input("Insert the distance between the two outer strings : ")), 3)
adding_factor = float(input("Insert adding factor : ")) #0.1 is good for guitars, increase a bit for basses

#print("Remaining length in the nut :",remaining_length)

starting_distance = 4.0
string_spacing_set = [0]

adding = -1
i=0
while(adding<100.00):
    adding = round(starting_distance + i * adding_factor, 3)
    string_spacing_set.append(adding)
    i+=1

#print(len(string_spacing_set), string_spacing_set)    

margin = (nofstrings-1) * adding_factor
minimum = round(remaining_length - margin, 3)

index1 = -1
index2 = -1

ending_point = nofstrings-1

for i in range(1,len(string_spacing_set)-ending_point):
    total = 0
    for j in range(i,i+ending_point):
        total += string_spacing_set[j]
    total = round(total, 3)
    #print(total)
    if (total>=minimum)and(total<remaining_length):
        index1 = i
    if (total == remaining_length):
        index2 = i
        break
    elif (total>remaining_length):
        #print("total>remaining length")
        break

if (index2>index1) :
    index = index2
else :
    index = index1
    total -= margin

#print(total, index, string_spacing_set[index])

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
check = round(check,3)
print("\n")
if check == remaining_length :
    #print("\nString spacing is correct\n")
    for i in range(ending_point):
        print("From %d string to %d string the distance is : %.3f mm" % (i+1,i+2,string_spacing_set[index+i]))
else :
    print("Sorry something went wrong")
input()
