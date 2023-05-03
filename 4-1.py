def GCcontent(sequence):
    'Function to return GC content of a sequence'
    output=''

    #return the GC content
    gc = 0
    for base in sequence:
        if base =='G':
            gc = gc + 1
        elif base == 'C':
            gc = gc + 1
        else:
            gc = gc + 0
        #print(gc)
        #print(len(sequence))
        output = gc/len(sequence)*100
    return output

sequence='''ATCGACC'''
#GCcontent(sequence)
print(GCcontent(sequence))
