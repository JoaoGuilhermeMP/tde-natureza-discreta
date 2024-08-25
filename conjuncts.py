# João Guilherme Machado Palma

#The program you will develop will receive a text file (.txt) as input containing several sets of data and several operations. These operations and data will be represented in a text file containing only the data related to the operations that must be performed according to the following fixed rule: the first line of the input text file will contain the number of operations described in the file, and this number of operations will be an integer; the following lines will always follow the same pattern of three lines: the first line presents the operation code (U for union, I for intersection, D for difference, and C for Cartesian product), and the second and third lines will contain the elements of the sets separated by commas.

# defining the functions of each operation

def union(conjunct01, conjunct02):
    result = conjunct01.union(conjunct02)
    return result

def intersection(conjunct01, conjunto2):
    result = conjunct01.intersection(conjunto2)
    return result

def difference(conjunct01, conjunct02):
    result = conjunct01.difference(conjunct02)
    return result

def cartesianProduct(conjunct01, conjunct02):
    result = { (x, y) for x in conjunct01 for y in conjunct02 }
    return result


# this function makes everything in this program 
def operationsConjunct(arquivoTxt): 
    with open(arquivoTxt, 'r') as file: # first the program will open and read the file .txt and will storage the data and how many operations this file has into the variable lines
        lines = file.readlines()

# now the program will initialize the global variables of the function
    i = 1
    NumOperations = int(lines[0].strip())  
    results= []


    for _ in range(NumOperations):
        operation = lines[i].strip()
        conjunct01 = set(lines[i + 1].strip().split(', '))
        conjunct02 = set(lines[i + 2].strip().split(', '))

        if operation == "U":
            result = union(conjunct01, conjunct02)
        elif operation == 'I':
            result = intersection(conjunct01, conjunct02)
        elif operation == 'D':
            result = difference(conjunct01, conjunct02)
        elif operation == 'C':
            result = cartesianProduct(conjunct01, conjunct02)
        
        if operation == 'I' and not result:
            resultConjuntos = '∅'
        elif operation != 'C':
            resultConjuntos = ', '.join(result)
        else:
            resultConjuntos = ', '.join(str(elemento) for elemento in(sorted(result))) 
        
        results.append(f"{operation}: Conjunct 1 {{{', '.join(conjunct01)}}}, Conjunct 2 {{{', '.join(conjunct02)}}}. Result: {{{resultConjuntos}}}")

        i = i + 3

# this will show in terminal all the results asked in .txt file one by one 
    for result in results:
        print(result)

# Put the name of the file you want to read here 
operationsConjunct('file01.txt')