# Copyright 2014 Google Inc.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'skia_warnings_as_errors': 0,
  },
  'targets': [
    {
      'target_name': 'libpng',
      'conditions': [
        [ 'skia_libpng_static',
          {
            'type': 'static_library',
            'include_dirs': [
              '../third-party/libpng',
            ],
            'dependencies': [
              'zlib.gyp:zlib',
            ],
            'export_dependent_settings': [
              'zlib.gyp:zlib',
            ],
            'direct_dependent_settings': {
              'include_dirs': [
                '../third-party/libpng',
              ],
            },
            'cflags': [
              '-w',
              '-fvisibility=hidden',
            ],
            'sources': [
              '../third-party/libpng/png.c',
              '../third-party/libpng/pngerror.c',
              '../third-party/libpng/pnggccrd.c',
              '../third-party/libpng/pngget.c',
              '../third-party/libpng/pngmem.c',
              '../third-party/libpng/pngpread.c',
              '../third-party/libpng/pngread.c',
              '../third-party/libpng/pngrio.c',
              '../third-party/libpng/pngrtran.c',
              '../third-party/libpng/pngrutil.c',
              '../third-party/libpng/pngset.c',
              '../third-party/libpng/pngtrans.c',
              '../third-party/libpng/pngvcrd.c',
              '../third-party/libpng/pngwio.c',
              '../third-party/libpng/pngwrite.c',
              '../third-party/libpng/pngwtran.c',
              '../third-party/libpng/pngwutil.c',
            ],
          }, {  # not skia_libpng_static
            'type': 'none',
            'conditions': [
              [ 'skia_os == "android"',
                {
                  # TODO(halcanary): merge all png targets into this file.
                  'dependencies': [
                    'android_deps.gyp:png',
                  ],
                  'export_dependent_settings': [
                    'android_deps.gyp:png',
                  ],
                }, {  # skia_os != "android"
                  'dependencies': [
                    'zlib.gyp:zlib',
                    ],
                  'export_dependent_settings': [
                    'zlib.gyp:zlib',
                    ],
                  'direct_dependent_settings': {
                    'link_settings': {
                      'libraries': [
                        '-lpng',
                      ],
                    },
                  },
                }
              ]
            ]
          }
        ]
      ],
    },
  ]
}