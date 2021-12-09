'''
6.5-2
Illustrate the operation of MAX-HEAP-INSERT.A; 10/ on the heap A D h15; 13; 9;
5; 12; 8; 7; 4; 0; 6; 2; 1i.
6.5-3
Write pseudocode for the procedures HEAP-MINIMUM, HEAP-EXTRACT-MIN,
HEAP-DECREASE-KEY, and MIN-HEAP-INSERT that implement a min-priority
queue with a min-heap.
6.5-4
Why do we bother setting the key of the inserted node to 1 in line 2 of MAXHEAP-INSERT when the next thing we do is increase its key to the desired value?

6.5-5
Argue the correctness of HEAP-INCREASE-KEY using the following loop invariant:
At the start of each iteration of the while loop of lines 4–6, the subarray
AŒ1 : : A:heap-size satisfies the max-heap property, except that there may
be one violation: AŒi may be larger than AŒPARENT.i /.
You may assume that the subarray AŒ1 : : A:heap-size satisfies the max-heap property at the time HEAP-INCREASE-KEY is called.
6.5-6
Each exchange operation on line 5 of HEAP-INCREASE-KEY typically requires
three assignments. Show how to use the idea of the inner loop of INSERTIONSORT to reduce the three assignments down to just one assignment.
6.5-7
Show how to implement a first-in, first-out queue with a priority queue. Show
how to implement a stack with a priority queue. (Queues and stacks are defined in
Section 10.1.)
6.5-8
The operation HEAP-DELETE.A; i / deletes the item in node i from heap A. Give
an implementation of HEAP-DELETE that runs in O.lg n/ time for an n-element
max-heap.
6.5-9
Give an O.n lg k/-time algorithm to merge k sorted lists into one sorted list,
where n is the total number of elements in all the input lists. (Hint: Use a minheap for k-way merging.)
'''