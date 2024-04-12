# Conway's Game of Life

Right around when the C language was first released, one mathematician thought
up a game that nobody would want play to play. The rules are simple, on an
infinitely sized grid there are "live" and "dead" squares. On each round, we
update the grid based on the neighbours of each square. Neighbours are the (up
to) 8 squares directly around one square:

 1. If a square has 0, 1, 4, 5, 6, 7, or 8 "live" neighbours, it's set to "dead"
 2. If a square is currently "live" and has 2 "live" neighbours, it remains
    "live"
 3. If a square has 3 "live" neighbours, set it or keep it "live"

This very simple ruleset allows for some pretty interesting "game play". Some
patterns become reoccurring and are able to effectively move. The most basic one
is the glider. Here is a glider over multiple rounds of play:


```
Round 1 | Round 2 | Round 3 | Round 4 | Round 5
...X..  | ..X...  | ...X..  | ......  | ......
.X.X..  | ...XX.  | ....X.  | ..X.X.  | ....X.
..XX..  | ..XX..  | ..XXX.  | ...XX.  | ..X.X.
......  | ......  | ......  | ...X..  | ...XX.
......  | ......  | ......  | ......  | ......
......  | ......  | ......  | ......  | ......
```

Notice how the pattern from round 1 reoccurs in round 5, but now it's moved
over one down and one right. There are some very complicated patterns that are
able to reoccur!

