from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(str(time_elapsed.total_seconds()) + " seconds elapsed")
    return wrapper

@execution_time
def random_func():
    for _ in range(1,100000000):
        pass

@execution_time
def sum(a: int, b: int) -> int:
    return a + b

def run():
    vfor = random_func()
    vsum = sum(4,7)
    print("For: ", vfor)
    print("Sum: ", vsum)

if __name__ == '__main__':
    run()