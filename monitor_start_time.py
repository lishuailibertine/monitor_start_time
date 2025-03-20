import os
from datetime import datetime
import time
from pynput import keyboard, mouse

LOG_FILE = os.path.join(os.getcwd(), "work_log.txt")  # 修改为当前工程根目录

def get_today_log():
    """检查今天是否已经记录过"""
    if not os.path.exists(LOG_FILE):
        return None
    
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    
    today = datetime.now().strftime("%Y-%m-%d")
    for line in lines:
        if line.startswith(today):
            return line.strip()
    
    return None

def log_start_time():
    """记录当天第一次使用电脑的时间"""
    if get_today_log():
        return
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(now + "\n")
    
    print(f"✅ 记录成功: {now}")

def on_activity(event):
    """检测到鼠标或键盘活动后记录时间"""
    log_start_time()
    exit(0)  # 记录后退出程序

if __name__ == "__main__":
    print("📌 监控中... 等待用户活动")

    while True:
        if not get_today_log():
            # 监听键盘和鼠标活动
            print("✅ 监听键盘和鼠标活动")
            listener1 = keyboard.Listener(on_press=on_activity)
            listener2 = mouse.Listener(on_move=on_activity, on_click=on_activity, on_scroll=on_activity)
            
            listener1.start()
            listener2.start()

            listener1.join()
            listener2.join()
        else:
            print("✅ 今天已经记录过了")
        
        # 等待一段时间后再检查
        time.sleep(30)  # 每60秒检查一次