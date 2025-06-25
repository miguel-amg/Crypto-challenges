# +----------------------------------+
# | The Cryptopals Crypto Challenges |
# | Miguel Guimarães                 |
# +----------------------------------+

# Xor function
def xor (input1: bytes, input2: bytes):
    if len(input1) != len(input2): raise ValueError('The input sizes must be the same for XOR.') 
    
    result = bytearray(input1)
    input2_array= bytearray(input2)
    
    # XOR of each byte in the input1 array and the input2 array
    for i in range(0, len(input1)):
        result[i] = result[i] ^ input2_array[i] 
    
    return result

########################################################################################################################
# Main function
if __name__ == "__main__":
    # Hexadecimal inputs
    input1 = "1c0111001f010100061a024b53535009181c"
    input2 = "686974207468652062756c6c277320657965"

    # Inputs in byte format
    input1_bytes = bytearray.fromhex(input1)
    input2_bytes = bytearray.fromhex(input2)

    # Make the XOR
    result = xor(input1_bytes, input2_bytes)

    result_bytes = bytes(result)    # ByteArray to bytes
    result_hex = result_bytes.hex() # Bytes to hex string

    # Verify the result
    print(result_hex)
    assert result_hex == "746865206b696420646f6e277420706c6179"