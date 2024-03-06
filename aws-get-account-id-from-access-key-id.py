#!/usr/bin/env python3

import base64
import binascii
import sys

def AWSAccount_from_AWSKeyID(AWSKeyID):
    trimmed_AWSKeyID = AWSKeyID[4:]  # remove KeyID prefix
    x = base64.b32decode(trimmed_AWSKeyID)  # base32 decode
    y = x[0:6]
    
    z = int.from_bytes(y, byteorder='big', signed=False)
    mask = int.from_bytes(binascii.unhexlify(b'7fffffffff80'), byteorder='big', signed=False)
    
    e = (z & mask)>>7
    return (e)

if len(sys.argv) != 2:
  print("\nUsage: " + sys.argv[0] + " <AWS_ACCESS_KEY_ID>\n")
else:
  aws_access_key_id = sys.argv[1]
  print ("account id: " + "{:012d}".format(AWSAccount_from_AWSKeyID(aws_access_key_id)))

