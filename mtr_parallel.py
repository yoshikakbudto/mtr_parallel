#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run mtr vs given targets in parallel

Use local config to configure targets and its running environment

WARN: Developed for centos 6.x and python 2.6.

"""

from contextlib import contextmanager
import datetime
import subprocess
import sys
import time

test_ip = "109.226.101.150"
pause_secs = 300


@contextmanager
def stdout_to_file( file ):
    sys.stdout = open( file, 'a')
    try:
        yield None
    finally:
        sys.stdout = sys.__stdout__


def mtr( cmd="mtr --report --report-wide -c 20", test_ip="127.0.0.1"  ):
    """mtr given target"""
    logfile = test_ip + "_" + datetime.datetime.utcnow().strftime("%Y-%m-%d") + ".log"

    print("running mtr vs %s. Log goes to %s" % ( cmd, logfile) )
    while True:
            mtr_proc = subprocess.Popen( cmd + " " + test_ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            mtr_stdout, mtr_stderr = mtr_proc.communicate()

            with stdout_to_file( logfile ):
                    print datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S %Z(UTC)")
                    print mtr_stdout

            time.sleep( pause_secs )

# 109.226.101.150 //
if __name__ == '__main__':
    print 'Ctrl-C to stop'
    mtr(test_ip='109.226.101.150')
