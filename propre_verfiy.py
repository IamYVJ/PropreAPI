import hashlib
from encrypt_decrypt import decrypt
from propre_tx import get_transaction

def hash_path(file_hash, hash_path):
    current_hash = file_hash
    index = 0
    is_right = True
    while index<len(hash_path):
        # print(current_hash)
        sha256 = hash_path[index:index+64]
        current_hash = hash_string(combine(sha256, current_hash))
        index+=64
    return current_hash

def combine(hash1, hash2):
    hash1 = int(hash1, 16)
    hash2 = int(hash2, 16)
    c_and = hash1 & hash2
    c_or = hash1 | hash2
    c_xor = hash1 ^ hash2
    combined = hex(c_and) + hex(c_or) + hex(c_xor)
    return combined

def hash_string(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()

def verify(transaction_id, file_hash, path_hash):

    transaction_data = get_transaction(transaction_id)

    if "Error" in transaction_data:
        return transaction_data

    transaction_data = transaction_data["data_string"]
    # print(transaction_data)
    # print('----1')
    final_hash = decrypt(transaction_data)
    # print(file_hash)
    # print('----2')
    calulated_final_hash = hash_path(file_hash, path_hash)
    # print(calulated_final_hash)
    # print('----3')
    check = final_hash==calulated_final_hash
    
    return {"verify": check}

