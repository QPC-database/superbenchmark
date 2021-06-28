# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""Network Utility."""

import socket
import subprocess
from contextlib import closing


def get_free_port():
    """Get a free port in current system.

    Return:
        port (int): a free port in current system.
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def get_ib_devices():
    """Get available ordered IB devices in the system and filter ethernet devices."""
    # command = 'ls -l /sys/class/infiniband/* | awk \'{print $9}\' | sort | awk -F\'/\' \'{print $5}\''
    command = "ibv_devinfo | awk '$1 ~ /hca_id/||/link_layer:/ {print $1,$2}' |  awk '{print $2}'"
    output = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, check=False, universal_newlines=True
    )
    lines = output.stdout.splitlines()
    ib_devices = []
    for i in range(len(lines) - 1):
        if 'InfiniBand' in lines[i + 1]:
            ib_devices.append(lines[i])
    return ib_devices
