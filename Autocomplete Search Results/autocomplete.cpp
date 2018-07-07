//See autocomplete.h for description of function variables,
// return values, and purpose

#include "autocomplete.h"

void Autocomplete::merge(int left, int right, int x) {
	int middle = (left + right) / 2;
	int i1 = 0;
	int i2 = left;
	int i3 = middle + 1;

	vector<Term> temp (right - left + 1);
	
	//Merge in sorted for the 2 vectors
	while (i2 <= middle && i3 <= right) {
		//Sort in lexicographic order
		if (x == 1) {
			if (terms[i2].query < terms[i3].query)
				temp[i1++] = terms[i2++];
		
			else
				temp[i1++] = terms[i3++];
		}
		//Sort in descending weight order
		else if (x == 2) {
			if (terms[i2].weight > terms[i3].weight)
				temp[i1++] = terms[i2++];
		
			else
				temp[i1++] = terms[i3++];
		}

	}

	//Merge the remaining elements in left vector
	while (i2 <= middle)
		temp[i1++] = terms[i2++];
	
	//Merge the remaining elements in right vector
	while (i3 <= right)
		temp[i1++] = terms[i3++];

	//Move from temp vector to master vector
	for (int i = left; i <= right; i++)
		terms[i] = temp[i-left];
}

void Autocomplete::MergeSort(int left, int right, int x) {
	if (left < right) {
		int middle = (left + right) / 2;
		MergeSort(left, middle, x);
		MergeSort(middle + 1, right, x);
		merge(left, right, x);
	}
}

void Autocomplete::insert(Term newterm) {
	terms.push_back(newterm);
}

int Autocomplete::BS_helper(vector<Term> &terms, string key, int left, int right) {
	while (left <= right) {
		int middle = (left + right) / 2;
		//If .compare returns 0 then the given prefix matches 
		// the prefix of the term being compared;
		if (terms[middle].query.compare(0, key.size(), key) == 0)
			return middle;
		else if (terms[middle].query > key)
			right = --middle;
		else
			left = ++middle;
	}
	//If a match is not found then return -1
	return -1;
}

bool Autocomplete::Search(string key, int& left, int& right) {
	bool found;
	clock_t tstart, tstop;
	tstart = clock();

	//Use the middle index as a starting point for
	// sequential searching
	int middle = BS_helper(terms, key, left, right);

	//If a match is found, begin sequential search
	if (middle != -1) {

		//Start at middle and search/compare forward
		bool match = true;
		int i = middle + 1;
		//Increment i until a match is no longer found
		// then set the final value of i
		while (match) {
			match = false;
			//"compare" method returns 0 if "key" matches
			// "terms[i].query" from index 0 to index key.size()
			if (terms[i].query.compare(0, key.size(), key) == 0) {
				match = true;
				i++;
			}
			right = i;
		}
		
		//Start at middle and search/compare backward
		match = true;
		i = middle - 1;

		while (match) {
			match = false;
			if (terms[i].query.compare(0, key.size(), key) == 0) {
				match = true;
				i--;
			}
			left = i + 1;
		}

		found = true;
	}
	else
		found = false;

	tstop = clock();
	elapsed_secs = double(tstop - tstart) / CLOCKS_PER_SEC;

	return found;
}
	
vector<Term> Autocomplete::allMatches(string prefix) {
	int left = 0;
	int right = terms.size() - 1;
	//Set "left" and "right"  to their appropriate index values
	// for the sequence of matches
	Search(prefix, left, right);
	
	//From the vector of all terms ("terms"), use "left" and
	// "right" to create a subvector of matches to be sorted 
	// in descending weight order
	vector<Term>::const_iterator start = terms.begin() + left;
	vector<Term>::const_iterator end = terms.begin() + right;
	vector<Term> matches(start, end);

	//Sort the subvector of matches in descending weight order
	Autocomplete autocomplete2;
	autocomplete2.terms = matches;
	autocomplete2.MergeSort(0, matches.size() - 1, 2);

	return autocomplete2.terms;
}

void Autocomplete::print() {
	for (int i = 0; i < terms.size(); i++)
		terms[i].print();
}

double Autocomplete::getTime() {
	return elapsed_secs;
}

int Autocomplete::getSize() {
	return terms.size();
}
