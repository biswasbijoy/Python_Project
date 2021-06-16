#Email slicer python project.
import sys
#Take input untill user want to stop
while True :

    #Enter email addres..
    email = input("Enter your email address or 'x' to stop: ")
    if email == 'x' :
        sys.exit()
    else :
        #find username. if email adress is abc@gmail.com, username is abc
        username = email[:email.index('@')]

        #domain name. if email adress is abc@gmail.com, Domain is gmail.com
        domain = email[email.index('@') + 1: ]
 
        # Now print output
        print(f'Username   : {username} \nDomain name: {domain}')