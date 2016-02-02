# ProjectHamster
PCFB project of Lotte and Wim

This script converts activity data from text file into a actogram plotted using Plotly. The original input files as provided contain time and date information for each pulse and the states of all sensors at that moment in groups of 8 bits that are displayed as a decimal number (0-255). This script first converts this into individual sensor states: 0 (inactive) or 1 (active).

All sensor activity over all applicable sensors can be aggregated for a user-defined time period (bin size). This is then plotted as a quantitativeve actogram in the form of a bar chart using the Plotly online environment. To use this, the user has to create an account at Plotly and use the provided API key:

	py.sign_in('<user name>', '<API key>')

Running the script will automatically generate an actogram.

The script requires user input to run:
	Enter the name of a text file containing your date. Input files should have the following space-delimited format:
	
		Year Month Day Hour Minutes Seconds Milliseconds <3-digit code> <3-digit code> <3-digit code> <3-digit code> <3-digit code> <3-digit code>
		
The user then has to input the range of sensors that should be processed (0-48). 

By default, events are grouped in 10 minute intervals. To use a different bin size, change the value of the following variable:

	BinSize=10

PLOTLY notes:
For the use of Plotly, it first needs to  be installed. This can be done using the following command in the terminal (With or without sudo):
	$ (sudo) pip install plotly
You probably have pip installed already, but it might be necessary to update it first:
	On OS X / Linux: pip install -U pip
	On Windows: python -m pip install -U pip

To make the plot, you need to be logged in on plotly.com while you run the program in the terminal.
In this script, Lottes username and API key are used, so the graph is only created when being logged in on that account. 
To check whether the script works completely you could contact or email Lotte or to make your own account and change the username and API key.
