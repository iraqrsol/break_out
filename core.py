import time
import threading


class BreakOut:
    def __init__(self):
        print('Hello')
        my_time = time.strftime("%H:%M:%S")
        print(my_time)
        # time.sleep(10)
        my_time = time.strftime("%H:%M:%S")
        print(my_time)

    def myBreak(self, user_peroid):
        time_in_minutes = user_peroid * 60
        print('this break will be:', user_peroid)
        breaker = threading.Timer(time_in_minutes, self.sleelpy)
        breaker.start()

    def sleelpy(self):
        print('Welcome back')
        my_time = time.strftime("%H:%M:%S")
        print(my_time)


if __name__ == "__main__":
    a = BreakOut()
    a.myBreak(1)
