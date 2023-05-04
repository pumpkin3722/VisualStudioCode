#list=['CATATGGG','GATCTGGT','CATATGAT','CTTCCGGC','CATGAGGC','CATCTCGC','CAAATGGC','CATATGGC']
#print(len(list))

def Consensus(list):
    'finds the consensus sequence between a set of sequences with the same length'
    
    seq=''

    #TEST  length
    for i in range(0,len(list)-1):
        if len(list[i]) != len(list[i+1]):
            print('Sequences should be in the same lenth.')
            return
        elif i == len(list)-2:
            print('Sequence length check......PASSED!')

    ## Compare sequence
    x=[[],[],[],[]]
    for j in range (0,len(list)):
        a=0
        t=0
        c=0
        g=0
        for k in range (0,len(list[i])):
            if list[k][j] == 'A':
                a=a+1
            elif list[k][j] == 'G':
                g=g+1
            elif list[k][j] == 'C':
                c=c+1
            elif list[k][j] == 'T':
                t=t+1
        x[0].append(a)
        x[1].append(c)
        x[2].append(g)
        x[3].append(t)
    print(' A ',x[0])
    print(' C ',x[1])
    print(' G ',x[2])
    print(' T ',x[3])

    
    #Consensue sequence
    #c=[]
    seq='['
    for p in range (0,len(list)):
        lib={
            'A':x[0][p],
            'C':x[1][p],
            'G':x[2][p],
            'T':x[3][p],
        }
        #print(max(x[0][p],x[1][p],x[2][p],x[3][p]))
        for base, count in lib.items():
            if count == max(x[0][p],x[1][p],x[2][p],x[3][p]):
                #print(base)
                #c.append(base)
                seq=seq+base+', '
    seq=seq[:-2]+']'
    #print(f'Seq{c}')
    print('Seq',seq)

list=['CATATGGG','GATCTGGT','CATATGAT','CTTCCGGC','CATGAGGC','CATCTCGC','CAAATGGC','CATATGGC']
Consensus(list)