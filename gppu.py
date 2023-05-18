import subprocess as sp
import time


#gpu_mem_cmd = r'(((Get-Counter "\GPU Process Memory(*)\Local Usage").CounterSamples | where CookedValue).CookedValue | measure -sum).sum'
gpu_usage_cmd = r'(((Get-Counter "\GPU Engine(*engtype_3D)\Utilization Percentage").CounterSamples | where CookedValue).CookedValue | measure -sum).sum'

def run_command(command):
    val = sp.run(['powershell', '-Command', command], capture_output=True).stdout.decode("ascii")
    return float(val.strip().replace(',', '.'))

while True:

    sp.run('cls', shell=True)

    print()
    print(" GPU Info ".center(80, '='))
    #print(f"GPU Memory Usage: {round(run_command(gpu_mem_cmd)/1e6, 1):<6} MB")
    print(f"GPU Load :        {round(run_command(gpu_usage_cmd), 2):<6} %")

    time.sleep(0.5) 
