import hashlib
from math import log2, ceil
import json
from encrypt_decrypt import encrypt
from propre_tx import make_transaction

def update_path(path, hash_left, hash_right, new_hash):
    for file_name in path:
        if path[file_name]['current_hash']==hash_left:
            path[file_name]['current_hash'] = new_hash
            path[file_name]['path'] += hash_right
        elif path[file_name]['current_hash']==hash_right:
            path[file_name]['current_hash'] = new_hash
            path[file_name]['path'] += hash_left
    return path

def hash_string(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()

def combine(hash1, hash2):
    hash1 = int(hash1, 16)
    hash2 = int(hash2, 16)
    c_and = hash1 & hash2
    c_or = hash1 | hash2
    c_xor = hash1 ^ hash2
    combined = hex(c_and) + hex(c_or) + hex(c_xor)
    return combined

def save_path(path):
    with open('data_api.json', 'w') as f:
        f.write(json.dumps(path, indent=4))

def make_tree(files, hashes):
    # print(files)
    # print(hashes)
    path = dict()
    file_count = 0
    # hashes = []
    for file_name in files:
        file_hash = hashes[file_count]
        # hashes.append(file_hash)
        path[file_name] = {
            'current_hash' : file_hash,
            'path' : ''
        }
        file_count+=1

    height = ceil(log2(file_count))
    hashes = [hashes.copy()]
    for i in range(height):
        hash_count = len(hashes[i])
        row = []
        for j in range(0, hash_count, 2):
            if j<hash_count-1:
                combined_hash = hash_string(combine(hashes[i][j], hashes[i][j+1]))
                path = update_path(path, hashes[i][j], hashes[i][j+1], combined_hash)
                row.append(combined_hash)
            elif j==hash_count-1:
                row.append(hashes[i][j])
        hashes.append(row)


    # for row in hashes:
    #     print(row)
    # save_path(path)

    results = dict()
    results['Files Path'] = {}

    for file_name in path:
        results['Files Path'][file_name] = path[file_name]['path']


    root_hash = hashes[-1][-1]
    # print(root_hash)
    encrypted_hash = encrypt(root_hash)
    # print(encrypted_hash)
    tx_details = make_transaction(encrypted_hash)

    results['Transaction'] = tx_details

    return results
                
