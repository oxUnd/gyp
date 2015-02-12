# gyp

## use

0. download third party, `sh third-party.sh`
0. config your `binding.gyp`

    if dependent on `zlib`, you can add the following code to `binding.gyp`

    ```
    {
        targets: [{
            "target_name": "addon",
            
            ...

            "dependencies": [
                "./gyp/zlib.gyp:zlib"
            ]

            ...
            
        }]
    }
    ```