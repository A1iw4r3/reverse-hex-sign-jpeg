def getHex(input_file, output_file):
    # Read the binary file and convert to hex
    with open(input_file, 'rb') as f:
        hex_data = f.read()
    file_hex = hex_data.hex()

    # Write the hex data to output file
    with open(output_file, 'w') as f:
        f.write(file_hex)

    # Read the hex data from the output file
    with open('analyze.txt', 'r') as f:
        data = f.read()

    # Split the data into chunks of 8 characters
    array_data = [data[i:i+8] for i in range(0, len(data), 8)]
    #result = ', '.join(array_data)
    return array_data
    # Write the formatted array data to a file
    #with open('array.txt', 'w') as f:
     #   f.write(result)

def reverse_hex_strings(hex_strings):
    reversed_hex_strings = []
    for hex_string in hex_strings:
        # Reverse each hex string by chunks of 2 characters
        reversed_hex_string = ''.join(reversed([hex_string[i:i+2] for i in range(0, len(hex_string), 2)]))
        reversed_hex_strings.append(reversed_hex_string)

    return reversed_hex_strings

# Example of usage
input_file = 'challengefile'
output_file = 'analyze.txt'
hex = getHex(input_file, output_file)

# Example hex string list 
reversed_hex = reverse_hex_strings(hex)



#result = ', '.join(reversed_hex)

with open('flag.jpg','wb') as f:
	for i in reversed_hex:
		f.write(bytes.fromhex(i))