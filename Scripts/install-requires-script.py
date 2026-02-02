#!c:\users\khanh.desktop-aq0hcuh\source\repos\python-horse\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'install-requires==0.3.0','console_scripts','install-requires'
__requires__ = 'install-requires==0.3.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('install-requires==0.3.0', 'console_scripts', 'install-requires')()
    )
