Work in progress for a base convertion/operation personal project.
http://base-convert.herokuapp.com/

To do (in order of priority):
Handling of decimal inputs - currently outputs rubbish (may require significant changes)
Handling of non-correct inputs e.g. inputting A(base 10) should return error, but currently handled as 11(base 10)
Handling of errors - not all errors go to error.html
Fix error.html rendering issue (background doesn't extend all of the way)
More elegant solution for base 1 than a special exemption in base.py