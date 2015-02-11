# Copyright 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This is a copy of ../third-party/libjpeg-turbo/libjpeg-turbo.gyp , modified
# such that all source paths point into that directory.
# See http://code.google.com/p/skia/issues/detail?id=543 ('wrap libjpeg-turbo.gyp
# from Chrome's libjpeg-turbo port, rather than making our own copy') for a better
# long-term solution.

{
  'variables': {
    'use_system_libjpeg-turbo%': 0,
    'skia_warnings_as_errors': 0,
  },
  'conditions': [
    ['skia_os == "android"', {
      'targets': [
        {
          'target_name': 'libjpeg-turbo',
          'type': 'none',
          'dependencies': [
            'android_deps.gyp:jpeg',
          ],
          'export_dependent_settings': [
            'android_deps.gyp:jpeg',
          ],
        },
      ],
    }, { # skia_os != android
      'conditions': [
          ['use_system_libjpeg-turbo==0', {
          'targets': [
            {
              'target_name': 'libjpeg-turbo',
              'type': 'static_library',
              'sources': [
                # we currently build skia's version of libjpeg-turbo-turbo without
                # SIMD optimizations for simplicity
                    "../third-party/libjpeg-turbo/bmp.c",
                    "../third-party/libjpeg-turbo/cdjpeg.c",
                    "../third-party/libjpeg-turbo/cjpeg.c",
                    "../third-party/libjpeg-turbo/djpeg.c",
                    "../third-party/libjpeg-turbo/example.c",
                    "../third-party/libjpeg-turbo/jaricom.c",
                    "../third-party/libjpeg-turbo/jcapimin.c",
                    "../third-party/libjpeg-turbo/jcapistd.c",
                    "../third-party/libjpeg-turbo/jcarith.c",
                    "../third-party/libjpeg-turbo/jccoefct.c",
                    "../third-party/libjpeg-turbo/jccolext.c",
                    "../third-party/libjpeg-turbo/jccolor.c",
                    "../third-party/libjpeg-turbo/jcdctmgr.c",
                    "../third-party/libjpeg-turbo/jchuff.c",
                    "../third-party/libjpeg-turbo/jcinit.c",
                    "../third-party/libjpeg-turbo/jcmainct.c",
                    "../third-party/libjpeg-turbo/jcmarker.c",
                    "../third-party/libjpeg-turbo/jcmaster.c",
                    "../third-party/libjpeg-turbo/jcomapi.c",
                    "../third-party/libjpeg-turbo/jcparam.c",
                    "../third-party/libjpeg-turbo/jcphuff.c",
                    "../third-party/libjpeg-turbo/jcprepct.c",
                    "../third-party/libjpeg-turbo/jcsample.c",
                    "../third-party/libjpeg-turbo/jcstest.c",
                    "../third-party/libjpeg-turbo/jctrans.c",
                    "../third-party/libjpeg-turbo/jdapimin.c",
                    "../third-party/libjpeg-turbo/jdapistd.c",
                    "../third-party/libjpeg-turbo/jdarith.c",
                    "../third-party/libjpeg-turbo/jdatadst-tj.c",
                    "../third-party/libjpeg-turbo/jdatadst.c",
                    "../third-party/libjpeg-turbo/jdatasrc-tj.c",
                    "../third-party/libjpeg-turbo/jdatasrc.c",
                    "../third-party/libjpeg-turbo/jdcoefct.c",
                    "../third-party/libjpeg-turbo/jdcol565.c",
                    "../third-party/libjpeg-turbo/jdcolext.c",
                    "../third-party/libjpeg-turbo/jdcolor.c",
                    "../third-party/libjpeg-turbo/jddctmgr.c",
                    "../third-party/libjpeg-turbo/jdhuff.c",
                    "../third-party/libjpeg-turbo/jdinput.c",
                    "../third-party/libjpeg-turbo/jdmainct.c",
                    "../third-party/libjpeg-turbo/jdmarker.c",
                    "../third-party/libjpeg-turbo/jdmaster.c",
                    "../third-party/libjpeg-turbo/jdmerge.c",
                    "../third-party/libjpeg-turbo/jdmrg565.c",
                    "../third-party/libjpeg-turbo/jdmrgext.c",
                    "../third-party/libjpeg-turbo/jdphuff.c",
                    "../third-party/libjpeg-turbo/jdpostct.c",
                    "../third-party/libjpeg-turbo/jdsample.c",
                    "../third-party/libjpeg-turbo/jdtrans.c",
                    "../third-party/libjpeg-turbo/jerror.c",
                    "../third-party/libjpeg-turbo/jfdctflt.c",
                    "../third-party/libjpeg-turbo/jfdctfst.c",
                    "../third-party/libjpeg-turbo/jfdctint.c",
                    "../third-party/libjpeg-turbo/jidctflt.c",
                    "../third-party/libjpeg-turbo/jidctfst.c",
                    "../third-party/libjpeg-turbo/jidctint.c",
                    "../third-party/libjpeg-turbo/jidctred.c",
                    "../third-party/libjpeg-turbo/jmemmgr.c",
                    "../third-party/libjpeg-turbo/jmemnobs.c",
                    "../third-party/libjpeg-turbo/jpegtran.c",
                    "../third-party/libjpeg-turbo/jquant1.c",
                    "../third-party/libjpeg-turbo/jquant2.c",
                    "../third-party/libjpeg-turbo/jsimd_none.c",
                    "../third-party/libjpeg-turbo/jstdhuff.c",
                    "../third-party/libjpeg-turbo/jutils.c",
                    "../third-party/libjpeg-turbo/rdbmp.c",
                    "../third-party/libjpeg-turbo/rdcolmap.c",
                    "../third-party/libjpeg-turbo/rdgif.c",
                    "../third-party/libjpeg-turbo/rdjpgcom.c",
                    "../third-party/libjpeg-turbo/rdppm.c",
                    "../third-party/libjpeg-turbo/rdrle.c",
                    "../third-party/libjpeg-turbo/rdswitch.c",
                    "../third-party/libjpeg-turbo/rdtarga.c",
                    "../third-party/libjpeg-turbo/tjbench.c",
                    "../third-party/libjpeg-turbo/tjunittest.c",
                    "../third-party/libjpeg-turbo/tjutil.c",
                    "../third-party/libjpeg-turbo/transupp.c",
                    "../third-party/libjpeg-turbo/turbojpeg-jni.c",
                    "../third-party/libjpeg-turbo/turbojpeg.c",
                    "../third-party/libjpeg-turbo/wrbmp.c",
                    "../third-party/libjpeg-turbo/wrgif.c",
                    "../third-party/libjpeg-turbo/wrjpgcom.c",
                    "../third-party/libjpeg-turbo/wrppm.c",
                    "../third-party/libjpeg-turbo/wrrle.c",
                    "../third-party/libjpeg-turbo/wrtarga.c",
              ],
              'direct_dependent_settings': {
                'include_dirs': [
                  '../third-party/libjpeg-turbo',
                ],
              },
              'cflags': [
                '-w', # supresses warnings
              ],
            },
          ],
        }, {  ## use_system_libjpeg-turbo != 0
          'targets': [
            {
              'target_name': 'libjpeg-turbo',
              'type': 'none',
              'direct_dependent_settings': {
                'defines': [
                  'USE_SYSTEM_LIBJPEG',
                ],
              },
              'link_settings': {
                'libraries': [
                  '-ljpeg',
                ],
              },
            }
          ],
        }],
      ],
    }],
  ],
}