If you want a better understanding of how this works, check out [this web-based
implementation of Conway's Game of Life](https://playgameoflife.com/).

In this lab, your task is to implement Conway's Game of Life. Unfortunately, it
would be very challenging to implement on an unlimited sized grid in both
directions. Instead, we will have only 6 rows, but 2^32 columns.

This lab isn't too conceptually difficult, but it will take a while to write.

## Input

Your input will be in a file name provided in the command line arguments to your
program. The file will always have valid structure.

The first line of the file contains a single integer greater than or equal to 1:
N. All following lines contain coordinate pairs in the form `%d, %d`. The first
number is the row and the second is the column. Coordinates in our game of life
are all 1 indexed, meaning the first number will be 1-6 and the second will be
1-2000000000.

For each coordinate pair in the file, set the square at that coordinate to be
"live". Then, play N rounds of Conway's Game of Life. Note that rounds are also
1 indexed, meaning if N = 1, then you don't need to play any rounds. Count and
print the number of "live" cells on the final round to the terminal.

**You must make a Makefile**. This Makefile must **provide the `a.out`** target
to build your program. The following should build it:

```
make a.out
```

## Implementation

Our recommended implementation uses a linked list and a chunking system. Each
chunk is a 6x6 grid. We used the following c-structure to represent this:

```c
typedef struct Chunk {
    int* grid;  // The 6x6 grid. Just an array of 36 integers
    struct Chunk* prev;  // Previous chunk
    struct Chunk* next;  // Next chunk
    int start_col;  // Starting column of this chunk (1, 7, 13...)
} Chunk;
```

The reason we want a linked list for this is to be memory efficient. We can't
allocate 6 * 2 billion integers in memory, as we don't have enough memory for
that. Instead, we will only allocate the chunks that have live cells and those
right around the live ones.

For example, let's say we have coordinates (1,1), (2,13), (3,13) and (4,13). Our
chunking system would look like:

```
Chunk 1 | Chunk 13
X.....  | ......
......  | X.....
......  | X.....
......  | X.....
......  | ......
......  | ......
```

The linked list in this situation looks like `1 <-> 13`, where `prev` in `1` is
NULL and `next` in `13` is NULL.

The reason we label them chunk 1 and 13 is since that's the left-most column in
each grid. Chunk 1 has columns 1-6 and chunk 13 has columns 13-18. However,
we're actually still missing a chunk. You'll notice that on the next round of
this Game of Life, coordinates (3,12) and (3,14) will become "live", as they
have 3 "live" neighbours. However, the current chunks don't have column 12!

In general, we should be allocating the neighbouring chunks of any chunk with a
"live" square as well, so the above should actually look like:

```
Chunk 1 | Chunk 7 | Chunk 13 | Chunk 18
X.....  | ......  | ......   | ......
......  | ......  | X.....   | ......
......  | ......  | X.....   | ......
......  | ......  | X.....   | ......
......  | ......  | ......   | ......
......  | ......  | ......   | ......
```

Interally, the linked list looks like: `1 <-> 7 <-> 13 <-> 18`. Both the `next` and
`prev` must be set on chunk `7`. Chunk `1` will have a NULL pointer to its
`prev`, since there are no columns smaller than `1`. Chunk `18` will have a NULL
pointer to its `next`, since there's no chunk to its right currently.

Now we can play a round of Game of Life:

```
Chunk 1 | Chunk 7 | Chunk 13 | Chunk 18
......  | ......  | ......   | ......
......  | ......  | ......   | ......
......  | .....X  | XX....   | ......
......  | ......  | ......   | ......
......  | ......  | ......   | ......
......  | ......  | ......   | ......
```

You will need to make sure you allocate adjacent chunks as needed. You may want
to deallocate chunks as well.

You will find you *really* want to do a lot of debugging with this program.
Here's one of the debugging functions we found very useful in implementing our
solution. You can use it in your code without citation:

```c
#define CHUNK_SIZE 6

int* chunk_index_ptr(Chunk* c, int row, int col) {
    return c->grid[(row-1)*CHUNK_SIZE + (col - c->start_col)];
}

void chunk_debug(Chunk* ch) {
    char cha;

    while (ch != NULL) {
        fprintf(stderr, "Chunk: %d\n", ch->start_col);
        int s = ch->start_col;

        for (int r = 1; r <= CHUNK_SIZE; r++) {
            for (int c = s; c <= s + CHUNK_SIZE - 1; c++) {
                cha = chunk_index(ch, r, c) == 0 ? '.' : 'X';
                fprintf(stderr, "%c", cha);
            }
            fprintf(stderr, "\n");
        }
        ch = ch->next;
    }

    fprintf(stderr, "===============\n");
}
```

The edge cases you should be watching out for:
 - Having to check "neighbours" from another chunk, as happens in the edge
   columns
 - Counting neighbours in squares along the bottom and top rows

Rough order of code:
 1. Create a blank chunk 1. Use this as the "root" of the list
 2. Iterate over the coordinates in the input file. Use a recursive
    implementation of `chunk_set` to set all the provided coordinates
 3. For-loop over the number of cycles. In each loop, start by filling in the
    blank adjacent chunks for current chunks, then play a round of the Game of
    Life.
 4. Use a recursive `chunk_count_live` function to count the number of live
    squares along all the chunks.

## Provided Code

This lab is massive, which is why you have 2 weeks. That said, we're still
providing a bit of code to help.

You will have 3 files: `main.c`, `chunk.c`, `chunk.h`. You must make a
`Makefile` to make compilation easier. `chunk.h` has a lot of function headers.
You do **not need to use all** these, feel free to delete many. They are the
function headers you may want to consider using.

Please read `chunk.h` for a description of the functions. You'll see some of
them implemented in `chunk.c`. Much of `main.c` is already written too.

Remember, you do not have to follow the provided code. If you'd like, feel free
to delete and rewrite as much code as you'd like.

## Check

The standard `check.sh` script is provided for this lab. You can run it with:

```bash
bash check.sh
```

You must be in the same directory as your Makefile to run this script. Passing
this script is worth 50% of your non-oral demo.

## Examples

### Input 1

```
4
1,4
2,2
2,4
3,3
3,4
1,1
```

### Output 1

```
9
```

### Debug Example 1

```
Chunk: 1
X..X..
.X.X..
..XX..
......
......
......
===============
Chunk: 1
..X...
.X.XX.
..XX..
......
......
......
===============
Chunk: 1
..XX..
.X..X.
..XXX.
......
......
......
===============
Chunk: 1
..XX..
.X..X.
..XXX.
...X..
......
......
===============
```

### Input 2

This one moves between two chunks

```
10
1,6
2,6
3,6
3,5
2,4
```

### Output 2

```
5
```

### Input 3

```
14
1,6
2,6
3,6
3,5
2,4

2,30
3,30
2,31
```

### Output 3

```
9
```
