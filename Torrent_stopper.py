import psutil
import subprocess
import time

# main variables for torrent stopping
t = input("Names of priority processes").split()

global x
x = []

for bla in t:
    x.append(bla.lower())
print (x)

global y
# This can be changed based on your needs
y = "torrent"



def pid_finder(x, y):
    # PID LISTS
    global r
    r = []
    global z
    z = []
    for proc in psutil.process_iter():
        try:
            for bla in x:
                if bla in proc.name().lower():
                    r.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    for proc in psutil.process_iter():
        try:
            if y in proc.name().lower():
                    z.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(f"r is {r}")
    print(f"z is {z}")


def stopper(r, z):
    if len(r) != 0:
        for proc in psutil.process_iter():
            if proc.pid in z:
                proc.kill()
            else:
                pass
    else:
        pass


def starter(r, z):
    if len(r) == 0:
        if len(z) == 0:
            subprocess.Popen([r'C:/CENSORED/uTorrent.exe'])
        else:
            pass
    else:
        pass


ever = True
while ever:
    pid_finder(x, y)
    stopper(r, z)
    starter(r, z)
    time.sleep(7)
else:
    pass