
CC=gcc

all: papi gem5 native

papi: make_dir libroi.papi.a libroi.papi.so roi.papi
gem5: make_dir libroi.gem5.a libroi.gem5.so roi.gem5
native: make_dir libroi.native.a libroi.native.so roi.native

make_dir:
	mkdir -p lib

libroi.papi.a: roi.c
	$(CC) -c $< -o lib/$@ -DPAPI --static -Ipapi/install/include

libroi.gem5.a: roi.c
	$(CC) -c $< -o lib/$@ -DGEM5 --static -Igem5/include

libroi.native.a: roi.c
	$(CC) -c $< -o lib/$@ --static

libroi.papi.so: roi.c
	$(CC) -c $< -o lib/$@ -DPAPI -Ipapi/install/include

libroi.gem5.so: roi.c
	$(CC) -c $< -o lib/$@ -DGEM5 -Igem5/include

libroi.native.so: roi.c
	$(CC) -c $< -o lib/$@

roi.papi: roi.c
	$(CC) -c $< -o lib/$@ -DPAPI -Ipapi/install/include

roi.gem5: roi.c
	$(CC) -c $< -o lib/$@ -DGEM5 -Igem5/include

roi.native: roi.c
	$(CC) -c $< -o lib/$@

clean:
	rm -f lib/libroi.papi.a lib/libroi.papi.so lib/roi.papi
	rm -f lib/libroi.gem5.a lib/libroi.gem5.so lib/roi.gem5
	rm -f lib/libroi.native.a lib/libroi.native.so lib/roi.native
