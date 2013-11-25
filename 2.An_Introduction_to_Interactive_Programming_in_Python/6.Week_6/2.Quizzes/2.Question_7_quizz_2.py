#Exemplo manipulação listas em python | exercicios quizz 6b 7
n=1000
num=range(2,n)
res=[]
k=0
while len(num) > 0:
    res.append(num[0])
    # usar list (num)!
    for i in list(num):
        if i % res[k] == 0:
            num.remove(i)
    k+=1
print res
print len (res)