answer = raw_input("Who's there?\n")
sup = "Sup "
period = "."
dog_data = {"Sady":{"Age":2,"Color":"Black","Description":"She's crazy."},"Buster":{"Age":15,"Color":"Carpet","Description":"He's old."}}
try: 
	dog = answer
	data = dog_data[dog]
except:
	dog = answer
	data=""
print sup+dog+period