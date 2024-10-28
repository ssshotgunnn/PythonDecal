#Making a List Variable
sillysillylist = list(range(21))
print(sillysillylist)

#Working with List Elements
sillysillylist = list(range(21))
def squareList(input_list):
     return [i**2 for i in input_list]
sillysillysillylist = squareList(sillysillylist)
print(sillysillysillylist)

#Slicing
sillysillysillylist = squareList(sillysillylist)
def first_fifteen_elements(input_list):
    return input_list[:15]
first_fifteen = first_fifteen_elements(sillysillysillylist)
print(first_fifteen)

#Striding
sillysillysillylist = squareList(sillysillylist)
def every_fifth_element(input_list):
    return input_list[::5]
every_fifth = every_fifth_element(sillysillysillylist)
print(every_fifth)

#Slicing and Striding
sillysillysillylist = squareList(sillysillylist)
def fancy_function(input_list):
    last_30_elements = input_list[-30:]
    reverse_list = last_30_elements[::-1]
    return reverse_list[::3]
print(fancy_function(sillysillysillylist))
#I encountered something that was not necessarily an error, but a mistake on my part because I accidentally strided the list before reversing the first part of the list. Then, I fixed it by reversing the order of code.

#Creating a 5X5 2D List
def create_2d_list():
    matrix = []
    count = 1  
    for i in range(5):  
        row = []  
        for j in range(5):  
            row.append(count)  
            count += 1  
        matrix.append(row)  
    return matrix
matrix = create_2d_list()
print(matrix)

#Replacing 2D List with Multiples of 3
matrix = create_2d_list()  
def modified_2d_list(input_matrix):
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            if input_matrix[i][j] % 3 == 0:
                input_matrix[i][j] = '?'
    return input_matrix
new_matrix = modified_2d_list(matrix)
print(new_matrix)
#Sometimes it would give me SyntaxError: expected ":" and I realized that I had forgotten to add a : after the for loop
#It said there was SyntaxError: unterminated string literal (detected at line 55) and I checled and realized I forgot to add a quotation on the other side of the question mark.

#Summing None '?' Elements
matrix = create_2d_list() 
new_matrix = modified_2d_list(matrix) 
def sum_non_question_elements(input_matrix):
    total_sum= 0  
    for row in input_matrix:
        for element in row:
            if element != '?' :
                total_sum += element 
    return total_sum  
result = sum_non_question_elements(new_matrix)  
print(result)  
#It gave me a SyntaxError: invalid syntax and pointed out line 70. I realized I accidentally added a space between + and = and that they needed to be next to each other.
