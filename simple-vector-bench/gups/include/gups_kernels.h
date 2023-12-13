
#ifndef __GUPS_KERNELS__
#define __GUPS_KERNELS__

#include <stdint.h>

typedef uint64_t TElement;
typedef uint64_t TIndex;
typedef int64_t TSignedIndex;

void doRandomAccess(TElement* __restrict__ table, const TIndex tableSize, const TIndex numUpdates, const TIndex numUpdatesPerBurst);

#endif // __GUPS_KERNELS
