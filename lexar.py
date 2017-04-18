import re

keywords = {'abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue',
            'default', 'do', 'double', 'else', 'enum', 'extends', 'final', 'finally', 'float', 'for', 'goto', 'if',
            'implements', 'import', 'instanceof', 'int', 'interface', 'long', 'native', 'new', 'package', 'private',
            'protected', 'public', 'return', 'short', 'static', 'strictfp', 'super', 'switch', 'synchronized', 'this',
            'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while'}
datatypes = {'boolean', 'byte', 'char', 'double', 'float', 'int', 'long', 'short'}
boolean = {"true", "false"}
separator = {'(', ')', '{', '}', '[', ']', ';', ',', '.'}

operators = {'>>>=', '>>=', '<<=', '%=', '^=', '|=', '&=', '/=', '*=', '-=', '+=', '<<', '--', '++', '||', '&&', '!=',
             '>=', '<=', '==', '%', '^', '|', '&', '/', '*', '-', '+', ':', '?', '~', '!', '<', '>', '=', '...', '->',
             '::'}
INFIX = {'||', '&&', '|', '^', '&', '==', '!=', '<', '>', '<=', '>=', '<<', '>>', '>>>', '+', '-', '*', '/', '%'}
PREFIX = {'++', '--', '!', '~', '+', '-'}

POSTFIX = {'++', '--'}

ASSIGNMENT = {'=', '+=', '-=', '*=', '/=', '&=', '|=', '^=', '%=', '<<=', '>>=', '>>>='}

LAMBDA = {'->'}

METHOD_REFERENCE = {'::'}

# file_name = input("Enter file name")
# file = open(file_name, "r")
file = open("C:\Users\Tanmay\Desktop\Hello.txt", "r")
code = file.read()
code = code.split("\n")
print(code)


def isKeyword(token):
    if keywords.__contains__(token):
        print("Keyword : " + token)


def isDataType(token):
    if datatypes.__contains__(token):
        print("Datatype : " + token)


def isSeparator(token):
    if separator.__contains__(token):
        print("Separator: " + token)


def isOperator(token):
    if operators.__contains__(token):
        print("Operators: " + token)


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


def func():
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
func()
for key in res.keys():
    print(key + ":")
    for values in res[key]:
        print("\t" + values)
print("Unmatched words ", not_matched)
