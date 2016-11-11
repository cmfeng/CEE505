# HW3
The goal of this assignment is to explore methods for reading from a file, processing the file input (line-by-line), and performing sensible data analysis on that data.  
Develop a python program that  

### 1 opens a provided file (CEE_220_Scores.txt)  
### 2 reads and analyzes the header line to identify what columns contain "Assignment"s, "Lab"s, "Midterm"s, and the "Final" so you can organize the subsequent data lines into the respective four groups.  
### 3 reads the second line and used information from 2. to compute target scores for each group  
### 4 loops through the remaining lines (list of students) and computes total points assigned for each of the four groups.  
compute a weighted score  
compute the grade  
store name, group point sums (the four discussed above), weighted score, and grade in a dictionary with sensible keys (name for the entry) and collect these in a growing list of student results.  
Perform a statistical analysis of all assigned grades using pyplot's hist function.  Use bins in 0.1 intervals (one by grade) and do not normalize the plot but rather show the actual number of students who received a particular grade. Check the online documentation for additional plot control features to add axis labels and title as shown in the following example figure.Use the pyplot.savefig() method to automatically generate a pdf (mac) or png (windows) file for your report.  
Include sensible error handling for missing data, IO-errors, or other likely problems.  
After testing with the dataset in CEE_220_Scores.txt and comparing results to the above image, run your code on the alternative file CEE_220_AlternativeList.txt and present the statistics (figure) in your report This is to test your ability to identify columns as requested under point 2.
