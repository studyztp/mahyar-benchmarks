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
	$(CC) -c -o $(BIN_DIR)/scatter-kernel.o scatter_kernel.c $(CFLAGS) -Iinclude

papi: kernels
	$(CXX) -o $(BIN_DIR)/permutating-scatter$(EXT).papi permutating_scatter.cpp $(BIN_DIR)/scatter-kernel.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -I$(ROI_DIR)/papi/install/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/papi/install/lib -lroi.papi -lpapi -lpthread

gem5: kernels
	$(CXX) -o $(BIN_DIR)/permutating-scatter$(EXT).gem5 permutating_scatter.cpp $(BIN_DIR)/scatter-kernel.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -I$(ROI_DIR)/gem5/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/gem5/lib -lroi.gem5 -lm5

native: kernels
	$(CXX) -o $(BIN_DIR)/permutating-scatter$(EXT).native permutating_scatter.cpp $(BIN_DIR)/scatter-kernel.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -L$(ROI_DIR)/lib -lroi.native

clean:
	rm -f $(BIN_DIR)/permutating-scatter.papi $(BIN_DIR)/permutating-scatter-sve.papi
	rm -f $(BIN_DIR)/permutating-scatter.gem5 $(BIN_DIR)/permutating-scatter-sve.gem5
	rm -f $(BIN_DIR)/permutating-scatter.native $(BIN_DIR)/permutating-scatter-sve.native
	rm -f $(BIN_DIR)/scatter-kernel.o
