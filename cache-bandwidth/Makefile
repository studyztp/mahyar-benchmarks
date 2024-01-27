
CXX=g++
ROI_DIR=$(PWD)/../roi
CXXFLAGS=-O3
CXXFLAGS_PAPI=-I$(ROI_DIR)/include -I$(ROI_DIR)/papi/install/include -L$(ROI_DIR)/lib -L$(ROI_DIR)/papi/install/lib -lroi.papi -lpapi -lpthread

all: native papi

native:
	$(CXX) cache_bandwidth.cpp -o cache_bandwidth.native $(CXXFLAGS)
papi:
	$(CXX) cache_bandwidth.cpp -o cache_bandwidth.papi $(CXXFLAGS) $(CXXFLAGS_PAPI)

clean:
	rm -rf cache_bandwidth.native cache_bandwidth.papi