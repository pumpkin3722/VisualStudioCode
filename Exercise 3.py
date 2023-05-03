participants= ['Linyi', 'Yao' , 'Tommy', 'Mummy','Daddy']  #1
participants_2 = participants
participants_3 = participants.copy() #2
participants.append('Teacher') #3
print(participants)
print(participants_2)
print(participants_3) #4
print(participants[2])
print(participants[4]) #5
participants.sort()
print(participants[2])
print(participants[4]) #6
print(participants[2][:2]) #7

ab={
    'Linyi' : 'trainee',
    'Yao' : 'trainee',
    'Tommy' : 'trainee',
    'Mummy' : 'trainee',
    'Daddy' : 'trainee',
    'Teacher' : 'trainer'
} #8

for name, role in ab.items():
    if role == 'trainee':
        print(name) #9



participants= ('Linyi', 'Yao' , 'Tommy', 'Mummy','Daddy')  
participants_2 = participants
#participants_3 = participants.copy() 
#participants.append('Teacher') 
print(participants)
print(participants_2)
#print(participants_3) 
print(participants[2])
print(participants[4]) 
#participants.sort()
print(participants[2])
print(participants[4]) 
print(participants[2][:2]) 