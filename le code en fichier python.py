# importation de photo
from scipy import misc
import matplotlib.pyplot as plt
face=misc.face()
plt.imshow(face)
plt.show()
# foncion qui cache le message
def stego(chaine,face):
    pho=face.copy()
    s=0
    for i in chaine :
        pho[s,0,0]=ord(i)
        s+=1
    return s,pho.copy()
# chacher le text hello world dans le photo stocker dans face
a,b=stego(" hello world ",face)
# fonction qui nous donne le message
def destego(s,b):
    somm=""
    for i in range(s):
        somm+=chr(b[i,0,0])
    return somm
# trouver notre message
destego(a,b)