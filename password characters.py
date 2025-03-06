list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list2=['0','1','2','3','4','5','6','7','8','9']
list3=['@','#','$','%','&','*','?','\','/','!','=','+']

password=input('enter password:')
       
def check (password):
    
if len(password)<8:
    print('password must contains at least 8 characters')

elif not password Contains '[A-Z]':
    print ('password must contains at least one capital character')
        
elif not password contains ('@','#','$','%','&','*'):
    print('password must contains at least one special character')
    
elif not password contains '[0-9]':
    print ('password must contains at least one number')
    

else:
    print ('password is valid')


