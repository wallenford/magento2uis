# -*- coding: utf-8 -*-

import sys
import os

from cx_Freeze import setup, Executable

includefiles = ['uis.conf',
                'D:\\WinPython-64bit-3.6.2.0Qt5\\python-3.6.2.amd64\\DLLs\\tcl86t.dll',
                'D:\\WinPython-64bit-3.6.2.0Qt5\\python-3.6.2.amd64\\DLLs\\tk86t.dll']
includes = [ 'xlwt','pandas','numpy','os','sys','encodings.utf_8']
excludes = ["PyQt4.QtSql", "sqlite3","PyQt4.QtNetwork","PyQt4.QtScript","PyQt5","alabaster","babel","boto3","botocore",
            "bottleneck","certifi","cffi","cloudpickle","dask","distributed","docrepr","docutils","fastparquet","feather",
            "h5py","html5lib","idna","ipykernel","ipyparallel","IPython","jedi","jinja2","jmespath","joblib","jupyter_client",
            "jupyter_client","jupyter_core","karas","llvmlite","matplotlib","nbcovert","nbformat","netCDF4","numba","pexpect",
            "ply","requests","requests_ftp","s3fs","s3transfer","scipy","seaborn","setuptools","simplejson",
            "sqlalchemy","tensflow","testpath","xml","xmlrpc","blosc","colorama","html","lxml","multiprocess","pyarrow","tables",
            "thriftpy","tornado","wcwidth", "werkzeug","xml","xmlrpc"]

#excludes = []
#packages = ['os','pan   das','numpy']

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

os.environ['TCL_LIBRARY'] = "D:\\WinPython-64bit-3.6.2.0Qt5\\python-3.6.2.amd64\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "D:\\WinPython-64bit-3.6.2.0Qt5\\python-3.6.2.amd64\\tcl\\tk8.6"


executables = [
    Executable('D:\\PycharmProjects\\magento2uis\\mainapp.py', base=base)
]

exe = Executable(
      script="mainapp.py",
      base="Win32GUI",
      targetName="magento2uis.exe"
     )
setup(name='magento2uis',
      version='0.1',
      description='Magento2Uis script',
      options={"build_exe": {"includes": includes, "include_files": includefiles, "excludes":excludes}},
      executables=executables
      )