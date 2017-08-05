import subprocess


def handle(event, context):
    p = subprocess.Popen('./hello', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data, stderr_data = p.communicate()
    return stdout_data.decode('utf-8')
