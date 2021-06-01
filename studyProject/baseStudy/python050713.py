import schedule
import time


def job():
    print('哈哈------')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
