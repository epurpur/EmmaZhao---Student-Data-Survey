# EmmaZhao---Student-Data-Survey


This script is meant to take in a dataset of peer survey data and pivot it to be structured differently.

--------

EmmaZhao-PeerSurveyPivot.py is python script
EmmaZhao1.csv is example class dataset

--------

At the beginning, the data is structured as...
    - groups contain 1-5 members
    - group members answer questions regarding themselves and their other group members
        - each group member answers 8 questions about each member in their group (including themselves)

Data is restructured so that each students' responses about themselves are linked to themselves and the other
group members' responses about that student are linked to that student

--------
The basic process of the script is as follows...
    - split up each group by section and group letter (1a, 1b, etc)
    - make a list of group members
    - Loop over each group member.
        - Use python's pandas library to create a series (a 1-Dimensional row of data) with the desired data for each group member
    - Assemble those into a pandas Dataframe (a 2-Dimensional tabular data structure)
    - Stick all dataframes together into one big dataframe and save it as a .csv file

--------

A few caveats about the data...

There must be consistent naming amongst the students in each group. In each group compare column 1 (name_1) to 
the names in columns AR-AV (Mem1 - Mem5). These names must be the same. For example, 'Dave' and 'David' will
result in errors. I suggest changing the name_1 column to match whatever is in the Mem1-Mem5 columns. This was
particlarly a problem for international students who choose an english name.

It appears that all groups are intended to have 5 members, but some group member data is missing. In this event,
that students' responses will be filled with the value 'n/a'.
