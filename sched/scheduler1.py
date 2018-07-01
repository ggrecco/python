#tarefa que diz a hora
import sched
import time

scheduler = sched.scheduler()

def saytime():
    print(time.ctime())
    scheduler.enter(delay=5, priority=0, action=saytime)

saytime()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print(" >>> 99% de dano...parou de funcionar!")
