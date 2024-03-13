CC?=gcc
CXX?=g++
CFLAGS=-O3 -fopenmp
CXXFLAGS=-O3 -fopenmp
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
	$(CC) -c -o $(BIN_DIR)/kernels.o scatter_gather_kernels.c $(CFLAGS) -Iinclude

papi: kernels
	$(CXX) -o $(BIN_DIR)/spatter$(EXT).papi spatter.cpp $(BIN_DIR)/kernels.o $(CXXFLAGS) -Iinclude -Ijson/single_include/nlohmann -I$(ROI_DIR)/include -I$(ROI_DIR)/papi/install/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/papi/install/lib -lroi.papi -lpapi -lpthread

gem5: kernels
	$(CXX) -o $(BIN_DIR)/spatter$(EXT).gem5 spatter.cpp $(BIN_DIR)/kernels.o $(CXXFLAGS) -Iinclude -Ijson/single_include/nlohmann -I$(ROI_DIR)/include -I$(ROI_DIR)/gem5/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/gem5/lib -lroi.gem5fs -lm5

native: kernels
	$(CXX) -o $(BIN_DIR)/spatter$(EXT).native spatter.cpp $(BIN_DIR)/kernels.o $(CXXFLAGS) -Iinclude -Ijson/single_include/nlohmann -I$(ROI_DIR)/include -L$(ROI_DIR)/lib -lroi.native

clean:
	rm -f $(BIN_DIR)/spatter.papi $(BIN_DIR)/spatter-sve.papi
	rm -f $(BIN_DIR)/spatter.gem5 $(BIN_DIR)/spatter-sve.gem5
	rm -f $(BIN_DIR)/spatter.native $(BIN_DIR)/spatter-sve.native
	rm -f $(BIN_DIR)/kernels.o
