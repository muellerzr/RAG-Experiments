"""
To use: Open up a file and store its contents as `code_string`:
with open("RAG-accelerate/src/accelerator.py", "r") as w:
    code_string = w.read()
"""
import re
func_list=[]
func = ''
tab  = ''
brackets = {'(':0, '[':0, '{':0}
close = {')':'(', ']':'[', '}':'{'}
string=''
tab_f=''
c1=''
multiline=False
check=False
in_class = False
decorator = None
class_name = ""
for line in code_string.split('\n'):
    tab = re.findall(r'^\s*',line)[0]
    if re.findall(r'^\s*@', line):
        decorator = line
    if (re.findall(r'^\s*def', line) or re.findall(r'^\s*class', line)) and not string and not multiline:
        if re.findall(r'^\s*class', line):
            in_class = True
            class_name = re.findall(r'class\s+(\w+)\s*[\(:]', line)[0]
        elif len(line.lstrip(" ")) == 0:
            in_class = False
        func += line + '\n'
        tab_f = tab
        check=True
    if func:
        if not check:
            if sum(brackets.values()) == 0 and not string and not multiline:
                if len(tab) <= len(tab_f):
                    # Append the metadata
                    metadata = f'File: accelerator.py\nClass: {class_name}'
                    if decorator is not None:
                        func = f'{decorator}\n{func}'
                        decorator = None
                    func = f'{metadata}\nSource:\n{func}'
                    func_list.append(func)
                    func=''
                    c1=''
                    c2=''
                    continue
            func += line + '\n'
        check = False
    for c0 in line:
        if c0 == '#' and not string and not multiline:
            break
        if c1 != '\\':
            if c0 in ['"', "'"]:
                if c2 == c1 == c0 == '"' and string != "'":
                    multiline = not multiline
                    string = ''
                    continue
                if not multiline:
                    if c0 in string:
                        string = ''
                    else:
                        if not string:
                            string = c0
            if not string and not multiline:
                if c0 in brackets:
                    brackets[c0] += 1
                if c0 in close:
                    b = close[c0]
                    brackets[b] -= 1
        c2=c1
        c1=c0

for f in func_list:
    print('-'*40)
    print(f)