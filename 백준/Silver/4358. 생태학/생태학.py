import sys

dict_list={}
total=0
while True:
	inputted=sys.stdin.readline().rstrip()
	if inputted=='':
		break
	if inputted in dict_list:
		dict_list[inputted]+=1
	else:
		dict_list[inputted]=1
	total+=1
sortdic=dict(sorted(dict_list.items()))
for i in sortdic:
	print(i,"%.4f" %((sortdic[i]/total*100)))
