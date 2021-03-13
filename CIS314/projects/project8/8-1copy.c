#include <stdio.h>
#include <stdlib.h>
struct Line
{
    unsigned char data[4];
    unsigned int tag;
    unsigned char valid;
};

struct Cache
{
    struct Line *lines;
    int numLines;
};

unsigned int getOffset(unsigned int address)
{ // 4B blocks, so offset is bits 0-1
    return address & 0x3;
}

unsigned int getSet(unsigned int address)
{ // 16 sets, so offset is bits 2-6
    return (address >> 2) & 0xF;
}
unsigned int getTag(unsigned int address)
{
    // Offset and set are 6 bits total, so tag is high-order 26 bits
    return address >> 6;
}
struct Cache *mallocCache(int numLines)
{
    // TODO - malloc a pointer to a struct Cache, malloc a pointer to an array
    // of struct Line instances (array length is numLines). Also initialize
    // valid to 0 for each struct Line. Return the struct Cache pointer.

    struct Cache *newCache = (struct Cache *)malloc(sizeof(struct Cache *));
    if (newCache != NULL)
    {
        struct Line *lines = (struct Line *)malloc(sizeof(struct Line *) * numLines);
        if (lines != NULL)
        {
            for (int set= 0; set < numLines; set++)
            {
                struct Line *cacheLine = &lines[set];
                cacheLine->valid = 0;
            }
            newCache->numLines = numLines;
            newCache->lines = lines;
        }
        else
        {
            free(newCache);
            newCache = NULL;
        }
    }
    return newCache;
}
void freeCache(struct Cache *cache)
{
    free(cache->lines);
    free(cache);
}
void printCache(struct Cache *cache)
{
    // TODO - print all valid lines in the cache.

    struct Line *lines = cache->lines;
    int numlines = cache->numLines;
    int set;

    for (set = 0; set < numlines; set++)
    {
        struct Line *cacheLine = &lines[set];
        if (cacheLine->valid)
        {
            printf("set: %d - tag: %x - valid: %u - data: %.2x %.2x %.2x %.2x\n",
                   set, cacheLine->tag, cacheLine->valid, cacheLine->data[0],
                   cacheLine->data[1], cacheLine->data[2], cacheLine->data[3]);
        }
    }
}

void readValue(struct Cache *cache, unsigned int address)
{
    // TODO - check the cache for a cached byte at the specified address.
    // If found, indicate a hit and print the byte.  If not found, indicate
    // a miss due to either an invalid line (cold miss) or a tag mismatch
    // (conflict miss).

    unsigned int s = getSet(address);
    unsigned int t = getTag(address);
    unsigned int o = getOffset(address);
    printf("looking for set: %d - tag: %d\n", s, t);

    struct Line *line = &cache->lines[s];

    if (line->valid)
    {
        printf("found set: %d - tag: %d - offset: %d - valid: %d - data: %.2x %.2x %.2x %.2x\n",
               s, line->tag, o, line->valid, line->data[0], line->data[1], line->data[2], line->data[3]);

        if (line->tag == t)
        {
            printf("hit!\n");
        }
        else
        {
            printf("tags don't match = conflict miss\n");
        }
    }
    else
    {
        printf("no valid line found - cold miss!\n");
    }
}

void writeValue(struct Cache *cache, unsigned int address, unsigned char *newData)
{ // Calculate set and tag for address
    unsigned int s = getSet(address);
    unsigned int t = getTag(address);
    // Get pointer to cache line in the specified set
    struct Line *line = &cache->lines[s];
    // Determine if we have a valid line in the cache that does not contain the
    // specified address - we detect this by checking for a tag mismatch
    if (line->valid && line->tag != t)
    {
        unsigned char *data = line->data;
        printf("evicting line - set: %x - tag: %x - valid: %u - data: %.2x %.2x %.2x %.2x\n",
               s, line->tag, line->valid, data[0], data[1], data[2], data[3]);
    }
    // Copy new data to line (could use memcpy here instead)
    for (int i = 0; i < 4; ++i)
    {
        line->data[i] = newData[i];
    }

    // Update line tag, mark line as valid
    line->tag = t;
    line->valid = 1;
    printf("wrote set: %x - tag: %x - valid: %u - data: %.2x %.2x %.2x %.2x\n",
           s, line->tag, line->valid, newData[0], newData[1], newData[2], newData[3]);
}

int main(){
    struct Cache *cache = mallocCache(16);

    
}