def double_hashing(keys, hashtable_size, double_hash_value):  # algse hajutustabeli loomine, kus kõik väärtused on alguses None
    hashtable = [None] * hashtable_size
    
    for i in range(len(keys)):
        primary_hash = keys[i] % hashtable_size        
        if hashtable[primary_hash] is None:            #võtme lisamine
            hashtable[primary_hash] = keys[i]
        else:                                          #kui koht on hõivatud, kasutame double hashingut
            current_hash = primary_hash
            while hashtable[current_hash] is not None:
                step_size = double_hash_value - (keys[i] % double_hash_value)
                current_hash = (current_hash + step_size) % hashtable_size 
            hashtable[current_hash] = keys[i] #lisame võtme uude kohta tabelis
    
    return hashtable          #tagastan tabeli



values = [26, 54, 94, 17, 31, 45, 44, 51,66, 78, 89, 100]
table_size = 16
double_hash_value = 5

resulting_table = double_hashing(values, table_size, double_hash_value)
print("Täidetud hajutustabel:", resulting_table)
