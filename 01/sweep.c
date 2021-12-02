#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/mman.h>

typedef struct ListInt {
    int *vals;
    size_t size;
    size_t capacity;
} ListInt;

ListInt createListInt(size_t);
void insertListInt(ListInt *, int);

ListInt createListInt(size_t capacity) {
    ListInt vect;
    vect.vals = malloc(capacity * sizeof(int));
    vect.size = 0;
    vect.capacity = capacity;
    return vect;
}

void insertVint(ListInt *vect, int value) {
    size_t idx = vect->size;
    if(idx == vect->capacity) {
        ListInt newVect = createListInt(vect->capacity * 2);
        newVect.capacity = vect->capacity * 2;
        for(size_t i = 0; i < vect->size; i++) {
            newVect.vals[i] = vect->vals[i];
            newVect.size++;
        }

        free(vect->vals);
        vect->vals = newVect.vals;
        vect->capacity = newVect.capacity;
        vect->size = newVect.size;
    }
    vect->vals[idx] = value;
    vect->size++;
}

int main(int argc, char **argv) {
    const char *path = "./input";
    int fd = open(path, O_RDONLY);
    ListInt nums = createListInt(100);

    struct stat inf;
    fstat(fd, &inf);
    void *addr = mmap(NULL, inf.st_size, PROT_WRITE, MAP_PRIVATE, fd, 0);

    const char *delim = "\n";
    char *num = strtok(addr, delim);
    while(num) {
        insertVint(&nums, atoi(num));
        num = strtok(NULL, delim);
    }

    int count = 0;
    for(size_t idx = 1; idx < nums.size; idx++) {
        count += (nums.vals[idx] > nums.vals[idx - 1]);
    }

    printf("%d\n", count);

    free(nums.vals);
    munmap(addr, inf.st_size);
    close(fd);
    return 0;
}
