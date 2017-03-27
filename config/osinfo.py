import  psutil, datetime

class OS:
    mem = psutil.virtual_memory()
    total_mem,free_mem,per_mem = mem.total,mem.free,mem.percent
    swap = psutil.swap_memory()
    swap_total,swap_per = swap.total,swap.percent
    io = psutil.disk_io_counters()
    read_io,write_io = io.read_count,io.write_count
    net = psutil.net_io_counters()
    net_sent,net_recv = net.bytes_sent,net.bytes_recv
    num = 1024*1024*1024
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    total_mem = format(total_mem/num,'.2f')
    free_mem = format(free_mem/1024/1024,'1.2f')