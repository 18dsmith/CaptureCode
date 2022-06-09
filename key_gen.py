from Crypto.PublicKey import RSA

try:
    test = open("keys/private.pem", "r")
    test.close()
    confirm = input("Are you sure you want to generate new keys?\nWARNING: This will stop previously generated codes from working.\nPlease type 'confirm' if you wish to continue or press <ENTER> to close.\n")
except:
    confirm = 'confirm'

if confirm == 'confirm':
    print("Generating keys. Please allow up to 30 seconds.")
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("keys/private.pem", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open("keys/receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()

    input("Keys generated. Press <ENTER> to close.")
else:
    exit()