
all: papi gem5 native

papi: roi.papi
gem5: roi.gem5
native: roi.native

roi.papi: roi.c
	$(CC) -c $< -o lib/$@ -DPAPI -Ipapi/install/include -Lpapi/install/lib -lpapi -lpthread

roi.gem5: roi.c
	$(CC) -c $< -o lib/$@ -DGEM5 -Igem5/include -Lgem5/lib/m5/arm64 -lm5

roi.native: roi.c
	$(CC) -c $< -o lib/$@

clean:
	rm -f lib/roi.papi
	rm -f lib/roi.gem5
	rm -f lib/roi.native
