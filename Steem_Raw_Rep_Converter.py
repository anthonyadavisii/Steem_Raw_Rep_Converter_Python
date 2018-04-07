import math
rawrep = int(input('Enter raw reputation score:'))
rep=max(math.log10(abs(rawrep))-9,0)*(1 if(rawrep>= 0) else-1)*9+25
rep = round(rep,1)
print("Rep is calculated at "+str(rep)+" based on raw reputation score")