import sys
import random
import csv
import time

name = "ComboFinder"

def make_combos(upper_limit, lower_limit, prices_csv, LowerBound = 2, UpperBound = 3):
    with open(prices_csv) as csv_file:
        # Opening csv file
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        number_of_rows = len(list(csv_reader))

        # Resetting the pointer back to the start of the file
        csv_file.seek(0)

        # First row is the names of the collumns
        products = [None]*(number_of_rows-1)
        prices = [None]*(number_of_rows-1)
        
        for row in csv_reader:
            if line_count == 0:
                print(f'{", ".join(row)} are being stored')
                line_count += 1
            else:
                products[line_count-1] = row[0]
                prices[line_count-1] = int(row[1])
                line_count += 1

    Set         = set(prices)
    ResultList  = set()    # Store Result set i.e. set of sets whose sum is zero
    Iterations  = len(Set)**UpperBound   # Number of Iterations

    def check_set(upper_limit,lower_limit):
        # Select set size randomly
        SetSize=random.randint(LowerBound,UpperBound)
        
        # Select number of elements from Set
        z=random.sample(Set,SetSize)
        
        # Check sum  of the set of elements 
        if sum(z) <= int(upper_limit) and sum(z) >= int(lower_limit):
            ResultList.add((frozenset(z)))
        return 1


    # Loop till number of Iterations
    for _ in range(Iterations):
        check_set(upper_limit,lower_limit)
        

    with open('combos.csv', 'w') as combo_file:
        combo_writer = csv.writer(combo_file)
        combo_list = []
        for entry in ResultList:
            #converting frozenset entries into lists
            result = list(entry)

            #appending the lists to form a list of lists
            combo_list.append(result)
        first_row = ["Product 1 Price","Product 2 Price", "Product 3 Price", "Product 4 Price"]
        combo_writer.writerow(first_row)

        #"writerows" takes an iterable as an argument and changes row after ','
        combo_writer.writerows(combo_list)











