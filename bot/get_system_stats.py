import psutil

# Get the current CPU usage
cpu_usage = psutil.cpu_percent()

# Get the current memory usage
memory_usage = psutil.virtual_memory().used

def get_system_stats():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    cpu_temperature = psutil.sensors_temperatures()['cpu_thermal'][0].current
    return cpu_usage, memory_usage, cpu_temperature

