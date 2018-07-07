#ifndef autocomplete_h
#define autocomplete_h

#include "term.h"
#include <vector>
#include <ctime>

class Autocomplete {
	public:
		//left and right are index values for the vector of terms ("terms")
		//If x is 1: the vector is sorted in lexicographic order
		// If x is 2: the vector is sorted in descending weight order
		//MergeSort helper
		void merge(int left, int right, int x);
		//Sort in lexicographic order using MergeSort algorithm
		void MergeSort(int left, int right, int x);

		//Inserts a new term into "terms'
		void insert(Term newterm);

		//Return the index number of the search key
		// using binary search algorithm
		//left and right (and middle) are index values for the entire list
		// of terms ("terms")
		int BS_helper(vector<Term> &v, string key, int left, int right);

		//Search calls BS_helper. 
		//If BS_helper finds a match then search: 
		// 1. sets the first and last index values for terms sorted in lexicographic order
		// 2. sets elapsed_secs to the time taken to perform the search
		// 3. returns true (indicating a match was found)
		// Otherwise, if BS_helper does not find a match then search:
		// 1. sets elapsed_secs to the time taken to call BS_helper
		// 2. returns false (indicating a match was not found)

		//left is changed from the index value of the first term to the index
		// value of the first matching term
		//right is changed from the index value of the last term to the index
		// value of the last matching term

		bool Search(string key, int& left, int& right);

		//Returns a vector of terms that start with the given prefix,
		// in descending order of weight
		vector<Term> allMatches(string prefix);
	
		//Display each term in terms
		void print();
		
		//Returns "elapsed_secs"
		double getTime();

		//Returns size of "terms"
		int getSize();

	private:
		vector<Term> terms; //Container for sequence of term objects
		double elapsed_secs;
};

#endif
