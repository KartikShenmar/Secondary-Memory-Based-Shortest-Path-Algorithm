# Secondary-Memory-Based-Shortest-Path-Algorithm
CODE HAS BEEN WRITTEN IN PYTHON AND IT INVOLVES THE USE OF ARRAYS FOR WHICH IT IS RECOMMENDED TO INSTALL NUMPY BEFOREHAND TO EXECUTE THE CODE SUCCESSFULLY. NUMPY MODULE CAN BE INSTALLED USING THE FOLLOWING COMMAND : 

pip install numpy
	or
pip3 install numpy

MAIN FILE NAMES HAVE BEEN CREATED IN THE FORM OF CELL-IDs.
OVERFLOW FILE NAMES ARE IN THE FORM :  <Main File Name>ov<Overflow No.>.txt

AFTER RUNNING THE PROGRAM, ALL THE NECESSARY FILES WILL GET CREATED in the specidfied format below:

1 <x coordinate, y coordinate>

2 <x coordinate, y coordinate>

3 <x coordinate, y coordinate>

4 <x coordinate, y coordinate>

## <special character indicating start of edges within cell>

3 1 <edge length>

2 3 <edge length>

2 4 <edge length>

4 3 <edge length>

** <special character indicating start of boundary information>

5 <x coordinate, y coordinate>

6 <x coordinate, y coordinate>

?? <special character indicating start of overflow page> FIle name of over disk block

<Contents of Overflow disk block>

?? File name of the main disk block

7 <x coordinate, y coordinate>

%% <special character indicating start of boundary edges information>

1 7 <edge length>

7 3 <edge length>

2 5 <edge length>

6 4 <edge length>



PROGRAM WILL RUN FOR SINGLE TIME IN WHICH FIRST IT WILL ASK FOR VALUE OF k AND B, AFTER WHICH IT WILL ASK FOR SOURCE AND DESTINATION NODES OF SIMPLE DJIKSTRA ALGORITHM, AFTER WHICH FINALLY RESULT OF SHORTEST DISTANCE BETWEEN SOURCE AND DESTINATION NODES WILL BE DISPLAYED ALONG WITH SHORTEST PATH.

SIMILARLY, APPROPRIATE DATA FOR PARTITIONED DJIKSTRA ALGORITHM WILL BE ASKED AFTER WHICH SHORTEST DISTANCE ALONG WITH SHORTEST PATH WILL BE DISPLAYED AT THE END. 
