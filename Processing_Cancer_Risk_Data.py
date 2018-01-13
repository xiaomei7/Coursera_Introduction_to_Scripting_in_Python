"""
Week 4 practice project solution for Python Data Analysis
Processing 2D tables 
"""

import csv



#########################################################
# Part 1 - Week 3



def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
       
    with open(file_name, newline='') as csv_file:       # don't need to explicitly close the file now
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_table.append(row)
    return csv_table



def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file with the name file_name
    """
    
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for row in csv_table:
            csv_writer.writerow(row)



#########################################################
# Part 2 - Week 4


def select_columns(my_table, col_indices):
    """
    Input: Nested list my_table and a list of integers col_indices
    Output: Nested list corresponding to sub-table formed by
    columns in col_indices
    """
    answer = []
    for row in my_table:
        reduced_row = [row[idx] for idx in col_indices] 
        answer.append(reduced_row)
    return answer


def sort_by_column(my_table, col_idx):
    """
    Input: Nested list my_table and an integer col_idx
    Action: Mutate the order of the rows in my_table such that the entries in
    the column col_idx appear in DESCENDING order when interpreted as numbers
    """
    # https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda/8966627#8966627
    col_fun = lambda row: float(row[col_idx])
    my_table.sort(key = col_fun, reverse = True)
    
    
    
def test_part2_code():
    """
    Run examples that test the functions for part 2
    """
    
    # Load a simple example table
    test_table = read_csv_file("test_case.csv")  # file is available at ...
    print_table(test_table)
    print()
    
    # Simple test for column trimmng function
    print_table(select_columns(test_table, [0, 2]))
    print()
    
    # Simple test for column sorting function
    sort_by_column(test_table, 3)
    print_table(test_table)
    print()

    # Read cancer-risk data set, select columns A, B, C, E, and L, then sort by column E in descending order
    cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    col_indices = [0, 1, 2, 4, 11]
    trimmed_risk_table = select_columns(cancer_risk_table, col_indices)
    sort_by_column(trimmed_risk_table, 4)
    write_csv_file(trimmed_risk_table, "cancer_risk_trimmed.csv")
    
    # Load our file "cancer_risk_trimmed_solution.csv" and compare with your solution
    trimmed_risk_solution = read_csv_file("cancer_risk_trimmed_solution.csv")
    for row in range(len(trimmed_risk_table)):
        for col in range(len(trimmed_risk_table[0])):
            if trimmed_risk_table[row][col] != trimmed_risk_solution[row][col]:
                print("Difference at", row, col, trimmed_risk_table[row][col], trimmed_risk_solution[row][col])
    


test_part2_code()

#Output from test_part2_code()
##['1', '2', '3', '4']
##['5', '6', '7', '8']
##['-2', '-3', '-4', '-5']
##
##['1', '3']
##['5', '7']
##['-2', '-4']
##
##['5', '6', '7', '8']
##['1', '2', '3', '4']
##['-2', '-3', '-4', '-5']
