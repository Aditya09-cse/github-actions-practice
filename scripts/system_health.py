import psutil

def check_system_health() :
    # to compare current cpu and cpu threshold
    cpu_threshold = int(input("Enter the cpu threshold valure :" ))
    current_cpu = psutil.cpu_percent(interval=1)
    print(current_cpu)
    if current_cpu > cpu_threshold :
        print("Alert sms sent")
    else :
        print("cpu in safe mode")

    # for comapre disk threshold and disk metrices
    disk_threshold = int(input("Enter the disk threshold valure :" ))
    disk_usage =  psutil.disk_usage('/')
    print(disk_usage)
    if disk_usage.percent > disk_threshold :
        print("Alert sms sent")
    else :
        print("Sufficient disk for future ")

    # to comapre memory threshold and memory usage 
    memory_threshold = int(input("Enter the memory threshold valure :" ))
    memory_usage = psutil.virtual_memory()
    print(memory_usage)
    if memory_usage.percent > memory_threshold :
        print("memory almost going to full ")
    else :
        print("Sufficient memory for future ")
check_system_health()
