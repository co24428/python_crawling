# 리눅스에만 가능함

# pip install apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler

import time

def exec_interval():
    print("hello world")

def exec_cron():
    str = time.strftime('%c', time.localtime(time.time()))
    print("corn: " + str)

sched = BlockingScheduler()
# 5초 간격으로 exec_interval() 함수 호출
sched.add_job(exec_interval, 'interval', seconds=5)

 # 예약 방식 
sched.add_job(exec_cron, 'cron', minute="*", second="10, 30") # 매분 10초 30초에 수행
sched.add_job(exec_cron, 'cron', hour="*", minute="30") # 매시 16분에 수행

sched.start()