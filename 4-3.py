def Hamming(sequence_1,sequence_2):
    'calculates the hamming distance (number of base differences) between two DNA sequences.'
    output=''

    #calculates the hamming distance
    len_a=len(sequence_1)
    len_b=len(sequence_2)
    if len_a == len_b:
        print('OK')
        c=0
        for i in range(0,len_a):
            if sequence_1[i]==sequence_2[i]:
                c=c+1
        print('The Hamming distance between these two string is', c)
    else:
        print('Error: Two sequences should be in the same length')

sequence_1='ATCCGA'
sequence_2='TTCCAG'
Hamming(sequence_1,sequence_2)