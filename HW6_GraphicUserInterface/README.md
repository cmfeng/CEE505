# HW6 Simple Graphic User Interface (GUI) for your midterm project.
## Given
Your flight database from your midterm solution  
Your Graph class, including a findShortestPath(self) method
## ToDo
create a GUI that creates a Graph containing your flight database as part of the constructor  
implement a method Graph.getAirportCodes(self) to Graph that returns a sorted list of available airports (by three-character code)  
create a GUI  
use the list of airport codes provided by your new Graph.getAirportCodes() to populate both ComboBoxes  
implement a callback function to find the shortest flight between the selected airports.  Display an error message in the TextCtrl if departure airport matches the destination.  
show the result of your search in the shown wx.TextCtrl()  -- only if no input error occured.  
make sure that a new selection of either airport erases the text field.  
make the "reset view"-button move the app to the center of the screen and resize to half screen width and half screen height.
allow selection and copy from the text  field.  Prevent the user from changing that text other than through a search.  
add a menu that presents a simple About dialog and a Quit feature.  
## Deliverables:
Full documentation including the problem statement, an explanation of your algorithms (not the Graph, just the GUI), screenshots of various states of the program (with explanation!).  
All code and the database file needed to execute your code.