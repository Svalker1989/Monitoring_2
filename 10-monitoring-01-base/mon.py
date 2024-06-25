import time
import json
filename = time.strftime("%Y-%m-%d")+"-awesome-monitoring.log"
log = open("/var/log/"+filename,"a")
metric1 = open('/proc/loadavg')[:14]
out = json.dumps({'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),'loadavg': metric1.read()[:14]})
log.write(f'\n{out}')
log.close()
