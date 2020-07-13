#python simple shellcode encoder.py
import os.sys
import struct
print " * Simple XOR shellcode Encoder *\n"

def xor(data):
    key = "\x01\x02\x03\x04" #XOR key
    leng = len(key)
    reverse = ""
    for i in x range(0, len(data)):
        reverse += struct.pack("B",(ord(data[i]) ^ ord(key[i%leng])) )
    return reverse

    def conv_hex(data):
        hex_str = ""
        for i in range(0, len(data)):
            hex_str += ("0x%02x" %ord(data[i]).replace('0x','\\x'))
            return hex_str
        
org_shellcode - {
    "\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
    "\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
    "\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
    "\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44"
}

xor_shellcode = ""

decoder = {
    "\xe8\xff\xff\xff\xff"
    "\xc2"
    "\x5e"
    "\x6a\x20\x59"
    "\xbf\x01\x02\x03\x04"
    "\x31\x7e\x12"
    "\x83\xc6\x04"
    "\xe2\xf8"
}
xor_shellcode = xor(org_shellcode)
print"Orginal:" + conv_hex(org_shellcode) + '\n'
print "Encoded : " +conv_hex(decoder)+conv_hex(xor_shellcode)+ '\n'
