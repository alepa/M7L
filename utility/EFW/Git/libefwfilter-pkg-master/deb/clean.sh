#!/bin/bash

version=`cat version`

rm -fr libefwfilter-$version
rm -fr libefwfilter_*
rm -fr libefwfilter-dev_*
rm -f debfiles/compat
rm -f debfiles/patches/*
