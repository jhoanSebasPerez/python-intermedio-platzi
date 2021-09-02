def run(): 
    super_dict = {
        "natural_nums": [4,56,76,3],
        "floating_nums": [3.4, 23.5, 90.7],
        "integer_nums": [-3, -2, -1, 0]
    } 

    super_list = [
        {"first_name": "Jhoan", "last_name": "Perez"}, 
        {"first_name": "Alejandro", "last_name": "Rodriguez"},
        {"first_name": "Jimena", "last_name": "Gutierrez"}
    ]

    for key, value in super_dict.items(): 
        print(key, "-", value) 
    
    print("------------------------------------")

    for item in super_list: 
        print(item["first_name"], item["last_name"])

if __name__ == "__main__": 
    run()
