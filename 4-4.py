
list=['CATATGGG','CATCTGGT','CATATGAT','CTTCCGGC','CATGAGGC','CATCTCGC','CAAATGGC','CATATGGC']
print(len(list))

def Consensus(list):
    'finds the consensus sequence between a set of sequences with the same length'
    output=''

    #TEST  length
    for i in range(0,len(list)-1):
        if len(list[i]) != len(list[i+1]):
            print('Sequences should be in the same lenth.')
        elif i == len(list)-2:
            print('OK')

    ## Compare sequence
    #print(len(list[0]))
    for j in range (0,len(list)-1):
        for k in range (0,len(list[i])):
            

    
        
        


Consensus(list)





