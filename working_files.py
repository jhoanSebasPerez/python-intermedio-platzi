def read(): 
    numbers = []
    with open("./archivos/numbers.txt", 'r', encoding='utf-8') as f: 
        for item in f: 
            numbers.append(int(item)) 
    print(numbers)


def write(): 
    names = ['Jhoan', 'Gilberto', 'Mauricio', 'Renata']
    with open("./archivos/names.txt", 'w') as f: 
        for name in names: 
            f.write(f'{name}\n')

def run(): 
    write()

if __name__ == "__main__": 
    run()