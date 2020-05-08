import os
import platform
import subprocess


name_of_platform = platform.system()
"""
    This returns the name of your System Operating System
    This is stored in "name_of_platform"
"""

def ping_return_code(name_of_host):
    """
        name_of_host -> parameter for hosted websites to be tested
                        for netwoork connectivity
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
            status_code = subprocess.call(['ping', '-n', '5', '-W', '3', name_of_host],
                                        stdout=open(os.devnull, 'w'),
                                        stderr=open(os.devnull, 'w'))

            
        


