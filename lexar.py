from tkinter import *

pre = ""
res = dict()
not_matched = []
rules = [('\d+', 'NUMBER'), ('\+', 'PLUS'), ('\-', 'MINUS'), ('\*', 'MULTIPLY'), ('\/', 'DIVIDE'), ('\(', 'LP'),
         ('\)', 'RP'), ('=', 'EQUALS'), ('^interface$', 'KEYWORD'), ('^synchronized$', 'KEYWORD'),
         ('^System$', 'KEYWORD'), ('^Math$', 'KEYWORD'), ('^BufferedReader$', 'KEYWORD'),
         ('^Integer$', 'KEYWORD'), ('^io$', 'KEYWORD'), ('^out$', 'KEYWORD'),
         ('^constant$', 'KEYWORD'), ('^java$', 'KEYWORD'), ('^super$', 'KEYWORD'), ('^class$', 'KEYWORD'),
         ('^static$', 'KEYWORD'), ('^return$', 'KEYWORD'),
         ('^continue$', 'KEYWORD'), ('^default$', 'KEYWORD'), ('^boolean$', 'KEYWORD'), ('^try$', 'KEYWORD'),
         ('^goto$', 'KEYWORD'), ('^byte$', 'KEYWORD'), ('^assert$', 'KEYWORD'), ('^private$', 'KEYWORD'),
         ('^switch$', 'KEYWORD'), ('^instanceof$', 'KEYWORD'), ('^if$', 'KEYWORD'), ('^protected$', 'KEYWORD'),
         ('^implements$', 'KEYWORD'), ('^throws$', 'KEYWORD'), ('^finally$', 'KEYWORD'), ('^else$', 'KEYWORD'),
         ('^import$', 'KEYWORD'), ('^native$', 'KEYWORD'), ('^double$', 'KEYWORD'), ('^catch$', 'KEYWORD'),
         ('^package$', 'KEYWORD'), ('^extends$', 'KEYWORD'), ('^final$', 'KEYWORD'), ('^case$', 'KEYWORD'),
         ('^strictfp$', 'KEYWORD'), ('^const$', 'KEYWORD'), ('^break$', 'KEYWORD'), ('^new$', 'KEYWORD'),
         ('^short$', 'KEYWORD'), ('^enum$', 'KEYWORD'), ('^char$', 'KEYWORD'), ('^transient$', 'KEYWORD'),
         ('^volatile$', 'KEYWORD'), ('^throw$', 'KEYWORD'), ('^int$', 'KEYWORD'), ('^String$', 'KEYWORD'),
         ('^abstract$', 'KEYWORD'), ('^float$', 'KEYWORD'), ('^public$', 'KEYWORD'), ('^main$', 'KEYWORD'),
         ('^long$', 'KEYWORD'), ('^for$', 'KEYWORD'), ('^void$', 'DATATYPE'), ('^while$', 'KEYWORD'),
         ('^this$', 'KEYWORD'), ('^do$', 'KEYWORD'), ('^long$', 'DATATYPE'), ('^short$', 'DATATYPE'),
         ('^char$', 'DATATYPE'), ('^double$', 'DATATYPE'), ('^boolean$', 'DATATYPE'), ('^int$', 'DATATYPE'),
         ('^String$', 'DATATYPE'),
         ('^byte$', 'DATATYPE'), ('^float$', 'DATATYPE'), ('\(', 'SEPARATOR'), ('\)', 'SEPARATOR'), ('\]', 'SEPARATOR'),
         ('\.', 'SEPARATOR'), ('\{', 'SEPARATOR'), ('\}', 'SEPARATOR'), ('\,', 'SEPARATOR'), ('\;', 'SEPARATOR'),
         ('\[', 'SEPARATOR'), ('true', 'BOOLEAN'), ('false', 'BOOLEAN'), ('\<<=', 'OPERATOR'), ('\<=', 'OPERATOR'),
         ('\?', 'OPERATOR'), ('\+=', 'OPERATOR'), ('\>>=', 'OPERATOR'), ('\|', 'OPERATOR'), ('\...', 'OPERATOR'),
         ('\:', 'OPERATOR'), ('\&=', 'OPERATOR'), ('\/', 'OPERATOR'), ('\~', 'OPERATOR'), ('\<', 'OPERATOR'),
         ('\%=', 'OPERATOR'), ('\::', 'OPERATOR'), ('\-', 'OPERATOR'), ('\*=', 'OPERATOR'), ('\&', 'OPERATOR'),
         ('\>=', 'OPERATOR'), ('\++', 'OPERATOR'), ('\>>>=', 'OPERATOR'), ('\%', 'OPERATOR'), ('\<<', 'OPERATOR'),
         ('\>', 'OPERATOR'), ('\^=', 'OPERATOR'), ('\*', 'OPERATOR'), ('\!=', 'OPERATOR'), ('\&&', 'OPERATOR'),
         ('\!', 'OPERATOR'), ('\->', 'OPERATOR'), ('\^', 'OPERATOR'), ('\==', 'OPERATOR'), ('\-=', 'OPERATOR'),
         ('\/=', 'OPERATOR'), ('\|=', 'OPERATOR'), ('\||', 'OPERATOR'), ('\=', 'OPERATOR'), ('\+', 'OPERATOR'),
         ('\--', 'OPERATOR'), ('\%', 'INFIX'), ('\>>', 'INFIX'), ('\<', 'INFIX'), ('\==', 'INFIX'), ('\>>>', 'INFIX'),
         ('\<<', 'INFIX'), ('\>', 'INFIX'), ('\^', 'INFIX'), ('\<=', 'INFIX'), ('\||', 'INFIX'), ('\-', 'INFIX'),
         ('\*', 'INFIX'), ('\&', 'INFIX'), ('\>=', 'INFIX'), ('\!=', 'INFIX'), ('\+', 'INFIX'), ('\|', 'INFIX'),
         ('\&&', 'INFIX'), ('\/', 'INFIX'), ('\--', 'POSTFIX'), ('\++', 'POSTFIX'), ('\-', 'PREFIX'), ('\++', 'PREFIX'),
         ('\+', 'PREFIX'), ('\--', 'PREFIX'), ('\~', 'PREFIX'), ('\!', 'PREFIX'), ('\%=', 'ASSIGNMENT'),
         ('\<<=', 'ASSIGNMENT'), ('\/=', 'ASSIGNMENT'), ('\|=', 'ASSIGNMENT'), ('\^=', 'ASSIGNMENT'),
         ('\=', 'ASSIGNMENT'), ('\*=', 'ASSIGNMENT'), ('\+=', 'ASSIGNMENT'), ('\>>=', 'ASSIGNMENT'),
         ('\&=', 'ASSIGNMENT'), ('\>>>=', 'ASSIGNMENT'), ('\-=', 'ASSIGNMENT'), ('\->', 'LAMBDA'),
         ('\::', 'METHOD REFERENCE')]

