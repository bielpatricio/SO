#print("SO")

def FCFS(lista_e, fcfs, tempo_atual, tret, tresp):

    if fcfs:    #caso tenha processos a executar
        #print('tempo atual = ', tempo_atual)
        #print(lista_e)
        #print(fcfs)

        for x in fcfs:  #adicionando processos na lista 
                        #se o tempo de chegada for igual ao tempo atual
            if x[0] == tempo_atual:
                lista_e.append(x)
        if lista_e: #caso tenha processos na fila de prioridades
            if lista_e[0][1]==lista_e[0][2]:    #Caso o processo esteja executando pela primeira vez
                tresp = tresp + tempo_atual - lista_e[0][0]

            lista_e[0][1] = lista_e[0][1]-1

            if lista_e[0][1]==0:    #caso processo termine
                tret = tret + tempo_atual - lista_e[0][0]+1
                lista_e.pop(0)
                fcfs.pop(0)

        tempo_atual = tempo_atual+1
        return FCFS(lista_e, fcfs, tempo_atual, tret, tresp)
    else:   #caso não tenha processos a executar
        #print(tempo_atual)
        tresp = tresp/num_process
        tesp_fcfs = tresp
        tret = tret/num_process
        #print(tefcfs)
        return tret, tresp, tesp_fcfs

def SJF_SP(lista_e, sjf, tempo_atual, tret, tresp):
    
    if sjf: #caso tenha mais processos a executar
        #print('tempo atual = ', tempo_atual)
        #print(lista_e)
        #print(sjf)
        for x in sjf:   #adicionando processos na lista 
                        #se o tempo de chegada for igual ao tempo atual
            if x[0] == tempo_atual:
                lista_e.append(x)
            if lista_e and lista_e[0][1]==lista_e[0][2]:
                    lista_e.sort(key=lambda y: y[1])
                
        if lista_e: #caso tenha processos na fila de prioridades
            if lista_e[0][1]==lista_e[0][2]:    #Caso o processo esteja executando pela primeira vez
                tresp = tresp + tempo_atual - lista_e[0][0]
                #print('temp resp = ', tresp)

            lista_e[0][1] = lista_e[0][1]-1
            if lista_e[0][1]==0:    #caso processo termine
                tret= tret + tempo_atual - lista_e[0][0]+1
                #print('temp retorno = ', tret)
                lista_e.pop(0)
                sjf.pop(0)

        tempo_atual = tempo_atual+1
        return SJF_SP(lista_e, sjf, tempo_atual, tret, tresp)
    else:   #caso não tenha mais processos a executar
        #print(tempo_atual_fcfs)
        tresp = tresp/num_process 
        tesp = tresp
        tret = tret/num_process
        #print(tefcfs)
        return tret, tresp, tesp

def RR(lista_e, rr2, tempo_atual, tret, tresp, tesp, q):
    quantum = 2
    if rr2: #caso tenha processos a executar
        #print('tempo atual = ', tempo_atual)
        #print(lista_e)
        #print(rr2)
        for x in rr2:   #adicionando processos na lista 
                        #se o tempo de chegada for igual ao tempo atual
            if x[0] == tempo_atual:  
                lista_e.append(x)
        
        if lista_e and q==quantum:  #caso tenha processos na fila de prioridades
            if len(lista_e)>1 and tempo_atual>lista_e[0][0]:
                lista_e.append(lista_e[0])
                lista_e.pop(0)
                rr2.append(rr2[0])
                rr2.pop(0)
            q=0

        if lista_e:
            if lista_e[0][1]==lista_e[0][2]:    #Caso o processo esteja executando pela primeira vez
                tresp = tresp + tempo_atual - lista_e[0][0]
                #print('tresp =', tresp)
                
            #tesp = soma 1 para cada processo que esteja na fila, menos o que está executando
            tesp = tesp + (len(lista_e)-1)
            #print('tempo de espera = ', tesp)

            lista_e[0][1] = lista_e[0][1] -1
            
            if lista_e[0][1] == 0:  #caso processo termine
                tret = tret + tempo_atual - lista_e[0][0]+1
                #print('tempo de retorno = ', tret)
                #elimina na fila de prioridade e na lista de processos a executar
                lista_e.pop(0)
                rr2.pop(0)
                q=-1
        tempo_atual = tempo_atual +1

        if lista_e:
            if q<quantum:
                q=q+1
        else:
            q=0
        return RR(lista_e, rr2, tempo_atual, tret, tresp, tesp, q)
    else:   #caso não tenha mais processos a executar
        tesp = tesp/num_process
        tret = tret/num_process
        tresp = tresp/num_process
        return tret, tresp, tesp

#################################################################
#ler arquivo

def format_lin(linha):
    linha = linha.split()
    elemento = map(lambda x: int(x), linha)
    #print(elemento)
    return list(elemento)

process = open("proj1.txt", "r")
processo = map(lambda linha: format_lin(linha), process)
processo = list(processo)
#print(processo)
processo = filter(lambda x: x[1]>0, processo)
processo = list(processo)
num_process = len(processo)
process.close()
from copy import deepcopy
#################################################################
#[processo][tempo de chegada, duração]
#print(processo)
#Saida = tempo de retorno, tempo de resposta, tempo de espera
fcfs = deepcopy(processo)
fcfs = list(fcfs)
#print(fcfs)
#processos, tempo atual,tempo de retorno, tempo de resposta atual
print('FCFS', end = ' ')
for x in range(len(fcfs)):
    fcfs[x].append(fcfs[x][1])
lista_e = []
fcfs = FCFS(lista_e, fcfs, 0, 0, 0)
for k in fcfs:
    print(round(k, 1), end = ' ')
print()
#################################################################
#processos - lista_e, arquivo, tempo atual,tempo de retorno, tempo de resposta atual
sjf = deepcopy(processo)
sjf = list(sjf)
lista_e = []
for x in range(len(sjf)):
    sjf[x].append(sjf[x][1])
print('SJF', end=' ')
sjf = SJF_SP(lista_e, sjf, 0, 0, 0)
#map(lambda x : print(x), sjf)
for k in sjf:
    print(round(k, 1), end = ' ')
print()
#################################################################
##processos - lista_e, arquivo, tempo atual,tempo de retorno, tempo de resposta atual, q
from copy import deepcopy
lista_e = []
rr2 = deepcopy(processo)
#print(rr2)
for x in range(len(rr2)):
    rr2[x].append(rr2[x][1])

rr = RR(lista_e, rr2, 0, 0, 0, 0, 0)
print('RR', end=' ')
for k in rr:
    print(round(k, 1), end = ' ')
#################################################################
