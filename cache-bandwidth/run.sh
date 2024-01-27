#! /bin/bash

export LD_LIBRARY_PATH=${PWD}/../roi/papi/install/lib:$LD_LIBRARY_PATH
export PAPI_EVENTS="PAPI_L1_DCM,PAPI_L1_DCA,PAPI_L2_LDM,PAPI_L2_DCA,PAPI_L2_TCA,PAPI_L3_LDM,PAPI_L3_STM"

export PAPI_OUTPUT_DIRECTORY=${PWD}/../data/azacca/cache_bandwidth/l1
./cache_bandwidth.papi l1
export PAPI_OUTPUT_DIRECTORY=${PWD}/../data/azacca/cache_bandwidth/l2
./cache_bandwidth.papi l2
export PAPI_OUTPUT_DIRECTORY=${PWD}/../data/azacca/cache_bandwidth/l3
./cache_bandwidth.papi l3
