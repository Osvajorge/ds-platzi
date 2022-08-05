import data

def run():
    

    python_devs = [worker["name"] for worker in data.DATA if worker["language"] == "python"]
    print('devs who use python: ')
    for worker in python_devs:
        print(worker)
    print("\n")
    
    platzi_workers = [worker["name"] for worker in data.DATA if worker["organization"] == "Platzi"]
    print(f"platzi workers:  {platzi_workers} \n")

    # adults = [worker["name"] for worker in data.DATA if worker["age"] >= 18]
    # print(adults)

    adults = list(filter(lambda worker: worker["age"] >= 18, data.DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    print('Adults: ')
    for worker in adults:
        print(worker)
    print("\n")

    olds = list(map(lambda worker: worker["age"] > 70 and worker["name"], data.DATA))
    print("Old people:\n" + ''.join([worker for worker in olds if worker != False]))
    
    


if __name__ == '__main__':
    run()