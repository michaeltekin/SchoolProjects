#ifndef term_h
#define term_h

#include <string>
#include <iostream>

using namespace std;

class Term {
	public:
		Term();
		Term(string query, long weight);
		
		//It takes longer to call one of the following two
		// functions than it does to simply implement them
		// directly where I need them

		/*
		//Each comparison function returns 1, 0, or -1.
		//When comparing two terms, if the first and second are
		// in the right order, it returns 1; if they are in the
		// wrong order, it returns -1; if they are the same, it
		// returns 0.
				
		//Compares two terms to check if they are in descending
		// weight order
		int byReverseWeightOrder(Term that);

		//Compares two terms to check if they are in lexicographic
		// order
		int compareTo(Term that);
		*/
		
		void print();

		friend class Autocomplete;

	private:
		string query;
		long weight;
};

#endif
