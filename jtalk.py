import subprocess
from datetime import datetime

def run(t):
    open_jtalk=['./jsay.sh', t]
    cmd = open_jtalk
    subprocess.call(cmd)

    # c.stdin.write(t)
    # c.stdin.close()
    # c.wait()
    aplay = ['aplay','-q','./talk.wav']
    wr = subprocess.Popen(aplay)

