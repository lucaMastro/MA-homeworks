#!/usr/bin/env python
import sys

def formatted_value(value:str):
    if '$' in value:
        first = value.find('$')
        end = first + 1
        while True:
            if value[end] == '$':
                break
            end += 1
        math_piece = value[first:end+1].strip()
        first_piece = value[:first].strip()
        second_piece = value[end+1:].strip() 
        new_value = "\\key{" + first_piece + "} " + math_piece + " \\key{" + second_piece + "}"
    else:
        new_value = "\\key{" + value + "} "
    new_value = "\\makecell{" + new_value.replace('||', '\\\\') + "}" + "\\\\"
    return equiv(new_value) 

def equiv(value:str):
    return value.replace("equiv ", "$\\equiv$ ")

def formatted_name(name:str):
    return "\\key{" + name + "}"

if (sys.argv[1] == ''): #only param's values
    params_names = []
    params_values = sys.argv[2].split(';')
    for i in range(1, len(params_values) + 1):
        params_names.append('Parametro {}'.format(i))
else:
    params_names = sys.argv[1].split(';')
    params_values = sys.argv[2].split(';')

# print("\\begin{myverb}")
# print(sys.argv)
# print("\\end{myverb}")
# print("-" * 50)
#input()
print("\\begin{center}")
print("\\begin{tabular}{|c|c|}")
print("\\hline")
print("\\cellcolor{cellcolor}Parametro & \\cellcolor{cellcolor}Valore \\\\")
print("\\hline")
for i in range(0, len(params_values)):
    name = formatted_name(params_names[i])
    value = formatted_value(params_values[i])
    print(name + " & " + value )
    print("\\hline")

print("\\end{tabular}")
print("\\end{center}")
