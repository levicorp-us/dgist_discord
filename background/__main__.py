import sys 
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

sys.path.append('/home/dgist/discord/dgist_discord/background')
from update_food_info import update_food_json

# 학식 정보 업데이트: 오전 8시, 오후 2시
def update_food():
    print("Update in progress...")
    update_food_json()
    print("Food info succesfully updated")

def background_process():
    scheduler = BlockingScheduler({'apscheduler.job_defaults.max_instances': 2})
    trigger = CronTrigger(year="*", month="*", day="*", hour="9", minute="0,15,30,45", second="00", timezone='Asia/Seoul')
    scheduler.add_job(update_food,trigger=trigger)
    scheduler.start()

    print("THIS SHOULD NOT BE PRINTED")

if __name__ == "__main__":
    background_process()