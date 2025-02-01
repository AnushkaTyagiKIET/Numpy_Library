#import Numpy
import numpy as np
#Make a File handling function where I shall load my data one line after another
#and further transform the array into Numpy array of Integers
from Operationclass import IntArray

# Here, we will also calculate which company made the maximum Product and the minimum Product
# For this I made 3 Functions , one for calculateing number of Products for each company 
# and one for finding company with max products and another to find comany with minimum products
# will be using first function in both the other 2 functions

def products_produced_by_each_company(Company_Number, data_frame):
    
    # One can use this Method as well for calculating number of products 
    '''num_products=0
    for element in data_frame[order]:
        num_products+=element
    return num_products
    '''
    # But since we are working with numpy we dont require that
    return np.sum(data_frame[Company_Number])

def max_productivity(data_frame):
    i = 0 # Used as a loop index.
    best_company = i + 1 # Initially assume the first company is the best.
    num_of_products = 0 # To store the highest number of products.

    for i in range(len(data_frame)):
        #Loops through all companies (each row in data_frame).
        #Calls a function to calculate the total products of company i
        result = products_produced_by_each_company(i, data_frame)
        
        #Compare with the current highes
        if result > num_of_products:
            num_of_products = result
            best_company = i + 1
    print(f"The best company is the {best_company}. company with {num_of_products} products made")


def min_productivity(data_frame):
    i = 0
    worst_company = i + 1
    num_of_products = products_produced_by_each_company(0, data_frame)

    for i in range(len(data_frame)):
        result = products_produced_by_each_company(i, data_frame)
        if result <= num_of_products:
            num_of_products = result
            worst_company = i + 1

    print(f"The best company is the {worst_company}. company with {num_of_products} products made")


def mean_Products(data_frame):
    for i in range(len(data_frame)):
        average = np.mean(data_frame[i])
        print(f"On average, one human from {i}. company produced {average} products")
    sum = 0
    num_elements = 0

    for row in data_frame:
        for element in row:
            num_elements += 1

    for row in range(len(data_frame)):
        row_sum = np.sum(data_frame[row])
        sum += row_sum

    total_mean = sum / num_elements

    print(f"Mean of the entire monopoly is {total_mean} per employee")


#Accessing File from Remote
def file_handling():
    lines=[]# A local List
    with open("company.txt",'r') as file:
        for line in file:
            # First I will strip the spaces(reading and beginning spaces) if there are some and will split the value having ',' as delimiter
            values=line.strip().split(",") 
            #now in value we have list of strings.
            #to convert this into Integer List I will use List Comprehension
            int_values=[int(val) for val in values]
            # We have to transform this into numpy array of Integer
            lines.append(int_values)
        data_frame=np.array([np.array(row)for row in lines],dtype='object')
        return data_frame

def main():
    #calling the above function
    # mark data_frame variable here is the local variable of main()
    data_frame=file_handling()
    print(data_frame)
    # One can check its a 2D array
    #print(type(data_frame))
    #one can check it is integer
    #for row in data_frame:
        #for i in row:
            #print(type(i))
    print("Number OF Companies",len(data_frame))
    first_branch=IntArray(data_frame[0])
    first_branch.display()
    first_branch.salary()
    first_branch.show_data()
    max_productivity(data_frame)
    min_productivity(data_frame)
    mean_Products(data_frame)

main()
    



