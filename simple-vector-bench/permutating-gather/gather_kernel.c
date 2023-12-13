#include "gather_kernel.h"

void gather(TElement* __restrict__ dst, TElement* __restrict__ src, const TIndex* __restrict__ indices, const size_t array_size) {
    #pragma omp parallel for simd
    for (size_t idx = 0; idx < array_size; idx++)
        dst[idx] = src[indices[idx]];
}

