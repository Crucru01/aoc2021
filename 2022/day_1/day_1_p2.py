

f = open("2022\day_1\input.txt","r")
listOfLines=f.readlines()

#adjusting input and calculating subTotals
res = []
subtotal=0

for sub in listOfLines:
    
    sub=sub.replace("\n","")

    if(sub==""):
        res.append(subtotal)
        subtotal=0
        sub="0"
        
    subtotal= subtotal+int(sub)

#find top three highest values in the array

sortedRes = sorted(res,reverse=True)

print(sortedRes[0]+sortedRes[1]+sortedRes[2])
   


