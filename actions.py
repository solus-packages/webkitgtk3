#!/usr/bin/python


from pisi.actionsapi import shelltools, get, autotools, pisitools

shelltools.export("HOME", get.workDIR())

def build_config():
    cflags = get.CFLAGS().replace("-ggdb3","")
    cxxflags = get.CXXFLAGS().replace("-gddb3", "")
    shelltools.export("CFLAGS", cflags)
    shelltools.export("CXXFLAGS", cxxflags)


def setup():
    shelltools.system("sed -i '/gtkdoc --rebase/s:^:# :' GNUmakefile.*")
    if not get.canClang(): build_config()
    autotools.configure("--disable-static \
                         --libexecdir=/usr/lib/WebKitGTK \
                         --with-gstreamer=1.0 \
                         --with-gnu-ld \
                         --enable-introspection \
                         --disable-geolocation \
                         --disable-webkit2 \
                         --disable-gtk-doc-html")
    shelltools.system("sed -i '/gtkdoc --rebase/s:^:# :' GNUmakefile.*")

def build():
    if not get.canClang(): build_config()
    autotools.make()

def install():
    if not get.canClang(): build_config()
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
