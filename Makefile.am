EXTRA_DIST =
CLEANFILES =
ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}
AM_MAKEFLAGS = --no-print-directory

AM_CPPFLAGS = \
	-include $(top_builddir)/config.h \
	-DSYSCONFDIR=\""$(sysconfdir)"\" \
	-DLIBEXECDIR=\""$(libexecdir)"\" \
	-I${top_srcdir}/src/tgl \
	-I${top_srcdir}/src

AM_CFLAGS = ${my_CFLAGS} \
	-fvisibility=hidden \
	-ffunction-sections \
	-fdata-sections

AM_LDFLAGS = \
	-Wl,--gc-sections \
	-Wl,--as-needed

LIBTGL_CURRENT=1
LIBTGL_REVISION=0
LIBTGL_AGE=1

pkginclude_HEADERS = tgl.h tgl-layout.h
lib_LTLIBRARIES = libtgl.la

src_libtgl_la_SOURCES =\
	tgl.c
	mtproto-common.c
	mtproto-client.c
	queries.c
	structures.c
	binlog.c
	auto/auto.c
	updates.c
	tg-mime-types.c

##EXTRA_DIST += src/libtgl.sym

src_libtgl_la_LDFLAGS = $(AM_LDFLAGS) \
	-version-info $(LIBtgl_CURRENT):$(LIBtgl_REVISION):$(LIBtgl_AGE)
##	-Wl,--version-script=$(top_srcdir)/src/libtgl.sym
##src_libtgl_la_DEPENDENCIES = ${top_srcdir}/src/libtgl.sym

##pkgconfigdir = $(libdir)/pkgconfig
##pkgconfig_DATA = src/libtgl.pc
##EXTRA_DIST += src/libtgl.pc.in
##CLEANFILES += src/libtgl.pc

##TESTS = src/test-libtgl

##check_PROGRAMS = src/test-libtgl
##src_test_libtgl_SOURCES = src/test-libtgl.c
##src_test_libtgl_LDADD = src/libtgl.la
