#ifndef __GATHER_KERNEL__
#define __GATHER_KERNEL__
#include <stdint.h>
#include <stddef.h>

typedef uint64_t TElement;
typedef uint64_t TIndex;

void gather(TElement* __restrict__ dst, TElement* __restrict__ src, const TIndex* __restrict__ indices, const size_t array_size);

#endif // __GATHER_KERNEL__