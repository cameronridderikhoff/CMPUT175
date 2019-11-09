#CMPUT 175
#Cameron Ridderikhoff
#Lab exercise 2: Earthquake
def main():
    #read the data
    file = open("earthquake.txt", "r")
    longstring = file.read()
    lines = longstring.splitlines()
    file.close()
    regions = []
    #create a list of the unique regions
    for line in lines:
        data = line.split(" ")
        if not data[len(data)-1] in regions:
            regions.append(data[len(data)-1])
            
    for region in regions:
        #parse through the list of regions
        region_list = [region]
        for line in lines:
            #add the data to a region list, then print the list
            data = line.split(" ")
            if data[len(data)-1] == region:
                region_list.append([data[1], data[0]])
        print(region_list)
            
main()