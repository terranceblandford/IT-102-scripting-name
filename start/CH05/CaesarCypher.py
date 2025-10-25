#CaesarCypher
#Terrance Blandford

msg = input("Enter a message: ")
shift = int(input("Enter the shift value (1-25):"))

result = ""
for ch in msg:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch) - base + 
shift) % 26 + base)
    else:
            result += ch

print("Encrypted message:", result)

if input("Decrypt the message? (yes/no): ").lower() == "yes":
    decrypted = ""
    for ch in result:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            decrypted += chr((ord(ch) - base - shift) % 26 + base)
        else:
                decrypted += ch
        print ("Decrypted message:", decrypted)
