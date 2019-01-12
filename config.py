# Surveillance Project
# File: config.py
# Author: Ryan Anstotz
# Description:
#  Configuration function
#
# =================================================================================

# import necessary packages
import os
import sys
import json

# function to parse configuration json
def parse_config(config_file, script_type):
    client = "client"
    server = "server"
    with open(config_file, 'r') as fp:
        data = json.load(fp)
    if script_type == client:
        return str(data["client_ip"]), int(data["client_port"])
    if script_type == server:
        return str(data["server_ip"]), int(data["server_port"])
