def index_mapping(input_list):
    hash_array = [-1] * len(input_list)     #tühi massiiv
    for i in range(len(input_list)):       
        hash_value = i % len(input_list)            
        hash_array[hash_value] = input_list[i] # salvestab räsi omale kohale    
    return hash_array

input_data = [10, 20, 30, 40, 50] #algandmed
hashed_data = index_mapping(input_data)

print("Räsitud andmed on :", hashed_data)

