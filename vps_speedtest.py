#!/usr/bin/python

# -*- coding: utf-8 -*-
# Copyright 2012-2016 Matt Martz
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import platform as pf
import urllib as ul
import re

def check_Network():
    return1=os.system('ping baidu.com -c 2')
    if return1:
        print 'ping fail'
        return False
    else:
        print 'ping OK'
        return True

def vps_speedtest():
    system_OS=pf.platform()
    re_match_systemOS=re.search(r'centos',system_OS,re.I)
    if re_match_systemOS.group()=='centos':
        OS="centos"
        os.system('curl -L ip.cn')
        ul.urlretrieve('https://raw.githubusercontent.com/zanshichun/centos_ss_install/master/speedtest.py',
                       "/opt/speedtest.py")
        os.system('python /opt/speedtest.py')
    else:
        print("This os is not CentOS")
        exit()
if os.getuid()!=0:
    print"This program must be run as root.Aborting."
    if check_Network()==True:
        if os.path.isfile('/opt/speedtest.py')==True:
            os.system('curl -L ip.cn')
            os.system('python /opt/speedtest.py')
        else:
            vps_speedtest()
    else:
        print'Plz check your Network!'
        exit()
else:
    print"plz use root  program!"
    if check_Network() == True:
        if os.path.isfile('/opt/speedtest.py') == True:
            os.system('curl -L ip.cn')
            os.system('python /opt/speedtest.py')
        else:
            vps_speedtest()
    else:
        print'Plz check your Network!'
        exit()