#ifndef __STREAM_KERNELS__
#define __STREAM_KERNELS__

#include <unistd.h>

typedef double TElement;

void do_copy(TElement* __restrict__ dst, TElement* __restrict__ src, const size_t array_size);

void do_scale(TElement* __restrict__ dst, TElement* __restrict__ src, const TElement scale_factor, const size_t array_size);

void do_add(TElement* __restrict__ dst, TElement* __restrict__ src1, TElement* __restrict__ src2, const size_t array_size);

void do_triad(TElement* __restrict__ dst, TElement* __restrict__ src1, TElement* __restrict__ src2, const TElement scale_factor, const size_t array_size);

#endif // __STREAM_KERNELS__
