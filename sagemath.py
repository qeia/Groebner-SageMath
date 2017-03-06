#edges are edges
#n is number of vertices
edges = [[1,3,5],[2,4,5]]
strings = []

ma = 0
for e in edges:
	for x in e:
		if x > ma:
			ma = x
n = ma		

st = "R.<"
for i in range(n):
	st = st + "z" + str(i+1) + ","
for i in range(n):
	st = st + "y" + str(i+1) + ","
for i in range(n):
	if i != n-1:
		st = st + "x" + str(i+1) + ","
	else:
		st = st + "x" + str(i+1) + ">"	
st =st + " = PolynomialRing(QQ, order='neglex')"






strings.append(st)
for i in range(len(edges)):
	st = "M{} = matrix([[".format(i+1)
	for j in range(len(edges[i])):
		if edges[i][j] != edges[i][len(edges[i])-1]:
			st = st + "x{},".format(edges[i][j])
		else:
			
			st = st + "x{}],".format(edges[i][j])
	st = st + "["
	for j in range(len(edges[i])):
		if edges[i][j] != edges[i][len(edges[i])-1]:
			st = st + "y{},".format(edges[i][j])
		else:
			st = st + "y{}],".format(edges[i][j])
	st = st + "["		
	for j in range(len(edges[i])):
		if edges[i][j] != edges[i][len(edges[i])-1]:
			st = st + "z{},".format(edges[i][j])
		else:
			st = st + "z{}]".format(edges[i][j])
	st = st+'])'
	strings.append(st)
st = "I = ideal("	
for i in range(len(edges)):
	if i != len(edges)-1:
		st = st+"M{}.det(),".format(i+1)
	else:
		st = st+"M{}.det())".format(i+1)
strings.append(st)
strings.append("from sage.rings.polynomial.toy_buchberger import *")


with open ("sage.txt","w")as f1, open("buch.txt","r") as f2:
   for line in strings:
       f1.write(line+"\n")
   for line in f2:
   	   f1.write(line+"\n") 	   



st = "G = buchberger1(I)\nprint 'Grobnerbasis'\nG\nprint buchberger(I)"
with open ("sage.txt","a") as f1:
	f1.write(st)

