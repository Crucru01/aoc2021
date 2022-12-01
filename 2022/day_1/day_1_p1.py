
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

#find max in the array

currentMax=0
#handmade way to find max
# for i in res:
#     if(i>currentMax):
#         currentMax=i
   
print(max(res))

