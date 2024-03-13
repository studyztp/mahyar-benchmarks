
CXX=g++
ROI_DIR=$(PWD)/../roi
CXXFLAGS=-O3
CXXFLAGS_PAPI=-I$(ROI_DIR)/include -I$(ROI_DIR)/papi/install/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/papi/install/lib -lroi.papi -lpapi -lpthread

L1_SIZE_BYTES=32768
L2_SIZE_BYTES=524288
L3_SIZE_BYTES=16777216
ITERS_PER_TEST=4096
USER_DEFINES=-DL1_SIZE_BYTES=$(L1_SIZE_BYTES) -DL2_SIZE_BYTES=$(L2_SIZE_BYTES) -DL3_SIZE_BYTES=$(L3_SIZE_BYTES) -DITERS_PER_TEST=$(ITERS_PER_TEST)

all: native papi

native:
	$(CXX) cache_bandwidth.cpp -o cache_bandwidth.native $(CXXFLAGS) $(USER_DEFINES)
	$(CXX) reverse_engineer.cpp -o reverse_engineer.native $(CXXFLAGS) $(USER_DEFINES)
papi:
	$(CXX) cache_bandwidth.cpp -o cache_bandwidth.papi $(CXXFLAGS) $(CXXFLAGS_PAPI) $(USER_DEFINES)
	$(CXX) reverse_engineer.cpp -o reverse_engineer.papi $(CXXFLAGS) $(CXXFLAGS_PAPI) $(USER_DEFINES)
clean:
	rm -rf cache_bandwidth.native cache_bandwidth.papi
	rm -rf reverse_engineer.native reverse_engineer.papi
