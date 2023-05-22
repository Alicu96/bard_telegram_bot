import psutil
import speedtest

st = speedtest.Speedtest()

def get_system_stats():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_temperature = psutil.sensors_temperatures()['cpu_thermal'][0].current
    speed_download = int(st.download()/10e6)
    return cpu_usage, memory_usage, cpu_temperature, speed_download

