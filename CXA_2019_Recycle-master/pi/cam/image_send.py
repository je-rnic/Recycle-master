import os
import image_p

def send():
    image_p.pic()
    os.system("rm send_pi.txt && rm new_points.txt")
    os.system(r"sshpass -p PASSWORD scp /home/pi/cam/capture.jpg nickie@10.143.209.103:'C:\Users\nicki\PycharmProjects\hackathon\python_main\test_images'")
    os.system(r"sshpass -p PASSWORD ssh nickie@10.143.209.103 'cd C:\Users\nicki\PycharmProjects\hackathon\python_main && C:\Users\nicki\PycharmProjects\hackathon\venv\Scripts\python.exe  main.py'")
