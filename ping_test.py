import os
import platform
import subprocess


def ping_host(name_of_host):
    """
        name_of_host -> parameter for hosted websites to be tested
                        for netwoork connectivity
    """

    name_of_platform = platform.system()
    """
        This returns the name of your System Operating System
        This is stored in "name_of_platform"
    """
    

    try:
        """
            Check for your current system OS

            ping: send an echo request
            -n: number of request (5)
            -W: time delay (3) in milliseconds
            name_of_host: hosted website to be tested for connectivty

            Direct other commands streams such as
            stdout and stdin to /dev/null (bin)

            Returns only status code for each executed process
            0: Success
            1 and above: Error
        """

        if name_of_platform == "Windows":
            """
                For Windows OS
            """
            status_code = subprocess.call(['ping', '-n', '5', '-W', '3', name_of_host],
                                        stdout=open(os.devnull, 'w'),
                                        stderr=open(os.devnull, 'w'))
        elif name_of_platform == "Linux":
            """
                For Linux OS
            """
            status_code = subprocess.call(['ping', '-c', '5', '-W', '3', name_of_host],
                                        stdout=open(os.devnull, 'w'),
                                        stderr=open(os.devnull, 'w'))

        if status_code == 0:
            print('Name of host: ', name_of_host)
            print("Connection result: Sucessful")
            print('Host is up and running\n\n')
        elif status_code == 1 or 2 or 256 or 512:
            print('Name of host: ', name_of_host)
            print("Connection result: Unsucessful")
            print('Host is down\n\n')

    except Exception:
        """
            Other values or unknown errors are captured here and 
            acted on with the code below
        """
        print('Name of host: ', name_of_host)
        print("Connection result: Unsucessful")
        print('Host is Unreachable\n\n')

    return status_code


def verify_hosts(list_of_hosts):
    host_status_code = dict()

    print("Networking Results\n\n")
    for name_of_host in list_of_hosts:
        host_status_code[name_of_host] = ping_host(name_of_host)
    return host_status_code


if __name__ == '__main__':
    
    hosts_list = [
        'google.com',
        'twitter.com',
        'linkedin.com',
        'instagram.com',
        'medium.com'
    ]

    status_code_results = verify_hosts(hosts_list)
    print(status_code_results)

            
        


