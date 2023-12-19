# Benchmarks

**NOTE**: All the instructions mentioned in this README have been tested on ARM-based
machines with Ubuntu 22.04.

**NOTE**: The gem5 libraries provided in this repository under `roi/gem5/lib` are built
for the ARM isa.

**NOTE**: This README is a complementary reading useful for building the workloads in
this repository's submodules.
This README does not cover the dependencies of each workload.
Please refer to their own instructions for a list of their dependencies.
Please make sure to follow their README/instructions for compilation if need be.

This repository includes benchmarks that are useful for characterizing and modeling
the performance of ARM HPC machines such as Neoverse N1.
The benchmarks have their regions of interest annotated to work with both gem5
and papi platforms.
All the workloads in this repository need the ROI binaries as a prerequisite.
Please refer to [this section](#building-the-roi-binaries) for instructions on creating the ROI binaries.

After building the ROI binaries, we can start compiling each workload.
Please refer to the following sections for instructions on how to compile each of the following benchmarks.

* [NASA Parallael Benchmarks](#building-npb)
* [Branson](#building-branson)
* [Simple Vectorizable Benchmarks](#building-simple-vectorizable-benchmarks)
* [Microbenchmarks]()

## Building the ROI binaries

By default the makefile located in `roi/Makefile` creates binaries for all annotating platforms.
There are three platforms to choose from: **native**, **papi**, and **gem5**.
For native the only the created binary will do is print statement at the beginning and the end of roi.
Therefore, it does not need any specific header or library for compilation.
Headers and binaries required for building the ROI binary for gem5 are given in `roi/gem5`.
However, to create the binaries for papi, first we need to build PAPI itself.
For instructions on how to build and install PAPI, please refer to [this section]()
**NOTE**: The targets in `roi/Makefile` assume that papi is installed in `roi/papi/install`.
If you decide to install papi somewhere else, please adapt `roi/Makefile`.

Now, to build the ROI binaries, run the following command in the base directory.

```shell
make
```

### Building PAPI

The source code for PAPI is located in `roi/papi`.
To build PAPI, run the following command in the base directory.

```shell
cd roi/papi/src
./configure --prefix=${PWD}/../install
make && make install
```

**NOTE**: The targets in `roi/Makefile` assume that papi is installed in `roi/papi/install`.
If you decide to install papi somewhere else, please adapt `roi/Makefile`.

## Building NPB

By default NPB workloads are created with the native roi binaries (just print statements).
Before building any workloads, please create a directory to store all the binaries.
Run the following command to create `bin` in `NPB3.4-OMP`.

```shell
mkdir bin
```

In order to build binaries for different annotation platforms, run the following command in `NPB3.4-OMP` and specify your desired platform as `platform`.

```shell
make [workload] CLASS=[class] PLATFORM=[platform]
```

Your choices for `workload` are listed below:

* BT
* CG
* DC
* EP
* FT
* IS
* LU
* MG
* SP
* UA

For your choices of `class` for each `workload` please refer to `NPB3.4-OMP/README.install`.

You choices of `platform` are either **papi** or **gem5**.
If `PLATFORM` is not specified it assumes the value **native**.

**NOTE**: To compile a list of all the benchmarks with their A,B,D sizes you can run `build_npb.sh` located in `NPB3.4-OMP` at your own risk.
Note that some benchmarks, do not have all the sizes.
In those cases, the biggest size available has been chosen.

## Building Branson

**NOTE**: Please make sure to refer to instructions found in `branson` for compiling Branson.
The following commands have been tested to work on ARM-based machines with Ubuntu 22.04.

In order to build Branson run the following commands in the base directory.

```shell
cd branson
mkdir build
cd build
cmake ../src -DCMAKE_BUILD_TYPE=Release -DCMAKE_ANNOTATE_TYPE=[platform]
make
```

After running the commands the binary for Branson should be in `branson/build/BRANSON`.


## Building Simple Vectorizable Benchmarks

These benchmarks consist of the following workloads.
They are all located in `simple-vector-bench`.

* gups
* permutating-gather
* permutating-scatter
* spatter
* stream

Each workload can be built with three possible targets: **native**, **papi**, and **gem5**.
To build all targets you can either specify **all** or not specify anything.
You can also specify to whether use SVE extensions from the ARM isa.
To do that just append `EXTENSION=sve` to you make command.

To build these benchmarks, run the following command inside each workload's directory.

```shell
make [target] {EXTENSION=sve}
```

As an example run `make gem5 EXTENSION=sve` to build the binary (with sve) for running on gem5.

## Building Microbenchmarks

Each workload can be built with three possible targets: **native**, **papi**, and **gem5**.
To build all targets you can either specify **all** or not specify anything.
The current Makefile in `microbench/Makefile` does not allow for compiling individual microbenchmarks.
To build all the microbenchmarks run the following command in `microbench`.

```shell
make [target]
```

As an example run `make gem5` to build all the microbenchmarks for running on gem5.
