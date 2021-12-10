"""
This script is meant to take in a dataset of peer survey data and pivot it to be structured differently.

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



"""



import pandas as pd

#read dataset
df = pd.read_csv(r'/Users/ep9k/Desktop/peereval.csv')

#get unique sections. Sorted into numerical order
sections = df['Section'].unique()
sections.sort()

#get unique groups. Sorted into numerical order
groups = df['GrpNo'].unique()
groups.sort()



def create_df(section, group):
    """ Takes section and group info and creates dataframe from that for each section/group combo"""

    #first make subset for section    
    temp_df = df.loc[df['Section'] == section]
    #then make subset for group in section
    final_df = temp_df.loc[temp_df['GrpNo'] == group]
    
    return final_df



#dfs will be list of dataframes. Each dataframe is each section/group combination for the class (ie: Section 1 Group A, etc...)
dfs = []

for section in sections:
    for group in groups:
        current_df = create_df(section, group)
        dfs.append(current_df)


#this holds all final pivoted dataframes after looping over them
dataframe_holder = []


#iterate over each dataframe and pivot data
#This will consider dataframes of any number of group members (0 - 5)
for dataframe in dfs:
    
    #if there are at least 1 member in a group  (some groups are empty, why???)
    if len(dataframe.index) > 1:
        
        #make a list of group members, section, and group
        group_members = dataframe.iloc[1][-5:].tolist()
        section = dataframe['Section'].unique()[0] 
        group = dataframe['GrpNo'].unique()[0] 
    
    
        #group member 1
        current_row = dataframe.loc[dataframe['ID'] == group_members[0]]
        try:
            member1 = [ f'{group_members[0]} on {group_members[0]} ->', section, group, current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
        except:
            member1 = [ f'{group_members[0]} on {group_members[0]} ->', section, group, 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[1]]
        try:
            member2 = [ f'{group_members[1]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
        except:
            member2 = [ f'{group_members[1]} on {group_members[0]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[2]]
        try:
            member3 = [ f'{group_members[2]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
        except:
            member3 = [ f'{group_members[2]} on {group_members[0]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[3]]
        try:
            member4 = [ f'{group_members[3]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
        except:
            member4 = [ f'{group_members[3]} on {group_members[0]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[4]]
        try:
            member5 = [ f'{group_members[4]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
        except:
            member5 = [ f'{group_members[4]} on {group_members[0]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        #combine all items in members list
        member1_series = member1 + member2 + member3 + member4 + member5
        
        
        #group member 2
        current_row = dataframe.loc[dataframe['ID'] == group_members[1]]
        try:
            member1 = [ f'{group_members[1]} on {group_members[1]} ->', section, group, current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
        except:
            member1 = [ f'{group_members[1]} on {group_members[1]} ->', section, group, 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[0]]
        try:
            member2 = [ f'{group_members[0]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
        except:
            member2 = [ f'{group_members[0]} on {group_members[1]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[2]]
        try:
            member3 = [ f'{group_members[2]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
        except:
            member3 = [ f'{group_members[2]} on {group_members[1]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[3]]
        try:
            member4 = [ f'{group_members[3]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
        except:
            member4 = [ f'{group_members[3]} on {group_members[1]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[4]]
        try:
            member5 = [ f'{group_members[4]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
        except:
            member5 = [ f'{group_members[4]} on {group_members[1]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        #combine all items in members list
        member2_series = member1 + member2 + member3 + member4 + member5
        
        
        #group member 3
        current_row = dataframe.loc[dataframe['ID'] == group_members[2]]
        try:
            member1 = [ f'{group_members[2]} on {group_members[2]} ->', section, group, current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
        except:
            member1 = [ f'{group_members[2]} on {group_members[2]} ->', section, group, 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[0]]
        try:
            member2 = [ f'{group_members[0]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
        except:
            member2 = [ f'{group_members[0]} on {group_members[2]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[1]]
        try:
            member3 = [ f'{group_members[1]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
        except:
            member3 = [ f'{group_members[1]} on {group_members[2]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[3]]
        try:
            member4 = [ f'{group_members[3]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
        except:
            member4 = [ f'{group_members[3]} on {group_members[2]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[4]]
        try:
            member5 = [ f'{group_members[4]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
        except:
            member5 = [ f'{group_members[4]} on {group_members[2]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        #combine all items in members list
        member3_series = member1 + member2 + member3 + member4 + member5
        
        
        #group member 4
        current_row = dataframe.loc[dataframe['ID'] == group_members[3]]
        try:
            member1 = [ f'{group_members[3]} on {group_members[3]} ->', section, group, current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
        except:
            member1 = [ f'{group_members[3]} on {group_members[3]} ->', section, group, 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[0]]
        try:
            member2 = [ f'{group_members[0]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
        except:
            member2 = [ f'{group_members[0]} on {group_members[3]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[1]]
        try:
            member3 = [ f'{group_members[1]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
        except:
            member3 = [ f'{group_members[1]} on {group_members[3]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[2]]
        try:
            member4 = [ f'{group_members[2]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
        except:
            member4 = [ f'{group_members[2]} on {group_members[3]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[4]]
        try:
            member5 = [ f'{group_members[4]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
        except:
            member5 = [ f'{group_members[4]} on {group_members[3]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        #combine all items in members list
        member4_series = member1 + member2 + member3 + member4 + member5
        
        
        #group member 5
        current_row = dataframe.loc[dataframe['ID'] == group_members[4]]
        try:
            member1 = [ f'{group_members[4]} on {group_members[4]} ->', section, group, current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem5_7'].values[0], current_row['mem5_8'].values[0] ]
        except:
            member1 = [ f'{group_members[4]} on {group_members[4]} ->', section, group, 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[0]]
        try:
            member2 = [ f'{group_members[0]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem5_7'].values[0], current_row['mem5_8'].values[0] ]
        except:
            member2 = [ f'{group_members[0]} on {group_members[4]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[1]]
        try:
            member3 = [ f'{group_members[1]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem5_7'].values[0], current_row['mem5_8'].values[0] ]
        except:
            member3 = [ f'{group_members[1]} on {group_members[4]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[2]]
        try:
            member4 = [ f'{group_members[2]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem5_7'].values[0], current_row['mem5_8'].values[0] ]
        except:
            member4 = [ f'{group_members[2]} on {group_members[4]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        current_row = dataframe.loc[dataframe['ID'] == group_members[3]]
        try:
            member5 = [ f'{group_members[3]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem5_7'].values[0], current_row['mem5_8'].values[0] ]
        except:
            member5 = [ f'{group_members[3]} on {group_members[4]} ->', 'n/a','n/a','n/a','n/a','n/a','n/a','n/a','n/a']
        
        #combine all items in members list
        member5_series = member1 + member2 + member3 + member4 + member5


        # combine these into a dataframe for the whole group
        final_df = pd.DataFrame([member1_series, member2_series, member3_series, member4_series, member5_series],
                                columns=['Name', 'Section', 'Group', 'mem1_1', 'mem1_2', 'mem1_3', 'mem1_4', 'mem1_5', 'mem1_6', 'mem1_7', 'mem1_8', 
                                         'Group Member', 'mem2_1', 'mem2_2', 'mem2_3', 'mem2_4', 'mem2_5', 'mem2_6', 'mem2_7', 'mem2_8', 
                                         'Group Member', 'mem3_1', 'mem3_2', 'mem3_3', 'mem3_4', 'mem3_5', 'mem3_6', 'mem3_7', 'mem3_8', 
                                         'Group Member', 'mem4_1', 'mem4_2', 'mem4_3', 'mem4_4', 'mem4_5', 'mem4_6', 'mem4_7', 'mem4_8',
                                         'Group_member', 'mem5_1', 'mem5_2', 'mem5_3', 'mem5_4', 'mem5_5', 'mem5_6', 'mem5_7', 'mem5_8'])
            
        #add dataframe to dataframe_holder which aggregates all dataframes 
        dataframe_holder.append(final_df)


#at the end concatenate all dataframes in dataframe_holder into one large dataframe
end_result = pd.concat(dataframe_holder)
    

    