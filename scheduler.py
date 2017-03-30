from apscheduler.schedulers.blocking import BlockingScheduler
from save_patch import save_patches

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     save_patches()
#     print('This job is run every three minutes.')

s

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=24)
def scheduled_job():
    save_patches()
    print('This job is run every weekday at 0am.')

sched.start()