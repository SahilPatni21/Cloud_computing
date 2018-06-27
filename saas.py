#!/usr/bin/python2


import time              #for accessing the time library
import os                #for accessing the O.S library


#use to display the valid options for the user to select
x='''
Press 1  to access Firefox  :
Press 2  to access vlc  :
Press 3  to access text editor  :
Press 4  to access calculator   :
'''

#to print option for user
print  x

#to allow user to input option
ch=raw_input("enter your choice : ")

if  ch  ==  '1'  :
	print  "Please wait firefox is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of firefox from server 
	os.system('ssh  -l   '+user+'  10.0.7.134  -X  firefox')

elif  ch  ==   '2'  :
	print  "plz wait vlc is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of vlc from server 
	os.system('ssh  -l   '+user+'  10.0.7.134  -X  vlc')

elif   ch ==  '3'  :

	print  "please wait text editor is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of gedit from server
	os.system('ssh  -l   '+user+'  10.0.7.134  -X  gedit')

elif  ch  ==  '4'  :
	print  "plz wait calculator is about to start..."
	time.sleep(2)
	user=raw_input("enter cloud user :  ")
	#to connect with server using Secure Shell (SSH)
	#to get access of calculator from server
	os.system('ssh  -l   '+user+'  10.0.7.134  -X  gnome-calculator')


else : 
	#if no valid option is selected by the user from the list
	print  "Wrong choice, please choose a valid option ! "
	print  "closing  programe"
	time.sleep(2)
	exit()
