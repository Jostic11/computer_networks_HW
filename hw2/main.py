import sys
import subprocess

def check_ping(host, now_mtu):
    print("Try ping with mtu = {}".format(now_mtu))
    command = ['ping', '-c', '1', host, '-M', 'do', '-s', str(now_mtu)]
    try:
        res = subprocess.run(command, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        return res.returncode == 0
    except:
        return False

def find_bounds(host):
    now_mtu = 1
    while check_ping(host, now_mtu):
        now_mtu *= 2
    return now_mtu // 2, now_mtu

args = sys.argv[1:]
if len(args) != 1:
    print("1 arguments were expected, but {} were given".format(len(args)))
    exit(1)

host = str(args[0])
if not check_ping(host, 0):
    print("Destination address {} is not available".format(host))
    exit(1)

l, r = find_bounds(host)
while l + 1 < r:
    mid = (l + r) // 2
    if check_ping(host, mid):
        l = mid
    else:
        r = mid

print("Min mtu is ", l) 