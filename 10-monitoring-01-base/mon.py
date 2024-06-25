import time
import json
filename = time.strftime("%Y-%m-%d")+"-awesome-monitoring.log"
log = open("/var/log/"+filename,"a")
metric1 = (open('/proc/loadavg')).read()[:14]
metric2 = ((open('/proc/meminfo')).read()).split()[1]
metric3 = ((open('/proc/meminfo')).read()).split()[4]
metric4 = ((open('/proc/uptime')).read()).split()[0]
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
out = json.dumps({'timestamp': timestamp,'loadavg,5 10 15': metric1,'MemTotal,Gb': int(metric2)/1024,'MemFree,Gb': int(metric3)/1024,'Uptime,H': float(metric4)/60/60})
log.write(f'\n{out}')
log.close()