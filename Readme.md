
## a Ubuntu distro running on a Raspberry Pi 2 needs a different version of the library in pip.
`sudo pip uninstall RPi.GPIO`
`sudo pip install mercurial`
`sudo pip install hg+http://hg.code.sf.net/p/raspberry-gpio-python/code#egg=RPi.GPIO`

