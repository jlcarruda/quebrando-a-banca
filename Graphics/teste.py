import os
import errno
directory = 'box_chart'
try:
    os.makedirs(directory+'/test')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
