import base64 #imports base64 module

choose = input("Encode/Decode?: ") #choose variable holding info from the input message

def encode(): #encode function
    message = input("What do you want to encode: ") #message variable holding information on what the user wants to encode 
    
    #encoding message portion
    message_bytes = message.encode("ascii") 
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")

    print(base64_message) #prints the encoded message
 
def decode(): #decode function
    message = input("What do you want to decode: ") #message variable holding information on what the user wants to decode

    #decoding message portion
    base64_bytes = message.encode("ascii") 
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode("ascii")

    print(message) #prints the decoded message

#portion to allow user to type encode and decode in lower case letters
if choose.lower() == "encode": 
    encode()
elif choose.lower() == "decode":
    decode()
