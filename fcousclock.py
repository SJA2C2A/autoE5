import time
import os

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time is up!')

    # 播放提醒音效（仅限Windows系统）
    if os.name == 'nt':
        os.system('play alarm.wav')

t = 25 * 60  # 设定计时器时间为25分钟
countdown(t)
