//See term.h for description of function variables,
// return values, and purpose

#include "term.h"

Term::Term() {}

Term::Term(string q, long w) : query(q), weight(w) {}

/*
int Term::byReverseWeightOrder(Term that) {
	if (this->weight > that.weight)
		return 1;
	else if (this->weight < that.weight)
		return -1;
	else
		return 0;
}

int Term::compareTo(Term that) {
	if (this->query < that.query)
		return 1;
	else if (this->query > that.query)
		return -1;
	else
		return 0;
}
*/

void Term::print() {
	cout << this->weight << " " << this->query << endl;
}

