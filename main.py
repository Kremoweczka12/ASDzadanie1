
from datetime import datetime


def lewy(i):
    return 2*i+1

def prawy(i):
    return lewy(i)+1

def kopcuj(i,tabela):
    try:
        i=i
        check = tabela[lewy(i)]
        check1=lewy(i)
        try:
            if(tabela[prawy(i)]>tabela[lewy(i)]):
                check = tabela[prawy(i)]
                check1 = prawy(i)
        except:
            pass
    except:
        return tabela
    if(check>tabela[i]):
        tabela[i], tabela[check1] = tabela[check1], tabela[i]
        tabela1=tabela
        tabela=kopcuj(check1, tabela)
        if(tabela1==tabela):
            return tabela
    else:
        return tabela


def createkopiec(tabela):
    i=0
    leng = len(tabela)//2
    while leng>=0:
        tabela = kopcuj(leng,tabela)
        leng-=1
    return tabela

#print(kopcuj(2,[27,17,3,16,13,10,1,5,7,12,4,8,9,0]))
#print(createkopiec([4,1,3,2,16,9,10,14,8,7]))


def sortujprzezkopcowanie(tabela):
    i=0
    final = []
    lg = len(tabela)
    while i < lg:
        createkopiec(tabela)
        final.append(tabela[0])
        final=[final[-1]]+final[0:-1]
        tabela=tabela[1:]
        i+=1
    return final

#print(sortujprzezkopcowanie([16,14,10,8,7,9,3,2,4,1]))
#print(sortujprzezkopcowanie([16,1409,10,8,7,9,3,2,4,1,1781,1543,1601]))

def bubblesort(tabela):
    while True:
        changes=0
        i=0
        j=1
        while i < len(tabela)-1:
            if(tabela[i]>tabela[j]):
                tabela[j], tabela[i] = tabela[i], tabela[j]
                changes+=1
            j+=1
            i+=1
        print(changes)
        if(changes==0):
            return tabela

#print(bubblesort([16,14,10,8,7,9,3,2,4,1]))


def mergetabels(tabela):
    if(len(tabela)>1):
        i=0
        j=0
        u=0
        c = len(tabela) // 2
        tab1=tabela[:c]
        tab2=tabela[c:]
        tabela3=[]
        mergetabels(tab1)
        mergetabels(tab2)
        while i<len(tab1) and j<len(tab2):
            if tab1[i]<tab2[j]:
                tabela[u] = tab1[i]
                i+=1
                u+=1
            else:
                tabela[u] = tab2[j]
                j+=1
                u+=1

        while i <len(tab1):
            tabela[u] = tab1[i]
            i += 1
            u+=1
        while j<len(tab2):
            tabela[u] = tab2[j]
            j += 1
            u += 1





def mergesort1(tabela):
    c=len(tabela)//2
    tab1=tabela[:c]
    tab2=tabela[c:]
    if len(tab1) ==1 or len(tab2)==1:
        tab3 = mergetabels(tab1)

def partition(table,p,r):
    x = table[r]
    i = p - 1
    for j in range(p, r):
        if table[j]<=x:
            i = i+1
            table[i], table[j] = table[j], table[i]
    table[i+1], table[r] = table[r], table[i+1]
    return i+1

def quickSort(table,p,r):
    if (p < r):
        q = partition(table, p, r)
        quickSort(table, p, q - 1)
        quickSort(table, q + 1, r)

reverse=[10,7,5,4,3,2,1,0]
allright=[1,2,3,4,5,6,7,8]
random=[5,7,3,5,2,9,1,4]


starttime=datetime.now().microsecond

quickSort(reverse,0,len(random)-1)
end=datetime.now().microsecond

starttime=round(datetime.now().microsecond)
quickSort(random,0,len(random)-1)
print(datetime.now().microsecond-round(starttime))
starttime=datetime.now().microsecond
quickSort(allright,0,len(random)-1)
print(datetime.now().microsecond-round(starttime))

reverse=[10,7,5,4,3,2,1,0]
allright=[1,2,3,4,5,6,7,8]
random=[5,7,3,5,2,9,1,4]

starttime=datetime.now().microsecond
bubblesort(reverse)
print(datetime.now().microsecond-round(starttime))
starttime=datetime.now().microsecond
bubblesort(random)
print(datetime.now().microsecond-round(starttime))
starttime=datetime.now().microsecond
bubblesort(allright)
print(datetime.now().microsecond-round(starttime))

reverse=[10,7,5,4,3,2,1,0]
allright=[1,2,3,4,5,6,7,8]
random=[5,7,3,5,2,9,1,4]

starttime=datetime.now().microsecond
sortujprzezkopcowanie(reverse)
print(datetime.now().microsecond-round(starttime))
starttime=datetime.now().microsecond
sortujprzezkopcowanie(random)
print(datetime.now().microsecond-round(starttime))
starttime=datetime.now().microsecond
sortujprzezkopcowanie(allright)
print(datetime.now().microsecond-round(starttime))

