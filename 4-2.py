def MotifTATA(sequence):
    'Finding occurrences of TATA motif in a sequence.'
    output=''

    #return the occurrence of TATA
    num=0
    
    running=True

    find = 0
    while running:
        if sequence.find('TATA') > -1:
            find = find + sequence.find('TATA')
            print('start',find +1, 'end', find +4)
            #sequence=sequence[find+1:]
            #find = find +1
            sequence=sequence[find+4:]
            find = find +4
            num = num +1
        else:
            running = False
    print('Found',num, 'TATA motif')

sequence='TATACCAFTATA'
MotifTATA(sequence)
            
