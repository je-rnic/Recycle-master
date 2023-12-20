import os
import image_p

def send():
    image_p.pic()
    os.system(r"sshpass -p '*0103549a' scp /home/pi/cam/capture.jpg nickie@10.143.209.103:'C:\Users\nicki\PycharmProjects\hackathon\python_main\test_images'")
    os.system(r"sshpass -p '*0103549a' ssh nickie@10.143.209.103 'cd C:\Users\nicki\PycharmProjects\hackathon\python_main && C:\Users\nicki\PycharmProjects\hackathon\venv\Scripts\python.exe  main_user.py'")
