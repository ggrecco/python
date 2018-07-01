#tarefa que diz a hora
import sched
import time

scheduler = sched.scheduler()

def saytime():
    print(time.ctime())

def ola():
    print('olá!!!')

def start():
    scheduler.enter(delay=10, priority=0, action=saytime)
    scheduler.enter(delay=5, priority=0, action=ola)

start()

try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print(" >>> 99% de dano...parou de funcionar!")
