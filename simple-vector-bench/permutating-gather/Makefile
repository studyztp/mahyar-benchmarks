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
	$(CC) -c -o $(BIN_DIR)/gather-kernel.o gather_kernel.c $(CFLAGS) -Iinclude

papi: kernels
	$(CXX) -o $(BIN_DIR)/permutating-gather$(EXT).papi permutating_gather.cpp $(BIN_DIR)/gather-kernel.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -I$(ROI_DIR)/papi/install/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/papi/install/lib -lroi.papi -lpapi -lpthread

gem5: kernels
	$(CXX) -o $(BIN_DIR)/permutating-gather$(EXT).gem5 permutating_gather.cpp $(BIN_DIR)/gather-kernel.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -I$(ROI_DIR)/gem5/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/gem5/lib -lroi.gem5fs -lm5

native: kernels
	$(CXX) -o $(BIN_DIR)/permutating-gather$(EXT).native permutating_gather.cpp $(BIN_DIR)/gather-kernel.o $(CXXFLAGS) -Iinclude -I$(ROI_DIR)/include -L$(ROI_DIR)/lib -lroi.native

clean:
	rm -f $(BIN_DIR)/permutating-gather.papi $(BIN_DIR)/permutating-gather-sve.papi
	rm -f $(BIN_DIR)/permutating-gather.gem5 $(BIN_DIR)/permutating-gather-sve.gem5
	rm -f $(BIN_DIR)/permutating-gather.native $(BIN_DIR)/permutating-gather-sve.native
	rm -f $(BIN_DIR)/gather-kernel.o
