# João Guilherme Machado Palma

#The program you will develop will receive a text file (.txt) as input containing several sets of data and several operations. These operations and data will be represented in a text file containing only the data related to the operations that must be performed according to the following fixed rule: the first line of the input text file will contain the number of operations described in the file, and this number of operations will be an integer; the following lines will always follow the same pattern of three lines: the first line presents the operation code (U for union, I for intersection, D for difference, and C for Cartesian product), and the second and third lines will contain the elements of the sets separated by commas.


# this function makes everything in this program 
def operations(arquivoTxt): 
    with open(arquivoTxt, 'r') as arquivo: # first the program will open and read the file .txt and will storage the data into the variable lines
        lines = arquivo.readlines()

# now the program will initialize the global variables of the function
    NumOperations = int(lines[0].strip())  
    init = 1
    results= []

# now the program will start a loop, this loop will make everything in this code and the file .txt run
    for _ in range(NumOperations):
        operation = lines[init].strip()
        conjunct01 = set(lines[init + 1].strip().split(', '))
        conjunct02 = set(lines[init + 2].strip().split(', '))

# this will check the letter in the .txt file and will do the right operation        
        if operation == 'U':
            result = conjunct01.union(conjunct02)
            nameGroup = "Union"
        elif operation == 'I':
            result = conjunct01.intersection(conjunct02)
            nameGroup = "Intersection"
        elif operation == 'D':
            result = conjunct01.difference(conjunct02)
            nameGroup = "Difference"
        elif operation == 'C':
            result = {(a, b) for a in conjunct01 for b in conjunct02}
            nameGroup = "Cartesian Product"
        
        if operation == 'I' and not result:
            resultConjuntos = '∅'
        elif operation != 'C':
            resultConjuntos = ', '.join(result)
        else:
            resultConjuntos = ', '.join(str(elemento) for elemento in sorted(result))
        
        results.append(f"{nameGroup}: Conjunct 1 {{{', '.join(conjunct01)}}}, Conjunct 2 {{{', '.join(conjunct02)}}}. Result: {{{resultConjuntos}}}")

        init = init + 3

# this will show in terminal all the results asked in .txt file one by one 
    for result in results:
        print(result)

# Put the name of the file you want to read here 
operations('arquivo02.txt')