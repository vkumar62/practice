#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <inttypes.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

typedef struct timespec timespec_t;

#define TIME_NSECS_PER_SEC                           1000000000ULL

static inline void
timestamp_to_nsecs (timespec_t *ts, uint64_t *nsecs)
{
    *nsecs = ts->tv_nsec;
    *nsecs += (uint64_t) (ts->tv_sec * TIME_NSECS_PER_SEC);
}

typedef struct {
    uint32_t left;
    uint32_t right;
    uint32_t mid;
} counts_t;

counts_t counts[256];



uint32_t 
max_consecutive_ones_a1 (uint8_t *a, uint32_t n)
{
    uint32_t max = 0;
    uint32_t prev_left = 0;

    for (uint32_t i = 0; i < n; i++) {
        uint32_t left = counts[a[i]].left;
        uint32_t right = counts[a[i]].right;
        uint32_t mid = counts[a[i]].mid;

        max = MAX(max, prev_left + right);
        max = MAX(max, mid);

        if ((left == right) && (left == 8)) {
            prev_left += left;
        } else {
            prev_left = left;
        }
    }
    return max;
}


uint32_t 
max_consecutive_ones_a2 (uint8_t *a, uint32_t n)
{
    uint32_t max = 0;
    uint32_t cur = 0;

    for (uint32_t i = 0; i < n; i++) {
        for (uint32_t j = 0; j < 8; j++) {
            if ((a[i] >> j) & 0x1) {
                cur++;
            } else {
                cur = 0;
            }
            max = MAX(max, cur);
        }
    }
    return max;
}

void
populate_counts (void)
{
    for (uint32_t i = 0; i < 256; i++) {
        uint8_t val = ~i & 0xff;
        counts[i].left = val ? __builtin_clz(val) - 24 : 8;
        counts[i].right = val ? __builtin_ctz(val) : 8;
        counts[i].mid = max_consecutive_ones_a2((uint8_t *)&i, 1);
        printf("0x%02X\t left %d right %d mid %d\n", i, counts[i].left, counts[i].right, counts[i].mid);
    }
}

int
main (void)
{
    populate_counts();

    struct timespec start;
    struct timespec end;

    uint64_t start_ns;
    uint64_t end_ns;

    uint32_t COUNT = 1<<25;

    clock_gettime(CLOCK_REALTIME, &start);
    for (uint32_t i = 0; i < COUNT; i++) {
        uint64_t val = i;
        max_consecutive_ones_a1((uint8_t *)&val, 8);
    }
    clock_gettime(CLOCK_REALTIME, &end);

    timestamp_to_nsecs(&start, &start_ns);
    timestamp_to_nsecs(&end, &end_ns);
    printf("a1 time %"PRId64 "\n", end_ns-start_ns);

    clock_gettime(CLOCK_REALTIME, &start);
    for (uint32_t i = 0; i < COUNT; i++) {
        uint64_t val = i;
        max_consecutive_ones_a2((uint8_t *)&val, 8);
    }
    clock_gettime(CLOCK_REALTIME, &end);

    timestamp_to_nsecs(&start, &start_ns);
    timestamp_to_nsecs(&end, &end_ns);
    printf("a2 time %"PRId64 "\n", end_ns-start_ns);

#if 0
    for (uint32_t i = 0; i < COUNT; i++) {
        uint64_t val = i;

        uint32_t c1 = max_consecutive_ones_a1((uint8_t *)&val, 8);
        uint32_t c2 = max_consecutive_ones_a2((uint8_t *)&val, 8);
        
        if (c1 != c2) {
            printf("ERROR val 0x%x c1 %d c2 %d\n", val, c1, c2);
            break;
        }
    }
#endif

    return 0;
}

