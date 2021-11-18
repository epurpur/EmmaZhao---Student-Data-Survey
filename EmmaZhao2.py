import pandas as pd

#read dataset
df = pd.read_csv('/Users/ep9k/Desktop/EmmaZhao.csv')

# #drop unneeded columns
# columns_to_drop = ['Unnamed: 48','Unnamed: 49','Unnamed: 50','Unnamed: 51','Unnamed: 52','Unnamed: 53','Unnamed: 54','Unnamed: 55','Unnamed: 56','Unnamed: 57',
#  'Unnamed: 58','Unnamed: 59','Unnamed: 60','Unnamed: 61','Unnamed: 62','Unnamed: 63','Unnamed: 64','Unnamed: 65','Unnamed: 66','Unnamed: 67','Unnamed: 68','Unnamed: 69','Unnamed: 70','Unnamed: 71',
#  'Unnamed: 72','Unnamed: 73','Unnamed: 74','Unnamed: 75','Unnamed: 76','Unnamed: 77','Unnamed: 78','Unnamed: 79','Unnamed: 80','Unnamed: 81','Unnamed: 82','Unnamed: 83','Unnamed: 84','Unnamed: 85','Unnamed: 86',
#  'Unnamed: 87','Unnamed: 88','Unnamed: 89','Unnamed: 90','Unnamed: 91','Unnamed: 92','Unnamed: 93','Unnamed: 94','Unnamed: 95','Unnamed: 96','Unnamed: 97','Unnamed: 98','Unnamed: 99','Unnamed: 100','Unnamed: 101',
#  'Unnamed: 102','Unnamed: 103','Unnamed: 104','Unnamed: 105','Unnamed: 106','Unnamed: 107','Unnamed: 108','Unnamed: 109','Unnamed: 110','Unnamed: 111','Unnamed: 112','Unnamed: 113','Unnamed: 114',
#  'Unnamed: 115','Unnamed: 116','Unnamed: 117','Unnamed: 118','Unnamed: 119','Unnamed: 120','Unnamed: 121','Unnamed: 122','Unnamed: 123','Unnamed: 124']

# df.drop(columns_to_drop, inplace=True, axis=1)

#get unique sections
sections = df['Section'].unique()

#get unique groups
groups = df['Group'].unique()





def create_df(section, group):
    """ Takes section and group info and creates dataframe from that for each section/group combo"""

    #first make subset for section    
    temp_df = df.loc[df['Section'] == section]
    #then make subset for group in section
    final_df = temp_df.loc[temp_df['Group'] == group]
    
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
#I only consider a dataframe if it has either 4 or 5 members. Otherwise it is discarded
for dataframe in dfs:
    
    #if there are 5 members in a group
    if len(dataframe.index) == 5:
        
        #make a list of group members, section, and group
        group_members = dataframe.iloc[1][-5:].tolist()
        section = dataframe['Section'].unique()[0] 
        group = dataframe['Group'].unique()[0]  
        
        print(group_members, section, group)
        
        #PIVOT DATA. Rearrange columns into desired output
        
        #group member 1
        try:
            current_row = dataframe.loc[dataframe['name_1'] == group_members[0]]
            member1 = [ f'{group_members[0]} on {group_members[0]} ->', section, group, current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[1]]
            member2 = [ f'{group_members[1]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[2]]
            member3 = [ f'{group_members[2]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[3]]
            member4 = [ f'{group_members[3]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[4]]
            member5 = [ f'{group_members[4]} on {group_members[0]} ->', current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]
            
            member1_series = member1 + member2 + member3 + member4 + member5
            
            
            #group member 2
            current_row = dataframe.loc[dataframe['name_1'] == group_members[1]]
            member1 = [ f'{group_members[1]} on {group_members[1]} ->', section, group, current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[0]]
            member2 = [ f'{group_members[0]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[2]]
            member3 = [ f'{group_members[2]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[3]]
            member4 = [ f'{group_members[3]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[4]]
            member5 = [ f'{group_members[4]} on {group_members[1]} ->', current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]
            
            member2_series = member1 + member2 + member3 + member4 + member5
            
            
            #group member 3
            current_row = dataframe.loc[dataframe['name_1'] == group_members[2]]
            member1 = [ f'{group_members[2]} on {group_members[2]} ->', section, group, current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[0]]
            member2 = [ f'{group_members[0]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[1]]
            member3 = [ f'{group_members[1]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
             
            current_row = dataframe.loc[dataframe['name_1'] == group_members[3]]
            member4 = [ f'{group_members[3]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[4]]
            member5 = [ f'{group_members[4]} on {group_members[2]} ->', current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
            
            member3_series = member1 + member2 + member3 + member4 + member5
            
            
            #group member 4
            current_row = dataframe.loc[dataframe['name_1'] == group_members[3]]
            member1 = [ f'{group_members[3]} on {group_members[3]} ->', section, group, current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[0]]
            member2 = [ f'{group_members[0]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[1]]
            member3 = [ f'{group_members[1]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[2]]
            member4 = [ f'{group_members[2]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[4]]
            member5 = [ f'{group_members[4]} on {group_members[3]} ->', current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]
            
            member4_series = member1 + member2 + member3 + member4 + member5
            
            
            #group member 5
            current_row = dataframe.loc[dataframe['name_1'] == group_members[4]]
            member1 = [ f'{group_members[4]} on {group_members[4]} ->', section, group, current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[0]]
            member2 = [ f'{group_members[0]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[1]]
            member3 = [ f'{group_members[1]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[2]]
            member4 = [ f'{group_members[2]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]
            
            current_row = dataframe.loc[dataframe['name_1'] == group_members[4]]
            member5 = [ f'{group_members[3]} on {group_members[4]} ->', current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]
            
            member5_series = member1 + member2 + member3 + member4 + member5
            
            
            
            
            # combine these into a dataframe for the whole group
            final_df = pd.DataFrame([member1_series, member2_series, member3_series, member4_series, member5_series],
                                    columns=['Name', 'Section', 'Group', 'mem1_1', 'mem1_2', 'mem1_3', 'mem1_4', 'mem1_5', 'mem1_6', 'mem1_7', 'mem1_8', 
                                             'Group Member', 'mem2_1', 'mem2_2', 'mem2_3', 'mem2_4', 'mem2_5', 'mem2_6', 'mem2_7', 'mem2_8', 
                                             'Group Member', 'mem3_1', 'mem3_2', 'mem3_3', 'mem3_4', 'mem3_5', 'mem3_6', 'mem3_7', 'mem3_8', 
                                             'Group Member', 'mem4_1', 'mem4_2', 'mem4_3', 'mem4_4', 'mem4_5', 'mem4_6', 'mem4_7', 'mem4_8',
                                             'Group_member', 'mem5_1', 'mem5_2', 'mem5_3', 'mem5_4', 'mem5_5', 'mem5_6', 'mem5_7', 'mem5_8'])
    
            
            #add finalized dataframe to dataframe_holder
            dataframe_holder.append(final_df)
        
        #skip if there is error
        except:
            pass
        
        
    #skip those with length of 4 (for now)    
    elif len(dataframe.index) == 4:
        pass
        # #make a list of group members, section, and group
        # group_members = dataframe.iloc[1][-5:].tolist()
        # section = dataframe['Section'].unique()[0] 
        # group = dataframe['Group'].unique()[0]  
        
    #skip those with less than 4 group members
    elif len(dataframe.index) < 4:
        pass
        



#at the end of all of it, concatenate all dataframes in dataframe_holder into one large dataframe
end_result = pd.concat(dataframe_holder)
    

    