
list=['CATATGGG','CATCTGGT','CATATGAT','CTTCCGGC','CATGAGGC','CATCTCGC','CAAATGGC','CATATGGC']


def Consensus(list):
    'finds the consensus sequence between a set of sequences with the same length'
    output=''

    #TEST  length
    #for i in range(0,len(list)-1):
     #   if len(list[i]) != len(list[i+1]):
      #      print('Sequences should be in the same lenth.')
    running= True
    while running:
        i=0
        if i < len(list):
                if  len(list[i]) == len(list[i+1]):
                    i= 1+1
                print(i)
           
        else:
            print('Sequences should be in the same lenth.')
            running = False
        if i == len(list):
                print('OK')
                running = False
    return i
        


Consensus(list)





