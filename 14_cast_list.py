def create_cast_list(filename):
    cast_list = []
    cast_lis = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list
    with open(filename) as f:
        file_data = f.read()
        for line in file_data:
            cast_lis.append(line.strip())
            for lin in cast_lis:
                for i in range(len(lin)):
                    while(lin[i] != ','):
                    	cast_list.append(lin[i])
                
    return cast_list
    print(cast_list)
    
create_cast_list("file:///Users/AKG/Desktop/Udacity/flying_circus_cast.txt")

#suggested solution
def create_cast_list_suggested(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename) as f:
    # use the for loop syntax to process each line        
    # and add the actor name to cast_list
        #for i in range(3):
    	for line in f:
        	#print(line)
            line_data = line.split(',')
            #print(line_data)
            cast_list.append(line_data[0]) #what happens if i remove the index???
    return cast_list

#create_cast_list_suggested('flying_circus_cast.txt')
