# CaptureCode
A mobile app for safely storing your precious passwords physically.

## Installation
You will need to install the dependencies for this program.
In command prompt do the following:
```
pip install pycryptodome
```

## Usage
You will first need to run **key_gen.py**. This will generate your public and private keys in a .pem file format.
> PEM or Privacy Enhanced Mail is a Base64 encoded DER certificate. PEM certificates are frequently used for web servers as they can easily be translated into readable data using a simple text editor.

Next, run **textformat.py**. This will take an input, encrypt it using your public key, and format it into an image which will look similar to ![CODE](https://user-images.githubusercontent.com/84883805/172512765-a54cb09b-152e-4ac7-9d6e-4c9fc2ec2669.png).
> **This image contains your secret message. However, without your private key (private.pem) they will be unable to read it. Please keep your private key as safe and private as possible.**

Finally, you are able to run **textdecrypt.py** which will scan your image and use your private key to decrypt the information and repeat your secret message back to you.

## Version info
Recent version: v1.0.0
Stable version: v1.0.0
