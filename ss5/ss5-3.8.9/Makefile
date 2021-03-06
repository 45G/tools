SUBDIRS=src modules

dst_dir   = ${prefix}
OS        = Linux
lib_path_base   = /usr/lib
conf_path_base  = /etc/opt
bin_path_base   = /usr/sbin
doc_path_base   = /usr/share/doc
man_path_base   = /usr/share/man
log_path_base   = /var/log/ss5
trc_path_base   = /var/log/ss5

CC = gcc

CFLAGS=-g -O2 -DLINUX -D_FILE_OFFSET_BITS=64 -I .  

LIBS = -lpthread 

all: common modules src

.PHONY : common
common ::
	@( cd common; $(MAKE) all )

.PHONY : modules
modules ::
	@( cd modules; $(MAKE) all )

.PHONY : src
src ::
	@( cd src; $(MAKE) all )

.PHONY : install
install:
	@( if [ ! -d $(dst_dir)$(log_path_base) ]; then mkdir -p $(dst_dir)$(log_path_base); fi )
	@( if [ ! -d $(dst_dir)$(trc_path_base) ]; then mkdir -p $(dst_dir)$(trc_path_base); fi )

	@( if [ ! -d $(dst_dir)$(bin_path_base) ]; then mkdir -p $(dst_dir)$(bin_path_base); fi )
	@( cp src/ss5 $(dst_dir)$(bin_path_base)/ )
	@( cp src/ss5srv $(dst_dir)$(bin_path_base)/ )

	@( if [ ! -d $(dst_dir)$(lib_path_base)/ss5 ]; then mkdir -p $(dst_dir)$(lib_path_base)/ss5; fi )
	@( find modules -name *.so -exec cp {} $(dst_dir)$(lib_path_base)/ss5/ \; )
	@( cp modules/mod_statistics/statmgr.cgi $(dst_dir)$(lib_path_base)/ss5/ )
	@( cp modules/mod_balance/balamgr.cgi $(dst_dir)$(lib_path_base)/ss5/ )
	@( cp modules/mod_statistics/SS5Logo.jpg $(dst_dir)$(lib_path_base)/ss5/ )
	@( cp modules/mod_balance/SS5Logo.jpg $(dst_dir)$(lib_path_base)/ss5/ )

	@( if [ $(OS) = "Linux" ]; then \
	if [ ! -d $(dst_dir)/etc/rc.d/init.d ]; then mkdir -p $(dst_dir)/etc/rc.d/init.d; fi ; \
        fi )
	@( if [ $(OS) = "Linux" ]; then \
	if [ ! -f $(dst_dir)/etc/rc.d/init.d/ss5 ]; then cp conf/ss5.init $(dst_dir)/etc/rc.d/init.d/ss5; \
	else cp conf/ss5.init $(dst_dir)/etc/rc.d/init.d/ss5.rpmnew ; fi ; \
        fi )
	@( if [ $(OS) = "Linux" ]; then \
	if [ ! -d $(dst_dir)/etc/sysconfig ]; then mkdir -p $(dst_dir)/etc/sysconfig; fi ; \
        fi )
	@( if [ $(OS) = "Linux" ]; then \
	if [ ! -f $(dst_dir)/etc/sysconfig/ss5 ]; then cp conf/ss5.sysconfig $(dst_dir)/etc/sysconfig/ss5; \
	else cp conf/ss5.sysconfig $(dst_dir)/etc/sysconfig/ss5.rpmnew ; fi ; \
        fi )
	@( if [ $(OS) = "SunOS" ]; then \
	if [ ! -d $(dst_dir)/etc/init.d ]; then mkdir -p $(dst_dir)/etc/init.d; fi ; \
        fi )
	@( if [ $(OS) = "SunOS" ]; then \
	if [ ! -f $(dst_dir)/etc/init.d/ss5 ]; then cp conf/ss5.init $(dst_dir)/etc/init.d/ss5; \
	else cp conf/ss5.init $(dst_dir)/etc/init.d/ss5.rpmnew ; fi ; \
        fi )
	@( if [ $(OS) = "FreeBSD" ]; then \
        if [ ! -f /usr/local/etc/rc.d/ss5 ]; then cp conf/ss5.init /usr/local/etc/rc.d/ss5; \
        else cp conf/ss5.init /usr/local/etc/rc.d/ss5.rpmnew ; fi ; \
        fi )

	@( if [ ! -d $(dst_dir)$(doc_path_base)/ss5 ]; then mkdir -p $(dst_dir)$(doc_path_base)/ss5; fi )
	@( cp License $(dst_dir)$(doc_path_base)/ss5 )
	@( cp -r doc/ldap/* $(dst_dir)$(doc_path_base)/ss5 )
	@( cp -r doc/pam/* $(dst_dir)$(doc_path_base)/ss5 )
	@( cp modules/mod_statistics/README.statmgr $(dst_dir)$(doc_path_base)/ss5 )
	@( cp modules/mod_balance/README.balamgr $(dst_dir)$(doc_path_base)/ss5 )

	@( if [ ! -d $(dst_dir)$(man_path_base)/man1 ]; then mkdir -p $(dst_dir)$(man_path_base)/man1; fi )
	@( cp man/$(OS)/ss5.1* $(dst_dir)$(man_path_base)/man1 )
	@( cp man/$(OS)/ss5srv.1* $(dst_dir)$(man_path_base)/man1 )
	@( if [ ! -d $(dst_dir)$(man_path_base)/man5 ]; then mkdir -p $(dst_dir)$(man_path_base)/man5; fi )
	@( cp man/$(OS)/ss5.passwd.5* $(dst_dir)$(man_path_base)/man5 )
	@( cp man/$(OS)/ss5.ha.5* $(dst_dir)$(man_path_base)/man5 )
	@( cp man/$(OS)/ss5.pam.5* $(dst_dir)$(man_path_base)/man5 )
	@( cp man/$(OS)/ss5.conf.5* $(dst_dir)$(man_path_base)/man5 )
	@( cp man/$(OS)/ss5_gss.5* $(dst_dir)$(man_path_base)/man5 )
	@( cp man/$(OS)/ss5_supa.5* $(dst_dir)$(man_path_base)/man5 )

	@( if [ ! -d $(dst_dir)$(conf_path_base) ]; then mkdir -p $(dst_dir)$(conf_path_base); fi )
	@( if [ ! -d $(dst_dir)$(conf_path_base)/ss5 ]; then mkdir -p $(dst_dir)$(conf_path_base)/ss5; fi )
	@( if [ ! -f $(dst_dir)$(conf_path_base)/ss5/ss5.conf ]; then cp conf/ss5.conf $(dst_dir)$(conf_path_base)/ss5; \
	else cp conf/ss5.conf $(dst_dir)$(conf_path_base)/ss5/ss5.conf.rpmnew ; fi )
	@( if [ ! -f $(dst_dir)$(conf_path_base)/ss5/ss5.ha ]; then cp conf/ss5.ha $(dst_dir)$(conf_path_base)/ss5; \
	else cp conf/ss5.ha $(dst_dir)$(conf_path_base)/ss5/ss5.ha.rpmnew ; fi )
	@( if [ ! -f $(dst_dir)$(conf_path_base)/ss5/ss5.passwd ]; then cp conf/ss5.passwd $(dst_dir)$(conf_path_base)/ss5; \
	else cp conf/ss5.passwd $(dst_dir)$(conf_path_base)/ss5/ss5.passwd.rpmnew ; fi )

	@( if [ $(OS) = "Linux" ] || [ $(OS) = "FreeBSD" ]; then \
        if [ ! -d $(dst_dir)/etc/pam.d ]; then mkdir -p $(dst_dir)/etc/pam.d; fi ; \
        fi )
	@( if [ $(OS) = "Linux" ] || [ $(OS) = "FreeBSD" ]; then \
	if [ ! -f $(dst_dir)/etc/pam.d/ss5 ]; then cp doc/pam/examples/ss5.pam $(dst_dir)/etc/pam.d/ss5; \
	else cp doc/pam/examples/ss5.pam $(dst_dir)/etc/pam.d/ss5.rpmnew ; fi ; \
        fi )

	@( if [ ! -d $(dst_dir)/var/run/ss5 ]; then mkdir -p $(dst_dir)/var/run/ss5; fi )


.PHONY : uninstall
uninstall:
	@( if [ -f $(dst_dir)$(bin_path_base)/ss5 ]; then rm -f $(dst_dir)$(bin_path_base)/ss5; fi )
	@( if [ -f $(dst_dir)$(bin_path_base)/ss5srv ]; then rm -f $(dst_dir)$(bin_path_base)/ss5srv; fi )

	@( if [ -d $(dst_dir)$(log_path_base) ]; then rm -rf $(dst_dir)$(log_path_base); fi )
	@( if [ -d $(dst_dir)$(trc_path_base) ]; then rm -rf $(dst_dir)$(trc_path_base); fi )

	@( if [ -d $(dst_dir)$(lib_path_base)/ss5 ]; then rm -rf $(dst_dir)$(lib_path_base)/ss5; fi )
	@( if [ -d $(dst_dir)$(doc_path_base)/ss5 ]; then rm -rf $(dst_dir)$(doc_path_base)/ss5; fi )

	@( if [ -f $(dst_dir)$(man_path_base)/man1/ss5.1 ]; then rm -f $(dst_dir)$(man_path_base)/man1/ss5.1; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man1/ss5srv.1 ]; then rm -f $(dst_dir)$(man_path_base)/man1/ss5srv.1; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.passwd.5 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.passwd.5; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.ha.5 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.ha.5; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.conf.5 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.conf.5; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.pam.5 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.pam.5; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5_gss.5 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5_gss.5; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5_supa.5 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5_supa.5; fi )

	@( if [ -f $(dst_dir)$(man_path_base)/man1/ss5.1.gz ]; then rm -f $(dst_dir)$(man_path_base)/man1/ss5.1.gz; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man1/ss5srv.1.gz ]; then rm -f $(dst_dir)$(man_path_base)/man1/ss5srv.1.gz; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.passwd.5.gz ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.passwd.5.gz; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.ha.5.gz ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.ha.5.gz; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.conf.5.gz ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.conf.5.gz; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.pam.5.gz ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.pam.5.gz; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5_gss.5.gz ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5_gss.5.gz; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5_supa.5.gz ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5_supa.5.gz; fi )

	@( if [ -f $(dst_dir)$(man_path_base)/man1/ss5.1.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man1/ss5.1.bz2; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man1/ss5srv.1.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man1/ss5srv.1.bz2; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.passwd.5.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.passwd.5.bz2; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.ha.5.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.ha.5.bz2; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.conf.5.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.conf.5.bz2; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5.pam.5.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5.pam.5.bz2; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5_gss.5.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5_gss.5.bz2; fi )
	@( if [ -f $(dst_dir)$(man_path_base)/man5/ss5_supa.5.bz2 ]; then rm -f $(dst_dir)$(man_path_base)/man5/ss5_supa.5.bz2; fi )

	@( if [ -d $(dst_dir)$(conf_path_base)/ss5 ]; then rm -rf $(dst_dir)$(conf_path_base)/ss5; fi )

	@( if [ $(OS) = "Linux" ] || [ $(OS) = "FreeBSD" ]; then \
	if [ -f $(dst_dir)/etc/pam.d/ss5 ]; then rm -f $(dst_dir)/etc/pam.d/ss5; fi ; \
        fi )

	@( if [ $(OS) = "Linux" ] || [ $(OS) = "FreeBSD" ]; then \
	if [ -f $(dst_dir)$(boot_path_base)/ss5 ]; then rm -f $(dst_dir)$(boot_path_base)/ss5; fi; \
        fi )

	@( if [ $(OS) = "Linux" ]; then \
	if [ -f $(dst_dir)/etc/rc.d/init.d/ss5 ]; then rm -f $(dst_dir)/etc/rc.d/init.d/ss5; fi; \
        fi )
	@( if [ $(OS) = "SunOS" ]; then \
	if [ -f $(dst_dir)/etc/init.d/ss5 ]; then rm -f $(dst_dir)/etc/init.d/ss5; fi; \
        fi )
	@( if [ $(OS) = "FreeBSD" ]; then \
        if [ -f /usr/local/etc/rc.d/ss5 ]; then rm -f /usr/local/etc/rc.d/ss5; fi; \
        fi )

	@( if [ -d $(dst_dir)/var/run/ss5 ]; then rm -rf $(dst_dir)/var/run/ss5; fi )

clean:
	for d in $(SUBDIRS); do (cd $$d; $(MAKE) clean); done

distclean: clean
	for d in $(SUBDIRS); do (cd $$d; $(MAKE) distclean); done
	rm -rf autom4te.cache
	rm -f config.h
	rm -f config.log
	rm -f config.status
	rm -f Makefile


