import base64
def my_encode_64(string_recieved):
    base64_string =string_recieved
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64encode(base64_bytes)
    print(f"Encoded string: {sample_string_bytes}")
    sample_string =base64.b64decode(sample_string_bytes)
    print(f"Decoded string: {sample_string}")
    return;

def my_encode_64_new(string_recieved):
    base64_string =string_recieved
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64encode(base64_bytes)
    print(f"Encoded string: {sample_string_bytes}")
    return sample_string_bytes;
    
    
def my_decode_64(string_recieved):
    base64_string =string_recieved
    sample_string =base64.b64decode(base64_string)
    print(f"Decoded string: {sample_string}")
    return sample_string;
	
str=my_encode_64_new(input())
print(my_decode_64(str))