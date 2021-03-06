{
  "targets": [
    {
      "target_name": "addon",
      "sources": [
        "ConfigLoader.cc",
        "GZNode.cc",
        "OgreMaterialParser.cc"
      ],
      'cflags_cc!': [ '-fno-rtti', '-fno-exceptions' ],
      'cflags!': [ '-fno-exceptions' ],
      "conditions": [
        ['OS=="linux"', {
          'cflags': [
            '<!@(pkg-config --cflags gazebo jansson protobuf)'
          ],
          'ldflags': [
            '<!@(pkg-config --libs-only-L --libs-only-other gazebo jansson protobuf)'
          ],
          'libraries': [
            '<!@(pkg-config --libs-only-l gazebo jansson protobuf)'
          ]
        }],
        ['OS=="mac"', {
          'libraries': [
            '<!@(pkg-config --libs-only-l gazebo jansson protobuf)'
          ],
          'xcode_settings' : {
            'GCC_ENABLE_CPP_RTTI': 'YES',
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'OTHER_CFLAGS': [
              '<!@(pkg-config --cflags gazebo jansson protobuf)'
            ],
            'OTHER_CPLUSPLUSFLAGS': [
              '<!@(pkg-config --cflags gazebo jansson protobuf)'
            ],
            'OTHER_LDFLAGS': [
              '<!@(pkg-config --libs-only-L --libs-only-other  gazebo jansson protobuf)'
            ]
          }
        }]
      ]   
    }
  ]
}