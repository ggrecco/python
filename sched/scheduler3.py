#Marcar um evento em um tempo determinado
import sched
import time

from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

#função zera os zera os segundo de now e soma mais 1 minuto
def rescheduler():
    new_target = datetime.now().replace(second=0, microsecond=0)
    new_target += timedelta(minutes=1)
    print(new_target)

    # scheduler.enterabs(new_target.timestamp(),priority=0, action=saytime)
    scheduler.enterabs(new_target.timestamp(),priority=0, action=google_request)


def saytime():
    print(time.ctime())


def google_request():
    from requests import get
    print(get('http://www.google.com').text)
    rescheduler()

rescheduler()

scheduler.run(blocking=True)
