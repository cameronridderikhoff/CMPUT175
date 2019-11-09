#CMPUT 175
#Cameron Ridderikhoff
#Lab exercise 1: Rainfall
def main():
    #read the data
    file = open("rainfall.txt", "r")
    longstring = file.read()
    strings = longstring.splitlines()
    sets = []
    file.close()
    #separate the data
    for data in strings:
        one_set = data.split(" ")
        one_set[0] = one_set[0].upper()
        one_set[1] = round(float(one_set[1]), 1)
        sets.append(one_set)
        
    #sort the data for the 51-60 set
    set_51_60 = sort_set(51, 60, sets)
            
    #sort the data for the 61-70 set
    set_61_70 = sort_set(61, 70, sets)   
    
    #sort the data for the 71-80 set
    set_71_80 = sort_set(71, 80, sets)   
    
    #sort the data for the 81-90 set
    set_81_90 = sort_set(81, 90, sets)   
    
    #sort the data for the 91-100 set
    set_91_100 = sort_set(91, 100, sets)
    
    #write the data to a file
    wfile = open("rainfallfmt.txt", "w")
    wfile.write("Annual Rainfall:\n")
    write_set(set_51_60, wfile, "[51-60]")
    write_set(set_61_70, wfile, "[61-70]")
    write_set(set_71_80, wfile, "[71-80]") 
    write_set(set_81_90, wfile, "[81-90]") 
    write_set(set_91_100, wfile, "[91-100]") 
    wfile.close()
def sort_set(low, high, sets):
    #this function sorts a list of lists with a number in the second position 
    #such that the number is between the low number and the high number inputted
    new_set = []
    for one_set in sets:
        if one_set[1] >= low and one_set[1] < high:
            new_set.append(one_set)
            sets.remove(one_set) 
    return new_set

def write_set(sets, wfile, interval):
    #this function writes a set of sets to a file
    #interval is the numerical distance between the upper and lower bounds of the sets 
    wfile.write(interval + ":\n")
    for aset in sets:
        wfile.write(aset[0].center(25, " ") + " " + str(aset[1]).center(5, " ") + "\n")
    wfile.write("\n")
    
main()