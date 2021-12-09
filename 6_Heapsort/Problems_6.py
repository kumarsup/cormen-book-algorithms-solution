'''
6-1 Building a heap using insertion
We can build a heap by repeatedly calling MAX-HEAP-INSERT to insert the elements into the heap. Consider the following variation on the BUILD-MAX-HEAP
procedure:

BUILD-MAX-HEAP0
.A/
1 A:heap-size D 1
2 for i D 2 to A:length
3 MAX-HEAP-INSERT.A; AŒi/
a. Do the procedures BUILD-MAX-HEAP and BUILD-MAX-HEAP0 always create
the same heap when run on the same input array? Prove that they do, or provide
a counterexample.
b. Show that in the worst case, BUILD-MAX-HEAP0 requires ‚.n lg n/ time to
build an n-element heap.

6-2 Analysis of d-ary heaps
A d-ary heap is like a binary heap, but (with one possible exception) non-leaf
nodes have d children instead of 2 children.
a. How would you represent a d-ary heap in an array?
b. What is the height of a d-ary heap of n elements in terms of n and d?
c. Give an efficient implementation of EXTRACT-MAX in a d-ary max-heap. Analyze its running time in terms of d and n.
d. Give an efficient implementation of INSERT in a d-ary max-heap. Analyze its
running time in terms of d and n.
e. Give an efficient implementation of INCREASE-KEY.A; i; k/, which flags an
error if k < AŒi, but otherwise sets AŒi D k and then updates the d-ary maxheap structure appropriately. Analyze its running time in terms of d and n.

6-3 Young tableaus
An m 	 n Young tableau is an m 	 n matrix such that the entries of each row are
in sorted order from left to right and the entries of each column are in sorted order
from top to bottom. Some of the entries of a Young tableau may be 1, which we
treat as nonexistent elements. Thus, a Young tableau can be used to hold r  mn
finite numbers.
a. Draw a 4	4 Young tableau containing the elements f9; 16; 3; 2; 4; 8; 5; 14; 12g.
b. Argue that an m 	 n Young tableau Y is empty if Y Œ1; 1 D 1. Argue that Y
is full (contains mn elements) if Y Œm; n < 1.

Give an algorithm to implement EXTRACT-MIN on a nonempty m 	 n Young
tableau that runs in O.m C n/ time. Your algorithm should use a recursive subroutine that solves an m 	 n problem by recursively solving either
an .m  1/ 	 n or an m 	 .n  1/ subproblem. (Hint: Think about MAXHEAPIFY.) Define T .p/, where p D m C n, to be the maximum running time
of EXTRACT-MIN on any m 	 n Young tableau. Give and solve a recurrence
for T .p/ that yields the O.m C n/ time bound.
d. Show how to insert a new element into a nonfull m 	 n Young tableau in
O.m C n/ time.
e. Using no other sorting method as a subroutine, show how to use an n	n Young
tableau to sort n2 numbers in O.n3/ time.
f. Give an O.m C n/-time algorithm to determine whether a given number is
stored in a given m 	 n Young tableau.
'''