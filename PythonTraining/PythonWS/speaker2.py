# coding: utf-8
import subprocess
from datetime import datetime
import time

def jtalk(t):
    open_jtalk=['open_jtalk']
    # Diictionary file setting
    mech=['-x', '/var/lib/mecab/dic/open-jtalk/naist-jdic']
    # Sound library setting
    htsvoice=['-m', '/usr/share/hts-voice/mei/mei_happy.htsvoice']
    speed=['-r', '1.0']
    # Ouput file setting
    outwav = ['-ow', 'open_jtalk.wav']
    cmd=open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    c.stdin.write(t.encode())
    c.stdin.close()
    c.wait()
    aplay = ['aplay', '-q', 'open_jtalk.wav']
    wr = subprocess.Popen(aplay)

def say_datetime():
    d = datetime.now()
    #text = '%s月%s日、%s時%s分%s秒' % \ (d.month, d.day, d.hour, d.minute, d.second)
    #jtalk(text)
    #time.sleep(3)
    text = 'こんにちは。'
    jtalk(text)    


if __name__ == '__main__' :
    say_datetime()