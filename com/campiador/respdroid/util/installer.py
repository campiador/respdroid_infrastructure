import pip
from subprocess import call

#need to install simplejson


# No longer need this dependency
def check_mysql_installed():
    try:
        import MySQLdb
    except ImportError, e:
        print("MySQLdb is not installed. Install it using: pip uninstall MySQL-python \
                brew install mysql \
                pip install MySQL-python")


def install(package):
    pip.main(['install', package])