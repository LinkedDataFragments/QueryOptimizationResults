# Log format
Every query line is followed by a result line, unless there was a problem executing that query.

Result lines are of the format ![{time for first result}];[{http calls for first result}];{total time};{total http calls};{nr of results}[;TIMEOUT]

The log files can be parsed using https://github.com/LinkedDataFragments/Client.js/blob/query-optimization/parse_watdiv.py
