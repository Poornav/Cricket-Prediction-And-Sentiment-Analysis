f=open("CricOvers.txt",'r')
overs=f.read()
overs=overs.split('\n')
overs.reverse()

z=overs.index('0.1')
overs[z]=0
end=overs.index('0.1')
print end
print overs[end]
second_innings=overs[309:]
for i in range(len(second_innings)):
	y=second_innings[i].split('.')
	if(int(y[1])>5):
		second_innings[i]=float(second_innings[i])+0.4

print second_innings[0]
	


