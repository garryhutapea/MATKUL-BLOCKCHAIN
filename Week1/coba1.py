from eth_hash.auto import keccak
preimage = keccak.new(b'part-a')
preimage.update(b'part-b')
print(preimage.digest())