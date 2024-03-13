
#include <chrono>
#include <iostream>
#include <random>

#ifdef PAPI
extern "C" {
#include "roi.h"
}
#endif //PAPI

#ifndef ITERS_PER_TEST
#define ITERS_PER_TEST 16384
#endif // ITERS_PER_TEST

#ifndef L1_SIZE_BYTES
#define L1_SIZE_BYTES 65536
#endif // L1_SIZE_BYTES

#ifndef L2_SIZE_BYTES
#define L2_SIZE_BYTES 1048576
#endif // L2_SIZE_BYTES

#ifndef L3_SIZE_BYTES
#define L3_SIZE_BYTES 2097152
#endif // L3_SIZE_BYTES

void test(uint32_t cache_size, const std::string name)
{
    int num_elements = (int) (cache_size / sizeof(uint32_t));
    uint32_t* array = new uint32_t[num_elements];

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 128);

    std::cout << "Initializing an array with "
    << num_elements << " uint32_t elements." << std::endl;
    for (int i = 0; i < num_elements; i++) {
        array[i] = dis(gen);
    }
    std::cout << "Done initializing." << std::endl;


    int sum = 0;
#ifdef PAPI
    annotate_init_();
#endif // PAPI
    auto start = std::chrono::high_resolution_clock::now();
#ifdef PAPI
    roi_begin_();
#endif // PAPI
    for (int iteration = 0; iteration < ITERS_PER_TEST; iteration++) {
        for (int i = 0; i < num_elements; i+= 8) {
            sum += array[i + 0];
            sum += array[i + 1];
            sum += array[i + 2];
            sum += array[i + 3];
            sum += array[i + 4];
            sum += array[i + 5];
            sum += array[i + 6];
            sum += array[i + 7];
            sum %= cache_size;
        }
    }
#ifdef PAPI
    roi_end_();
#endif // PAPI
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << name << " bandwidth test results:" << std::endl
    << "sum: " << sum << std::endl
    << "Number of bytes read in each iteration: " << cache_size << std::endl
    << "Number of iterations: " << ITERS_PER_TEST << std::endl
    << "Total time for test: " << duration.count() << " us" << std::endl
    << "Bandwidth: " << ((double) L2_SIZE_BYTES / duration.count()) * ((double) ITERS_PER_TEST / 1e3) << " GB/s" << std::endl;

    return;
}


int main(int argc, char** argv)
{
    if (argc != 2) {
        std::cout << "To run the cache bandwidth test please use this binary "
        << "like below:" << "\n\tcache_bandwidth {l1, l2, l3}" << std::endl;
        return 1;
    }

    std::string target = argv[1];
    if (target == "l1") {
        test(L1_SIZE_BYTES, "L1");
    } else if (target == "l2") {
        test(L2_SIZE_BYTES, "L2");
    } else if (target == "l3") {
        test(L3_SIZE_BYTES, "L3");
    } else {
        std::cerr << "Target: " << target << " not recognized." << std::endl;
        return -1;
    }

    return 0;
}