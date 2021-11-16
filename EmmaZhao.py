
import pandas as pd

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


dfs = []

for section in sections:
    for group in groups:
        
        current_df = create_df(section, group)
    
        dfs.append(current_df)
   
        
test_df = dfs[0] 
#make a list of group members
group_members = test_df.iloc[1][-5:].tolist()
section = test_df['Section'].unique()[0] 
group = test_df['Group'].unique()[0]


#group member 1
current_row = test_df.loc[test_df['name_1'] == group_members[0]]
member1 = [ group_members[0], section, group, current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[1]]
member2 = [ group_members[1], current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[2]]
member3 = [ group_members[2], current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[3]]
member4 = [ group_members[3], current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[4]]
member5 = [ group_members[4], current_row['mem1_1'].values[0], current_row['mem1_2'].values[0], current_row['mem1_3'].values[0], current_row['mem1_4'].values[0], current_row['mem1_5'].values[0], current_row['mem1_6'].values[0], current_row['mem1_7'].values[0], current_row['mem1_8'].values[0] ]

member1_series = member1 + member2 + member3 + member4 + member5


#group member 2
current_row = test_df.loc[test_df['name_1'] == group_members[1]]
member1 = [ group_members[1], section, group, current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[0]]
member2 = [ group_members[0], current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[2]]
member3 = [ group_members[2], current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[3]]
member4 = [ group_members[3], current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[4]]
member5 = [ group_members[4], current_row['mem2_1'].values[0], current_row['mem2_2'].values[0], current_row['mem2_3'].values[0], current_row['mem2_4'].values[0], current_row['mem2_5'].values[0], current_row['mem2_6'].values[0], current_row['mem2_7'].values[0], current_row['mem2_8'].values[0] ]

member2_series = member1 + member2 + member3 + member4 + member5


#group member 3
current_row = test_df.loc[test_df['name_1'] == group_members[2]]
member1 = [ group_members[2], section, group, current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[0]]
member2 = [ group_members[0], current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[1]]
member3 = [ group_members[1], current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]
 
current_row = test_df.loc[test_df['name_1'] == group_members[3]]
member4 = [ group_members[3], current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[4]]
member5 = [ group_members[4], current_row['mem3_1'].values[0], current_row['mem3_2'].values[0], current_row['mem3_3'].values[0], current_row['mem3_4'].values[0], current_row['mem3_5'].values[0], current_row['mem3_6'].values[0], current_row['mem3_7'].values[0], current_row['mem3_8'].values[0] ]

member3_series = member1 + member2 + member3 + member4 + member5


#group member 4
current_row = test_df.loc[test_df['name_1'] == group_members[3]]
member1 = [ group_members[3], section, group, current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[0]]
member2 = [ group_members[0], section, group, current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[1]]
member3 = [ group_members[1], section, group, current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[2]]
member4 = [ group_members[2], section, group, current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[4]]
member5 = [ group_members[4], section, group, current_row['mem4_1'].values[0], current_row['mem4_2'].values[0], current_row['mem4_3'].values[0], current_row['mem4_4'].values[0], current_row['mem4_5'].values[0], current_row['mem4_6'].values[0], current_row['mem4_7'].values[0], current_row['mem4_8'].values[0] ]

member4_series = member1 + member2 + member3 + member4 + member5


#group member 5
current_row = test_df.loc[test_df['name_1'] == group_members[4]]
member1 = [ group_members[4], section, group, current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[0]]
member2 = [ group_members[0], current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[1]]
member3 = [ group_members[1], current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[2]]
member4 = [ group_members[2], current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]

current_row = test_df.loc[test_df['name_1'] == group_members[4]]
member5 = [ group_members[4], current_row['mem5_1'].values[0], current_row['mem5_2'].values[0], current_row['mem5_3'].values[0], current_row['mem5_4'].values[0], current_row['mem5_5'].values[0], current_row['mem5_6'].values[0], current_row['mem4_7'].values[0], current_row['mem5_8'].values[0] ]

member5_series = member1 + member2 + member3 + member4 + member5


# combine these into a dataframe for the whole group
