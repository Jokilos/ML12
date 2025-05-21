# KDIR ?= /lib/modules/`uname -r`/build
KDIR ?= /lib/modules/6.12.6/build

default:
	$(MAKE) -C $(KDIR) M=$$PWD

install:
	$(MAKE) -C $(KDIR) M=$$PWD modules_install

clean:
	$(MAKE) -C $(KDIR) M=$$PWD clean
