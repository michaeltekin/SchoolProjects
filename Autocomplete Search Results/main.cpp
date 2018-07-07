//Course: CS216
//Project: Program Assignment 3
//Date: 12-6-16
//Purpose: Autocomplete search results - Sort elements of text file in lexicographic order 
// and then search sorted text file for given number of terms with matching 
// prefix - returning matching terms in descending order of weight.
//Author: Michael Tekin

#include "term.h"
#include "autocomplete.h"
#include <sstream>
#include <fstream>

int main(int argc, char* argv[]) {

	//Quit the program if a text file isn't provided
	if (argc < 2) {
		cout << "Need 1 argument (textfile)" << endl;
		return 1;
	}
	
	//Quit the program if the text file cannot be opened
	ifstream infile;
	infile.open(argv[1]);
	if (!infile.good()) {
		cout << "Cannot open the file named " << argv[1] << endl;
		return 2;
	}

	//Read in the terms of the input file
	Autocomplete autocomplete;
	long weight;
	string query;
	while (!infile.eof()) {
		infile >> weight >> ws;
		getline(infile, query);
		if (query != "") {
			Term newterm(query, weight);
			autocomplete.insert(newterm);
		}
	}	

	//Sort the terms in lexicographical order using mergesort algorithm
	int right = autocomplete.getSize() - 1;
	clock_t tstart, tstop;
	tstart = clock();
	autocomplete.MergeSort(0, right, 1); 
	tstop = clock();
	double elapsed = double(tstop - tstart) / CLOCKS_PER_SEC;
	cout << fixed << "Time for sorting all terms: " 
	<< elapsed << " seconds." << endl;

	//Repeatedly ask the user to type prefix to search for one matched term
	// until the user types "exit" to quit
	string prefix;
	cout << "Please input the search query(type \"exit\" to quit): " << endl;
	getline(cin, prefix);
	while (prefix != "exit") {
		//If the user does not enter a prefix then ask again
		if (prefix != "") {
			int a = 0; //Index value of first element in terms vector
			int b = autocomplete.getSize() - 1; //Index value of last element in terms vector
		
			bool found = autocomplete.Search(prefix, a, b); //Search sets Time
			elapsed = autocomplete.getTime();
			cout << "Time for searching all matched terms: " 
			<< elapsed << endl;
	
			//If a match is found, print the appropriate 
			// number of matches
			if (found) {
				vector<Term> matchingTerms;

				//Create a vector of matching terms that is sorted
				// in reverse weight order
				matchingTerms = autocomplete.allMatches(prefix);
	
				int nterms; //The number of matching terms to print
				//If an argument is given after the filename
				// try to convert that argument into an integer
				if (argc > 2) {
					istringstream ss(argv[2]);
					//If the argument cannot be converted to
					// an integer, then set nterms to all 
					// matching terms
					if (!(ss >> nterms))
						nterms = matchingTerms.size();
					else
						ss >> nterms;
				}
				//If no argument is given after the filename
				// then set nterms to all matching terms 
				else
					nterms = matchingTerms.size();
	
				//If the argument for terms to be printed happens to be greater 
				// than the total number of matching terms, set the number of 
				// terms to be printed to the total number of matching terms 
				if (nterms > matchingTerms.size())
					nterms = matchingTerms.size();
	
				//Print the determined number of matching terms
				for (int i = 0; i < nterms; i++)
					matchingTerms[i].print();
			}
		}
		cout << "Please input the search query(type \"exit\" to quit): " 
		<< endl;
		getline(cin, prefix);
	}

	return 0;

}
