rules = [('\d+', 'NUMBER'), ('\+', 'PLUS'), ('\-', 'MINUS'), ('\*', 'MULTIPLY'), ('\/', 'DIVIDE'), ('\(', 'LP'),
         ('\)', 'RP'), ('=', 'EQUALS'), ('interface', 'KEYWORD'), ('synchronized', 'KEYWORD'), ('super', 'KEYWORD'),
         ('class', 'KEYWORD'), ('static', 'KEYWORD'), ('return', 'KEYWORD'), ('continue', 'KEYWORD'),
         ('default', 'KEYWORD'), ('boolean', 'KEYWORD'), ('try', 'KEYWORD'), ('goto', 'KEYWORD'),
         ('byte', 'KEYWORD'), ('assert', 'KEYWORD'), ('private', 'KEYWORD'), ('switch', 'KEYWORD'),
         ('instanceof', 'KEYWORD'), ('if', 'KEYWORD'), ('protected', 'KEYWORD'), ('implements', 'KEYWORD'),
         ('throws', 'KEYWORD'), ('finally', 'KEYWORD'), ('else', 'KEYWORD'), ('import', 'KEYWORD'),
         ('native', 'KEYWORD'), ('double', 'KEYWORD'), ('catch', 'KEYWORD'), ('package', 'KEYWORD'),
         ('extends', 'KEYWORD'), ('final', 'KEYWORD'), ('case', 'KEYWORD'), ('strictfp', 'KEYWORD'),
         ('const', 'KEYWORD'), ('break', 'KEYWORD'), ('new', 'KEYWORD'), ('short', 'KEYWORD'), ('enum', 'KEYWORD'),
         ('char', 'KEYWORD'), ('transient', 'KEYWORD'), ('volatile', 'KEYWORD'), ('throw', 'KEYWORD'),
         ('int', 'KEYWORD'), ('String', 'KEYWORD'), ('abstract', 'KEYWORD'), ('float', 'KEYWORD'),
         ('public', 'KEYWORD'),
         ('main', 'KEYWORD'),
         ('long', 'KEYWORD'), ('for', 'KEYWORD'), ('void', 'KEYWORD'), ('while', 'KEYWORD'), ('this', 'KEYWORD'),
         ('do', 'KEYWORD'), ('long', 'DATATYPE'), ('short', 'DATATYPE'), ('char', 'DATATYPE'),
         ('double', 'DATATYPE'), ('boolean', 'DATATYPE'), ('int', 'DATATYPE'), ('byte', 'DATATYPE'),
         ('float', 'DATATYPE'), ('\(', 'SEPARATOR'), ('\)', 'SEPARATOR'), ('\]', 'SEPARATOR'), ('\.', 'SEPARATOR'),
         ('\{', 'SEPARATOR'), ('\}', 'SEPARATOR'), ('\,', 'SEPARATOR'), ('\;', 'SEPARATOR'), ('\[', 'SEPARATOR'),
         ('true', 'BOOLEAN'), ('false', 'BOOLEAN'), ('\<<=', 'OPERATOR'), ('\<=', 'OPERATOR'), ('\?', 'OPERATOR'),
         ('\+=', 'OPERATOR'), ('\>>=', 'OPERATOR'), ('\|', 'OPERATOR'), ('\...', 'OPERATOR'), ('\:', 'OPERATOR'),
         ('\&=', 'OPERATOR'), ('\/', 'OPERATOR'), ('\~', 'OPERATOR'), ('\<', 'OPERATOR'), ('\%=', 'OPERATOR'),
         ('\::', 'OPERATOR'), ('\-', 'OPERATOR'), ('\*=', 'OPERATOR'), ('\&', 'OPERATOR'), ('\>=', 'OPERATOR'),
         ('\++', 'OPERATOR'), ('\>>>=', 'OPERATOR'), ('\%', 'OPERATOR'), ('\<<', 'OPERATOR'), ('\>', 'OPERATOR'),
         ('\^=', 'OPERATOR'), ('\*', 'OPERATOR'), ('\!=', 'OPERATOR'), ('\&&', 'OPERATOR'), ('\!', 'OPERATOR'),
         ('\->', 'OPERATOR'), ('\^', 'OPERATOR'), ('\==', 'OPERATOR'), ('\-=', 'OPERATOR'), ('\/=', 'OPERATOR'),
         ('\|=', 'OPERATOR'), ('\||', 'OPERATOR'), ('\=', 'OPERATOR'), ('\+', 'OPERATOR'), ('\--', 'OPERATOR'),
         ('\%', 'INFIX'), ('\>>', 'INFIX'), ('\<', 'INFIX'), ('\==', 'INFIX'), ('\>>>', 'INFIX'), ('\<<', 'INFIX'),
         ('\>', 'INFIX'), ('\^', 'INFIX'), ('\<=', 'INFIX'), ('\||', 'INFIX'), ('\-', 'INFIX'), ('\*', 'INFIX'),
         ('\&', 'INFIX'), ('\>=', 'INFIX'), ('\!=', 'INFIX'), ('\+', 'INFIX'), ('\|', 'INFIX'), ('\&&', 'INFIX'),
         ('\/', 'INFIX'), ('\--', 'POSTFIX'), ('\++', 'POSTFIX'), ('\-', 'PREFIX'), ('\++', 'PREFIX'),
         ('\+', 'PREFIX'), ('\--', 'PREFIX'), ('\~', 'PREFIX'), ('\!', 'PREFIX'), ('\%=', 'ASSIGNMENT'),
         ('\<<=', 'ASSIGNMENT'), ('\/=', 'ASSIGNMENT'), ('\|=', 'ASSIGNMENT'), ('\^=', 'ASSIGNMENT'),
         ('\=', 'ASSIGNMENT'), ('\*=', 'ASSIGNMENT'), ('\+=', 'ASSIGNMENT'), ('\>>=', 'ASSIGNMENT'),
         ('\&=', 'ASSIGNMENT'), ('\>>>=', 'ASSIGNMENT'), ('\-=', 'ASSIGNMENT'), ('\->', 'LAMBDA'),
         ('\::', 'METHOD REFERENCE')]
rules1 = []
for regex, type in rules:
    if type is 'KEYWORD' or type is 'DATATYPE':
        rules1.append(("^" + regex + "$", type))
    else:
        rules1.append((regex, type))

print(rules1)
