#!/usr/bin/python


import re
import operator
import sys

chars = {
    '\xc2\x82' : ',',        # High code comma
    '\xc2\x84' : ',,',       # High code double comma
    '\xc2\x85' : '...',      # Tripple dot
    '\xc2\x88' : '^',        # High carat
    '\xc2\x91' : '\x27',     # Forward single quote
    '\xc2\x92' : '\x27',     # Reverse single quote
    '\xc2\x93' : '\x22',     # Forward double quote
    '\xc2\x94' : '\x22',     # Reverse double quote
    '\xc2\x95' : ' ',
    '\xc2\x96' : '-',        # High hyphen
    '\xc2\x97' : '--',       # Double hyphen
    '\xc2\x99' : ' ',
    '\xc2\xa0' : ' ',
    '\xc2\xa6' : '|',        # Split vertical bar
    '\xc2\xab' : '<<',       # Double less than
    '\xc2\xbb' : '>>',       # Double greater than
    '\xc2\xbc' : '1/4',      # one quarter
    '\xc2\xbd' : '1/2',      # one half
    '\xc2\xbe' : '3/4',      # three quarters
    '\xca\xbf' : '\x27',     # c-single quote
    '\xcc\xa8' : '',         # modifier - under curve
    '\xcc\xb1' : ''          # modifier - under line
}
def replace_chars(match):
    char = match.group(0)
    return chars[char]
 
Marron={ '0-1':'A', '2-5':'B', 'veces':'C', \
         '1ro':'A', '2do':'B', '3ro':'C', '4to':'D' }
def getLetterOption(st):
    if st in Marron:
        return Marron[st]
    return st.split("-")[0]

def prettyPrint(M):
    print "Pregunta,A,B,C,D,E"
    for k in M:
        st = str(k[0]) + ","
        for i in "ABCDE": #k[1]:
            val = 0
            if i in k[1]:
                val = k[1][i]
            st = st + str(val)
            if (i != 'E'):
                st = st + ","
        print st


arg = sys.argv
if len(arg) < 2: 
    print "Usage: eval.py file.txt"
    sys.exit(0)

fPtr = open(arg[1], 'r')
content = fPtr.read()

# erase anything that is not an accepted character 
content = re.sub("(?![A-z\s\-\*\|0-9]).{1}","",content)
content = re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, content)

sp = re.split(' ', content) #, flags=re.IGNORECASE)
sp = filter (lambda a: a.replace(" ","")!='' , sp)
sp = map (lambda a: a.replace(" ","") , sp)

 
bar = False
question = ""
Q = {} # map for the questions
M = {} # map for the options per question

for i in sp:
    if bar:
		M[getLetterOption(option)] = int(i)	
		option = ""
		bar = False
    if re.match("\S*PREG\S+",i):
		if (question!=""):
			if question not in Q:
				Q[question] = M
			else:
				Q[question].update(M)
		question = int(re.sub("PREG","",i))
		M = {}
    if re.match(".+\*+",i):		
		# an asterisk bar was detected		
		if len(option)==0:
			option = prior
		bar = True
    if re.match("[ABCD]-",i):
	 	option = i
    prior = i

# for the last
Q[question] = M

sortedQ = sorted(Q.iteritems(), key=operator.itemgetter(0))

prettyPrint(sortedQ)
