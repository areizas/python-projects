import time

def time_it(func):
  def wrapper(*args, **kwargs):
    tic = time.time()
    result = func(*args, **kwargs)
    toc = time.time() - tic
    print(f"Execution time: {toc:.6f} seconds")
    return result
  return wrapper

@time_it
def sumNumbers(x,y):
  return x+y

@time_it
def simulateLongTime():
  time.sleep(2)

if __name__ == '__main__':
  sumNumbers(1,2)
  simulateLongTime()