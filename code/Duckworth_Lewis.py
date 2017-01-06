import collections
import copy 

from prettytable import PrettyTable

def DLMethod(oppScore,scoreDict):
    for key,value in scoreDict.items():
        score=value[0]
        wickets=value[1]
        overs,balls=str(key).split(".")
        if int(overs)%10==0 and int(balls)==0:
            ballsPerc=0.1666*int(balls)
            overPerc=int(overs)+ballsPerc
            overLeft=50-overPerc
            wicketLeft=10-wickets
            arr=[0,0.1,0.1,0.2,0.2,0.3,0.3,0.4,0.4,0.5,0.5]
            if overLeft>40:
                scale=5-arr[wickets]
            elif overLeft>30:
                scale=4.5-arr[wickets]
            elif overLeft>20:
                scale=4-arr[wickets]
            elif overLeft>10:
                scale=3.5-arr[wickets]
            elif overLeft>0:
                scale=3-arr[wickets]
            predScore=oppScore*(100-(overLeft*wicketLeft/scale))/100
            if predScore<=score:
                print("Prediction at "+str(key)+":Team batting second will win")
            else:
                print("Prediction at "+str(key)+":Team batting second will lose")

f=open("CricFinal.txt",'r')
#print f.read()
data=f.read()
one=data.split('\n')
#print one[1]
one.reverse()
#print one[1]
#print len(one)
bat_bowl=one[1].split(',')[0]
bowler=bat_bowl.split("to")[0]
batsmen=bat_bowl.split("to")[1]
#print bat_bowl,bowler,batsmen

bowler_details=collections.OrderedDict()
batsmen_details=collections.OrderedDict()
prev="a"
count=0

############Overs calculation STARTS#################


f=open("CricOvers.txt",'r')
overs=f.read()
overs=overs.split('\n')
overs.reverse()

z=overs.index('0.1')
overs[z]=0
end=overs.index('0.1')
#print end
#print overs[end]
second_innings=overs[309:]
for i in range(len(second_innings)):
    y=second_innings[i].split('.')
    if(int(y[1])>5):
        second_innings[i]=float(second_innings[i])+0.4


#print second_innings
SecWickets=0
SecScore=0
Sec_details=collections.OrderedDict()
bowler_first=collections.OrderedDict()
batsmen_first=collections.OrderedDict()


