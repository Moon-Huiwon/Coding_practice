#%%
base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
reverse_table = {ch: i for i, ch in enumerate(base64_table)}

def base64_decode(encoded_str):
    # 입력된 문자열에서 공백 및 '='을 제거
    # encoded_str = encoded_str.rstrip("=")
    
    # 6비트씩 분리하여 저장할 리스트
    bits = []
    
    # Base64로 인코딩된 문자열을 6비트씩 분리
    for char in encoded_str:
        bits.append(format(reverse_table[char], '06b'))
    
    # 6비트씩 모은 후 8비트로 변환
    decoded_bytes = []
    byte_str = ''.join(bits)
    
    # 8비트씩 자르기
    for i in range(0, len(byte_str), 8):
        byte_chunk = byte_str[i:i+8]
        decoded_bytes.append(int(byte_chunk, 2))
    
    # 디코딩된 바이트를 반환
    return bytes(decoded_bytes)

T = int(input())
for t in range(T):
    encoded_string = input()
    decoded_bytes = base64_decode(encoded_string)
    decoded_string = decoded_bytes.decode('utf-8')
    print(f'#{t+1} {decoded_string}')

# %%
