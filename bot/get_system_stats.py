
import psutil
import speedtest
from requests import get

st = speedtest.Speedtest()

def get_system_stats():
    ipv4_addr = get('https://api.ipify.org').content.decode('utf8')
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_temperature = psutil.sensors_temperatures()['cpu_thermal'][0].current
    speed_download = st.download()/10e6
    return ipv4_addr, cpu_usage, memory_usage, cpu_temperature, speed_download

