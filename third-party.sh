#!/usr/bin/env bash

## libpng ##
wget "http://jaist.dl.sourceforge.net/project/libpng/libpng16/1.6.16/libpng-1.6.16.tar.gz" -O "./libpng.tar.gz"
tar xvf libpng.tar.gz
mv libpng-1.6.16 ./third-party/libpng
rm libpng.tar.gz

## libjpeg-turbo ##
wget "http://jaist.dl.sourceforge.net/project/libjpeg-turbo/1.4.0/libjpeg-turbo-1.4.0.tar.gz" -O "./libjpeg.tar.gz"
tar xvf libjpeg-turbo.tar.gz
mv libjpeg-turbo-1.4.0 ./third-party/libjpeg-turbo
rm libjpeg-turbo.tar.gz

## giflib ##
wget "http://cznic.dl.sourceforge.net/project/giflib/giflib-4.x/giflib-4.2.3.tar.gz" -O "./giflib.tar.gz"
tar xvf giflib.tar.gz
mv giflib-4.2.3 ./third-party/giflib
rm giflib.tar.gz