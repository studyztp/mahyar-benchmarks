#ifndef __SCATTER_GATHER_KERNELS__
#define __SCATTER_GATHER_KERNELS__

#include <stdint.h>
#include <stddef.h>

typedef double TElement;
typedef uint64_t TIndex;

void gather(TElement* __restrict__ dst, TElement* __restrict__ src, const TIndex* __restrict__ indices, const size_t array_size);
void scatter(TElement* __restrict__ dst, TElement* __restrict__ src, const TIndex* __restrict__ indices, const size_t array_size);

#endif // __SCATTER_GATHER_KERNELS__