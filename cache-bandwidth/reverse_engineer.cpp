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

#ifndef L3_SIZE_BYTES
#define L3_SIZE_BYTES 2097152
#endif // L3_SIZE_BYTES

void test(uint32_t test_size)
{
    int num_elements = (int) (L3_SIZE_BYTES / sizeof(uint32_t));
    uint32_t* array = new uint32_t[num_elements];

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 128);

    std::cout << "Initializing an array with " << num_elements << " uint32_t elements." << std::endl;
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
    int num_test_elements = (int) (test_size / sizeof(uint32_t));
    for (int iteration = 0; iteration < ITERS_PER_TEST; iteration++) {
        for (int i = 0; i < num_test_elements; i+= 8) {
            sum += array[(iteration * num_test_elements + i + 0) % num_elements];
            sum += array[(iteration * num_test_elements + i + 1) % num_elements];
            sum += array[(iteration * num_test_elements + i + 2) % num_elements];
            sum += array[(iteration * num_test_elements + i + 3) % num_elements];
            sum += array[(iteration * num_test_elements + i + 4) % num_elements];
            sum += array[(iteration * num_test_elements + i + 5) % num_elements];
            sum += array[(iteration * num_test_elements + i + 6) % num_elements];
            sum += array[(iteration * num_test_elements + i + 7) % num_elements];
            sum %= test_size;
        }
    }
#ifdef PAPI
    roi_end_();
#endif // PAPI
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "Chunk bandwidth test results:" << std::endl
    << "sum: " << sum << std::endl
    << "Number of bytes read in each iteration: " << test_size << std::endl
    << "Number of iterations: " << ITERS_PER_TEST << std::endl
    << "Total time for test: " << duration.count() << " us" << std::endl
    << "Bandwidth: " << ((double) test_size / duration.count()) * ((double) ITERS_PER_TEST / 1e3) << " GB/s" << std::endl;

    return;
}

int main(int argc, char** argv)
{
    if (argc != 2) {
        std::cout << "To run the cache bandwidth test please use this binary "
        << "like below:" << "\n\tcache_bandwidth test_size: number of bytes to read for bandwidth measurement." << std::endl;
        return 1;
    }
    uint32_t test_size = std::stoi(argv[1]);
    test(test_size);
    return 0;
}