cont = ""
child_class = ""
inheritance_text = ""
var_func_datatype = ""
functions = dict()
variables = []


def tokenize(code_word, counter):
    flag = 0
    global var_func_datatype, cont, child_class, inheritance_text, functions, variables
    for regex, type in rules:
        m = re.search(regex, code_word)
        if m is not None and m.group(0):
            res.setdefault(type, []).append(m.group(0))
            if var_func_datatype not in "":
                n = re.search("(.+)\((.*)\)", code_word)
                if n:
                    # functions.update([child_class, n.group(0), str(counter)])
                    functions.setdefault(child_class + "$" + n.group(0), []).append(str(counter))
                    print(n.group(0))
                    # print(m.group(1))
                    print(code_word, counter)
            if "DATATYPE" in type:
                var_func_datatype = code_word
                cont = type
            if re.search("^class$", code_word):
                cont = "class"
            if re.search("^extends$", code_word):
                cont = code_word
                print("Inheritance at line : ", counter)
            if "." in m.group(0):
                for code_words_new in code_word.split("."):
                    tokenize(code_words_new, counter)
            flag = 1
    if flag == 0:
        if "class" in cont:
            print("Class name: ", code_word, counter)
            cont = ""
            child_class = code_word
            res.setdefault("CLASS", []).append(code_word)
        elif "extends" in cont:
            print("Child class :", child_class, "Parent class :", code_word)
            cont = ""
            inheritance_text += "\tChild class :" + child_class + "\n\tParent class : " + code_word + "\n\tLine : " + str(
                counter) + "\n"
        elif "DATATYPE" in cont:
            variables.append(code_word)
            cont = ""
            print("VAR: ", code_word)
        else:
            not_matched.append(code_word)


def okClicked(output=''):
    java_code = E1.get('1.0', END)
    print(java_code)
    counter = 0
    global cont, var_func_datatype
    for code_line in java_code.split('\n'):
        counter += 1
        cont = ""
        var_func_datatype = ""
        k = re.search("(.+)//(.*)", code_line)
        if k is not None:
            print(code_line.split("//")[0])
            print(code_line)
            code_line = code_line.split("//")[0]
        for code_word in code_line.split():
            tokenize(code_word, counter)

    for key in res.keys():
        print(key + ":")
        output += key + ":\n"
        res[key] = list(set(res[key]))
        for values in res[key]:
            print("\t" + values)
            output += "\t" + values + "\n"
    # print("Unmatched words ", not_matched)
    # output += "Unmatched words - "
    rules1 = []
    for word in not_matched:
        # output += word + " , "
        rules1.append(("^" + word + "$", "KEYWORD"))
    output += "\n"
    output += "INHERITANCE: \n" + inheritance_text
    rules1 = list(set(rules1))
    print(rules1)
    for classnamefname in functions.keys():
        functions[classnamefname] = list(set(functions[classnamefname]))
        if len(functions[classnamefname]) > 1:
            print("OVERLOADING OF :", classnamefname.split("$")[1], " AT ", functions[classnamefname])
            output += "\n" + "OVERLOADING OF : " + classnamefname.split("$")[1] + " AT \n"
            for l in functions[classnamefname]:
                output += "\tLine : " + l + "\n"
    print(functions)
    print(variables)
    output += "VARIABLES: \n"
    for var in variables:
        output += "\t" + var + "\n"
    E2.insert(END, output)


top = Tk()
L1 = Label(top, text="Java Code")
L1.grid(row=0, column=0)
E1 = Text(top, height=20)
E1.grid(row=0, column=1)
E2 = Text(top, height=20)
E2.grid(row=1, column=1)
MyButton1 = Button(top, text="Submit", width=10, command=okClicked)
MyButton1.grid(row=0, column=2)
top.mainloop()
