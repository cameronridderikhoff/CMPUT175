# CMPUT 175 Winter 2013 Lab 2 Exercise 2
# This program is used to calculate the worth of an automobile.

class Automobile:
    
    # Constructor:
    def __init__(self, length, horsepower, color):
        self.__length = length
        self.__horsepower = horsepower
        self.__color = color
        if self.__color=="red":
            self.color_factor=3
        elif self.__color=="yellow" or self.__color=="blue":
            self.color_factor=2
        else:
            self.color_factor=1
        
    # Returns the length:
    def get_length(self):
        return self.__length
    
    # Returns the horsepower:
    def get_horsepower(self):
        return self.__horsepower
    
    # Returns the color:
    def get_color(self):
        return self.__color
    
    #Returns the worth:
    def get_worth(self):
        return self.__horsepower*self.__length*self.color_factor*10
    
# Main function, which asks the user for the length, horsepower, and color of
# an automobile, and will then print out the worth of that automobile:
def main():
    l=input("Enter automobile's length in meters: ")
    h=input("Enter automobile's horsepower: ")
    c=input("Enter automobile's color: ")
    car=Automobile(float(l), int(h), c)
    print("This automobile is worth: $%.2f" % car.get_worth())

main()