import threading
import time
import random

is_running = True
light_intensity = 100   # 0 = gelap, 100 = terang
motion_detected = False

lamp_state = 0  # 0 = mati, 1 = nyala

def task_sensor():
    global light_intensity, motion_detected, is_running
    
    while is_running:
        light_intensity = random.randint(0, 100)
        motion_detected = random.choice([True, False])
        
        print(f"[SENSOR] Cahaya: {light_intensity} | Gerakan: {motion_detected}")
        
        time.sleep(1)

def task_control():
    global lamp_state, is_running
    
    while is_running:
        if light_intensity < 40 and motion_detected:
            if lamp_state == 0:
                print("[KONTROL] Lampu dinyalakan (gelap & ada gerakan)")
                lamp_state = 1
        
        else:
            if lamp_state == 1:
                print("[KONTROL] Lampu dimatikan")
                lamp_state = 0
        
        time.sleep(0.5)

def task_timer():
    global is_running
    time.sleep(10)
    print("\n[TIMER] Sistem dihentikan otomatis\n")
    is_running = False

if __name__ == "__main__":
    print("======================================")
    print("        SISTEM LAMPU OTOMATIS         ")
    print("======================================")

    t1 = threading.Thread(target=task_sensor)
    t2 = threading.Thread(target=task_control)
    t3 = threading.Thread(target=task_timer)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("======================================")
    print("         SISTEM SELESAI               ")
    print("======================================")
