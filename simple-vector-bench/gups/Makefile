CC?=gcc
CXX?=g++
CFLAGS=-O2 -fopenmp
CXXFLAGS=-O2 -fopenmp
BIN_DIR=bin
ROI_DIR=$(PWD)/../../roi

EXT=
ifeq ($(EXTENSION), sve)
	CFLAGS+=-march=armv8.1-a+sve
	EXT="-sve"
endif

all: papi gem5 native

make_dir:
	mkdir -p $(BIN_DIR)

kernels: make_dir
	$(CC) -c -o $(BIN_DIR)/kernels.o gups_kernels.c $(CFLAGS) -Iinclude

papi: kernels
	$(CXX) -o $(BIN_DIR)/gups$(EXT).papi gups.cpp $(BIN_DIR)/kernels.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -I$(ROI_DIR)/papi/install/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/papi/install/lib -lroi.papi -lpapi -lpthread

gem5: kernels
	$(CXX) -o $(BIN_DIR)/gups$(EXT).gem5 gups.cpp $(BIN_DIR)/kernels.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -I$(ROI_DIR)/gem5/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/gem5/lib -lroi.gem5 -lm5

native: kernels
	$(CXX) -o $(BIN_DIR)/gups$(EXT).native gups.cpp $(BIN_DIR)/kernels.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -L$(ROI_DIR)/lib -lroi.native

clean:
	rm -f bin/gups.papi bin/gups-sve.papi
	rm -f bin/gups.gem5 bin/gups-sve.gem5
	rm -f bin/gups.native bin/gups-sve.native
	rm -f bin/kernels.o
