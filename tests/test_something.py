# coding: utf8
#
# static - test_something
# 
# Author: ilcwd 
# Create: 15/5/11
#


import base


def test_version():
    versionInfo = base.rpc('/static/version', {})
    assert isinstance(versionInfo, dict), versionInfo
    assert 'version' in versionInfo, versionInfo


def main():
    test_version()


if __name__ == '__main__':
    main()