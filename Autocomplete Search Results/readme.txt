//Course: CS216
//Project: Program Assignment 3
//Date: 12-6-16
//Purpose: Autocomplete search results - Sort elements of text file in lexicographic order 
// and then search sorted text file for given number of terms with matching 
// prefix - returning matching terms in descending order of weight.
//Author: Michael Tekin

Originally I used bubble sort to sort in lexicographic and descending weight order.

Since it took so long, I decided to use merge sort to sort in lexicographic order and continued to use bubble sort to sort the sequence of matches to a query in descending weight order. However, searching for something like "The" in the imdb list would take over 1 second to complete. So I got rid of bubble sort altogether and decided to only use merge sort.

Bubble sort is O(n^2). I chose to use merge sort because its worse-case performance is O(n log n) which is a huge improvement compared to O(n^2) when n is large.

