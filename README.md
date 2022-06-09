# CaptureCode
**Currently in a very early stage of development.**

A mobile app for safely storing your precious passwords physically.

## Installation
1. Navigate to https://github.com/18dsmith/CaptureCode/releases and click on the blue _"source code"_ button at the bottom of a release.
2. Install the dependencies for this program.
In command prompt do the following:
```
pip install pycryptodome
```
From there, you are able to use the program. See below for usage instructions.

## Usage
You will first need to run **key_gen.py**. This will generate your public and private keys in a .pem file format.
> _PEM or Privacy Enhanced Mail is a Base64 encoded DER certificate. PEM certificates are frequently used for web servers as they can easily be translated into readable data using a simple text editor._

Next, run **textformat.py**. This will take an input, encrypt it using your public key, and format it into an image which will look similar to ![CODE](https://user-images.githubusercontent.com/84883805/172512765-a54cb09b-152e-4ac7-9d6e-4c9fc2ec2669.png).

> **This image contains your secret message. However, without your private key (private.pem) they will be unable to read it. Please keep your private key as safe and private as possible.**

Finally, you are able to run **textdecrypt.py** which will scan your image and use your private key to decrypt the information and repeat your secret message back to you.

## Version info
Recent version: v0.5.1

For any questions, concerns, or bug reports, [contact me](mailto:18dsmith@wakatipu.school.nz).
