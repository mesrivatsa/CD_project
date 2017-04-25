from tkinter import *

res = dict()
not_matched = []


def findit(code_word):
    flag = 0
    for regex, type in rules:
        m = re.search(regex, code_word)
        if m is not None and m.group(0):
            res.setdefault(type, []).append(m.group(0))
            if m.group(0) is '.':
                for code_words_new in code_word.split("."):
                    findit(code_words_new)
            flag = 1
    if flag == 0:
        not_matched.append(code_word)


def func(code):
    for code_line in code:
        for code_word in code_line.split():
            findit(code_word)


rules = [('\d+', 'NUMBER'), ('\+', 'PLUS'), ('\-', 'MINUS'), ('\*', 'MULTIPLY'), ('\/', 'DIVIDE'), ('\(', 'LP'),
         ('\)', 'RP'), ('=', 'EQUALS'), ('^interface$', 'KEYWORD'), ('^synchronized$', 'KEYWORD'),
         ('^super$', 'KEYWORD'), ('^class$', 'KEYWORD'), ('^static$', 'KEYWORD'), ('^return$', 'KEYWORD'),
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
         ('^long$', 'KEYWORD'), ('^for$', 'KEYWORD'), ('^void$', 'KEYWORD'), ('^while$', 'KEYWORD'),
         ('^this$', 'KEYWORD'), ('^do$', 'KEYWORD'), ('^long$', 'DATATYPE'), ('^short$', 'DATATYPE'),
         ('^char$', 'DATATYPE'), ('^double$', 'DATATYPE'), ('^boolean$', 'DATATYPE'), ('^int$', 'DATATYPE'),
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

# func()

text = ''


def okClicked(text=''):
    code = E1.get('1.0', END)
    print(code)
    code = code.split('\n')
    func(code)
    for key in res.keys():
        print(key + ":")
        text += key + ":\n"
        for values in res[key]:
            print("\t" + values)
            text += "\t" + values + "\n"
    print("Unmatched words ", not_matched)
    text += "Unmatched words - "
    for word in not_matched:
        text += word + " , "
    E2.insert(END, text)


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
