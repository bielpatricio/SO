#print("proj 2 - Faltas de espaço na memória")

def FIFO(fifo, memory2, tam_memory, faltas, count): 
    """[FIFO]

    #fifo é a memória
    memory2 é os valores que tem que entrar na memória
    
    Returns:
        [Número de faltas] --
        [Vai contando e adicionando
        na ordem, no primeiro espaço,
        no segundo espaço, no terceiro
        espaço...]
    """   
    #print(fifo)
    test = memory2[0] in fifo
    if not test:
        faltas = faltas+1
        if len(fifo) == tam_memory:
            fifo[count] = memory2[0]
            count = count+1 #responsavel por dizer qual espaço
                            #de memoria será add
        else:
            fifo.append(memory2[0])
    memory2.pop(0)
    if count == tam_memory:    
        count = 0

    if memory2:
        return FIFO(fifo, memory2, tam_memory, faltas, count)
    else:
        return faltas

def OTM(otm, memory3, tam_memory, faltas):
    """[OTM]
    
    Arguments:
        otm {[vector]} -- [memória]
        memory3 {[vector]} -- [valores a entrar na memória]
        faltas {[int]} -- [contando as faltas para cada valor que irá entrar]
    
    Returns:
        [int] -- [faltas]
    """    
    #print(otm)
    modfy = 0
    sai = False
    test = memory3[0] in otm
    
    if not test:
        faltas = faltas+1
        #checa quantas vezes cada valor da memoria ainda vai aparecer
        if len(otm) == tam_memory: #Se a memoria tiver cheia
            for tryy in otm:    #percorre cada espaço da memória já preenchido
                count = 0;
                for look in memory3: #percorre os valores da memoria a ser acrescentado
                    count = count+1 #espaços que o valor ainda não apreceu
                    #print("count - ", count)
                    #print(" memoria - ", len(memory3))
                    if tryy == look:    #checa se ele tá aparecendo na memória
                        if count > modfy: #checa se foi ele é o valor da memória que irá aparecer mais longe
                            modfy = count
                            num = tryy
                            break
                    if count == len(memory3): #indica que ele não irá mais aparecer
                        num = tryy
                        sai = True
                        break
                if sai:
                    break
            pos = otm.index(num)
            otm[pos]=memory3[0] 
        else:
            otm.append(memory3[0]) #joga na memória

    memory3.pop(0) #remove o valor que já foi add na memória

    if memory3:
        return OTM(otm, memory3, tam_memory, faltas)
    else:
        return faltas

def LRU(lru, memory, tam_memory, faltas, loc):
    """[summary]
    
    Arguments:
        lru {[vector]} -- [memória]
        memory {[vector]} -- [a entrar na memória]
        tam_memory {[int]} -- [tamanho da memória]
        faltas {[int]} -- [quando a memória ta cheia]
        loc {[int]} -- [local onde se encontra o valor
        a ser colocado na memória no memory]
    
    Returns:
        [int] -- [faltas]
    """    
    
    modfy = 0
    sai = False
    test = memory[loc] in lru
    
    if not test:
        faltas = faltas+1
        if len(lru) == tam_memory:
            for tryy in range(len(lru)): #percorre os valores da memória
                count = loc
                casa = 0
                #print("loc da lista -", tryy)
                while(count>=0):
                    count = count-1 #percorre os valores anteriores do memory
                    casa = casa+1 #distancia
                    #print("tst - ", lru[tryy])
                    #print(" tst2 - ", memory[count])
                    if lru[tryy] == memory[count]: #checa se achou o valor da memória nos valores
                                                    #anteriores do memory
                        #print("count - ", count)
                        #print("modfy - ", modfy)
                        if casa > modfy: #checa o valor que mais longe do local atual do memory
                            modfy = casa
                            num = tryy
                            #print("go- ", num)
                        break
                    if count == 0: #caso só apareceu no primeiro valor do memory
                        num = tryy
                        sai = True
                        break
                if sai:
                    break
            lru[num]=memory[loc] #add na memória
        else:
            lru.append(memory[loc])
    #print(loc)
    loc = loc+1
    #print(lru)
    if loc<len(memory):
        return LRU(lru, memory, tam_memory, faltas, loc)
    else:
        return faltas

memory = open("proj2.txt", "r")
memory = list(memory)
memory = map(lambda num: int(num), memory)
memory = list(memory)
#print(memory)

tam_memory = memory[0]
memory.pop(0)
#print(memory)

from copy import deepcopy
#####################################################################
memory2 = deepcopy(memory)

fifo = []
# FIFO (memória, entrar na memória, tamanho da memória, faltas, local de inicio da memoria)
print("FIFO ", FIFO(fifo, memory2, tam_memory, 0, 0)) 
#####################################################################
memory3 = deepcopy(memory)
#print(memory3)
otm = []
#OTM (memória, entrar na memória, tamanho da memória, faltas)
print("OTM ", OTM(otm, memory3, tam_memory, 0))
#####################################################################
#print(memory)
lru = []
# LRU (memória, entrar na memória, tamanho da memória, faltas, local de inicio da memoria)
print("LRU ", LRU(lru, memory, tam_memory, 0, 0))
