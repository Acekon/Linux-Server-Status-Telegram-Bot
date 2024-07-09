import os


def get_disk_space():
    return os.system('df -h')


def get_ram_usage():
    return os.system('free -mh')


def get_cpu_usage():
    return os.system('mpstat')


if __name__ == '__main__':
    get_cpu_usage()