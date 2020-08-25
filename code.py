string = "example@gmail.com" #samplestring

a = string.index("@") #the seperator between domain name and username

print("The user name is: " + string[0:a]) #Will print the username

print("The domain name is: " + string[a+1:]) #will print the domain name

print(string) #the original string
