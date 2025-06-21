# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Imports
import base64

# Read fronm hexadecimal
input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
input_bytes = bytearray.fromhex(input)

# Convert to Base64
b64_bytes = base64.b64encode(input_bytes)
b64_str = b64_bytes.decode("ascii")

# Verify the output
print(b64_str)
assert b64_str == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"