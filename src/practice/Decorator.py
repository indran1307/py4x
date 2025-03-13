import time


def decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Difference is ", end_time-start_time)
    return wrapper()

@decorator
def test_ui():
    print("Add a function, time taken by this function")
    time.sleep(3)