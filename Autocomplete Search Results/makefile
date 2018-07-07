#Use g++ as our compiler
CC = /usr/bin/g++
#Use -g to enable debugging
FLAGS = -g

SOURCES = main.cpp autocomplete.cpp term.cpp
EXEC = CS216PA3

#Create object files with the same name as the .cpp file
# but with .o
OBJECTS = $(SOURCES:.cpp = .o)

#Build executable
$(EXEC): $(OBJECTS)
	$(CC) -o $(EXEC) $(FLAGS) $(OBJECTS)

#Build source files
%.o: %.cpp
	$(CC) $(FLAGS) -c $(.SOURCE)
clean:
	rm -i $(OBJECTS) $(EXEC)
