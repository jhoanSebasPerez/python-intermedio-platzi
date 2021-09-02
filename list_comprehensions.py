def run(): 
    cube = {i: round(i**(1/2), 3)for i in range(1, 1001)}

    print(cube)

if __name__ == "__main__": 
    run()