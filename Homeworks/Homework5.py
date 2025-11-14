from datetime import datetime as dt

time_now = dt.now()

def checktime(func):
  def wrapper():
      time_now = dt.now()
      print(f"Функция была вызвана в {time_now.strftime('%H:%M:%S %d/%m/%Y')}")
  func()
  return wrapper


@checktime
def hello_world():
    print("hello world")

hello_world()