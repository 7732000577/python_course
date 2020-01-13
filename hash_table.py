class AlgoHashTable:
    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_keynval(self,key,value):
        bucket_no = hash(key)%self.size
        bucket = self.hash_table[bucket_no]
        key_found = False
        for index,num in enumerate(bucket):
            record_key,record_value = num
            if key == record_key:
                key_found = True
                break
        if key_found:
            bucket[index] = (key,value)
        else:
            bucket.append((key,value))
    def get_val(self,key):
        bucket_no = hash(key)%self.size
        bucket = self.hash_table[bucket_no]
        key_found = False
        for index,num in enumerate(bucket):
            record_key,record_value = num
            if key == record_key:
                key_found = True
                break
        if key_found:
            return record_value
        else:
            return "record not found for this email"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = AlgoHashTable(256)
# print(hash_table)
#
# hash_table.set_keynval('hamranamehai','some info')
# print(hash_table)
# hash_table.set_keynval("hamranamehai",'some other info')
# print(hash_table)
#
# print(hash_table.get_val("hamranamehai"))

with open("test.txt") as f:
    for line in f:
        key,value  = line.rstrip().split(":")
        hash_table.set_keynval(key,value)

print(hash_table.get_val("chandra@gmail.com"))
print(hash_table.get_val("dhirukumar@gmail.com"))