scores=[]
############Overs calculation ENDS###################
target=0
j=0
for i in range(1,len(one)):
    if(i==int(end)):
        count+=1
        bowler_details[prev][0]+=1
        bowler_first= copy.deepcopy(bowler_details)
        batsmen_first= copy.deepcopy(batsmen_details)
        bowler_details.clear()
        batsmen_details.clear()
        Sec_details.clear()
        target=SecScore
        SecWickets=0
        SecScore=0
        
    
    split_one=one[i].split(',')
    bat_bowl=split_one[0]
    
    score=split_one[1]
    bowler=bat_bowl.split("to")[0]
    batsmen=bat_bowl.split("to")[1]
    
    try:
        bowler_details[bowler]
    except KeyError:
        bowler_details[bowler]=[0,0,0]
    try:
        batsmen_details[batsmen]
    except KeyError:
        #print batsmen_details
        batsmen_details[batsmen]=[0,0,0,0]
    
    if("byes" in score):
        byes="yes"
        score=split_one[2]
    if("no ball" in score):
        #print score
        bowler_details[bowler][1]+=1
        score=split_one[2]
        SecScore+=1
    elif("wide" in score):
        if(str(5) in score):
            bowler_details[bowler][1]+=5
            SecScore+=5
        if(str(4) in score):
            bowler_details[bowler][1]+=4
            SecScore+=4
        elif(str(3) in score):
            bowler_details[bowler][1]+=3
            SecScore+=3
        elif(str(2) in score):
            bowler_details[bowler][1]+=2
            SecScore+=2
        else:
            bowler_details[bowler][1]+=1
            SecScore+=1
    if(("FOUR" in score or "four" in score) and "wide" not in score):
        #print score
        bowler_details[bowler][1]+=4
        batsmen_details[batsmen][0]+=4
        batsmen_details[batsmen][1]+=1
        batsmen_details[batsmen][3]+=1
        SecScore+=4
    elif("1" in score and "wide" not in score):
        #print one[i]
        if(byes=="no"):
            batsmen_details[batsmen][0]+=1
            bowler_details[bowler][1]+=1
            batsmen_details[batsmen][3]+=1
        
        SecScore+=1
    elif("2" in score and "wide" not in score):
        #print score
        if(byes=="no"):
            batsmen_details[batsmen][0]+=2
            bowler_details[bowler][1]+=2
            batsmen_details[batsmen][3]+=1
        
        SecScore+=2
    elif("3" in score and "wide" not in score):
        #print score
        if(byes=="no"):
            batsmen_details[batsmen][0]+=3
            bowler_details[bowler][1]+=3
            batsmen_details[batsmen][3]+=1

        SecScore+=3
    elif("SIX" in score or "six" in score):
        #print score
        bowler_details[bowler][1]+=6
        batsmen_details[batsmen][0]+=6
        batsmen_details[batsmen][2]+=1
        batsmen_details[batsmen][3]+=1
        SecScore+=6
    elif(("OUT " in score or "out " in score)and "Run" not in score):
        #print one[i]
        #count+=1
        #print bowler
        bowler_details[bowler][2]+=1
        batsmen_details[batsmen][3]+=1
        SecWickets+=1
    elif("wide" not in score ):
            #print score
            batsmen_details[batsmen][3]+=1
    #print SecScore,SecWickets
    byes="no"
    try:
        
        if(i>=end):
            #print second_innings[i-end]
            Sec_details[str(second_innings[i-end])]=[SecScore,SecWickets]
            #print second_innings[j],SecScore,SecWickets
    except IndexError:
        pass
    j+=1
    if(prev!=bowler):
        #print i,prev,bowler
        try:
            bowler_details[prev][0]+=1
        except KeyError:
            a=1
    prev=bowler



#print Sec_details
print "---------------------------------------"

print "FIRST INNINGS"

t=PrettyTable(["BATSMEN","Runs","Balls","FOUR'S","SIXES","StrikeRate"])
s=0
for i in batsmen_first:
        s+=batsmen_first[i][3]
        strk=(batsmen_first[i][0]/float(batsmen_first[i][3]))*100
        t.add_row([i,str(batsmen_first[i][0]),str(batsmen_first[i][3]),str(batsmen_first[i][1]),str(batsmen_first[i][2]),str(round(strk,2))])
print t


t=PrettyTable(["BOWLER","OVERS","RUNS","WICKETS","EconomyRate"])

for i in bowler_first:
        eco=bowler_first[i][1]/float(bowler_first[i][0])
        t.add_row([i,str(bowler_first[i][0]),str(bowler_first[i][1]),str(bowler_first[i][2]),str(round(eco,2))])
print t

print "--------------------------------------------------------------------------"
print "SECOND INNINGS"

t=PrettyTable(["BATSMEN","Runs","Balls","FOUR'S","SIXES","StrikeRate"])
z=0
for i in batsmen_details:
        z+=batsmen_details[i][3]
        strk=(batsmen_details[i][0]/float(batsmen_details[i][3]))*100
        t.add_row([i,str(batsmen_details[i][0]),str(batsmen_details[i][3]),str(batsmen_details[i][1]),str(batsmen_details[i][2]),str(round(strk,2))])
print t

t=PrettyTable(["BOWLER","OVERS","RUNS","WICKETS","EconomyRate"])
for i in bowler_details:
        eco=bowler_details[i][1]/float(bowler_details[i][0])
        
        t.add_row([i,str(bowler_details[i][0]),str(bowler_details[i][1]),str(bowler_details[i][2]),str(round(eco,2))])
print t


DLMethod(target,Sec_details)
















