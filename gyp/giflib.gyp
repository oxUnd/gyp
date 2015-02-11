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
      'target_name': 'giflib',
      'conditions': [
        [ 'skia_giflib_static',
          {
            'type': 'static_library',
            'defines': [
              'HAVE_CONFIG_H',
            ],
            'include_dirs': [
              '../third-party/giflib',
            ],
            'dependencies': [
            ],
            'direct_dependent_settings': {
              'include_dirs': [
                '../third-party/giflib',
              ],
            },
            'cflags': [
              '-w',
            ],
            'sources': [
              '../third-party/giflib/lib/dgif_lib.c',
              '../third-party/giflib/lib/gifalloc.c',
              '../third-party/giflib/lib/gif_err.c',
            ],
          }, {  # not skia_giflib_static
            'type': 'none',
            'direct_dependent_settings': {
              'link_settings': {
                'libraries': [
                  '-lgif',
                ],
              },
            },
          }
        ],
      ]
    }
  ]
}