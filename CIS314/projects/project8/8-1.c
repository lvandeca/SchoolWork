/*
Author: Luke Vandecasteele
Date: 3/12/2021 Last Modified: 3/13/2021
Credits: Class notes, Assignment8.pdf in folder
Description: Simulation of a 64B direct mapped cache with 4B blocks and 16 sets.
Notes:
        1. None
*/

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

void freeCache(struct Cache *cache)
{
    free(cache->lines);
    free(cache);
}

//=================================My Methods==================================

struct Cache *mallocCache(int numLines)
{
    //malloc a a pointer to a struct Cache
    //only continue if malloc call succeeds
    struct Cache *newCache = (struct Cache *)malloc(sizeof(struct Cache));
    if (newCache != NULL)
    {
        //malloc an array of struct Line instances of length "numLines"
        //only continue if malloc call suceeds
        struct Line *lines = (struct Line *)malloc(
            sizeof(struct Line) * numLines);

        if (lines != NULL)
        {
            //initialize each struct Line in the array
            //to have an invalid cache line (i.e. set valid = 0)
            for (int set = 0; set < numLines; set++)
            {
                struct Line *cacheLine = &lines[set];
                cacheLine->valid = 0;
            }
            //store numLines and array of struct Line in our new
            //struct Cache instance
            newCache->numLines = numLines;
            newCache->lines = lines;
        }
        else
        {
            //malloc call for an array of struct Line failed
            //must free the newCache instance
            free(newCache);
            newCache = NULL;
        }
    }

    //return the new struct Cache pointer
    return newCache;
}

void printCache(struct Cache *cache)
{
    int numlines = cache->numLines;
    int set;

    //iterate through each set in the cache
    for (set = 0; set < numlines; set++)
    {
        //get the line in the cache with the relevant set
        struct Line *line = &cache->lines[set];

        //if the line in cache has a valid tag, print the line's information
        if (line->valid)
        {
            //simpel helper for printing the date in the current line of cache
            unsigned char *data = line->data;
            printf("set: %x - tag: %x - valid: %x - data: %.2x %.2x %.2x %.2x\n",
                   set, line->tag, line->valid,
                   data[0], data[1], data[2], data[3]);
        }
    }
}

void readValue(struct Cache *cache, unsigned int address)
{
    //get the relevant fields from the address
    unsigned int s = getSet(address);
    unsigned int t = getTag(address);
    unsigned int o = getOffset(address);
    printf("looking for set: %d - tag: %d\n", s, t);

    //get the cache line determined by the set of the address
    struct Line *line = &cache->lines[s];

    //continue if the line has data in it (i.e. valid != 0)
    if (line->valid)
    {
        //print the set we found in the cache along with its data
        printf("found set: %x - tag: %x - offset: %x - valid: %x - data: %.2x\n",
               s, line->tag, o, line->valid, line->data[o]);

        //check if the tag in our set matches the tag of the given address
        if (line->tag == t)
        {
            printf("hit!\n");
        }
        else
        {
            //line in cache has different data so we have a conflict miss
            printf("tags don't match - conflict miss!\n");
        }
    }
    else
    {
        //not a valid line in the set
        printf("no valid line found - cold miss!\n");
    }
}

//=============================================================================

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

int main()
{
    struct Cache *cache = mallocCache(16);
    // Loop until user enters 'q'
    char c;
    do
    {
        printf("Enter 'r' for read, 'w' for write, 'p' to print, 'q' to quit: ");
        scanf(" %c", &c);
        if (c == 'r')
        {
            printf("Enter 32-bit unsigned hex address: ");
            unsigned int a;
            scanf(" %x", &a);
            readValue(cache, a);
        }
        else if (c == 'w')
        {
            printf("Enter 32-bit unsigned hex address: ");
            unsigned int a;
            scanf(" %x", &a);
            printf("Enter 32-bit unsigned hex value: ");
            unsigned int v;
            scanf(" %x", &v);
            // Get byte pointer to v
            unsigned char *data = (unsigned char *)&v;
            writeValue(cache, a, data);
        }
        else if (c == 'p')
        {
            printCache(cache);
        }
        printf("\n");
    } while (c != 'q');

    freeCache(cache);
}
