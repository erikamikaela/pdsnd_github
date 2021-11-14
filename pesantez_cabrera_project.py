#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


CITY_DATA = { 'Chicago': 'C:\\Users\\UserAdmin\\Desktop\\bikeshare-2\\chicago.csv',
              'New York': 'C:\\Users\\UserAdmin\\Desktop\\bikeshare-2\\new_york_city.csv',
              'Washington': 'C:\\Users\\UserAdmin\\Desktop\\bikeshare-2\\washington.csv'}

def load_data(city, month,day):
    '''
    It takes the city, month and day specified by the user
    Returns:
    The data frame filtered by city, month and day
    '''

    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df =  df[df['month']== month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        df = df[df['day_of_week']==days.index(day)]

    
    return df

cities=['Chicago', 'New York','Washington']
list2=['month', 'day', 'not at all']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while True:
        try: 
            city_=input('Would you like to see data for Chicago, New York, or Washington? ')
            cities.index(city_) #consistency check
            break
        except:
            print('\n Insert a valid name please!')
            
while True:
        try: 
            question= input('Would you like to filter the data by month, day, or not at all? ')
            list2.index(question)#consistency check
            break
        except:
            print('\n Insert a valid answer please!')

if question=='month':
    while True:
        try: 
            month_= input('Which month -january, february, march, april, may or june? ')
            months.index(month_)
            pp=load_data(city_, month_, 'all')
            break
        except:
            print('\n Insert a valid month please!')    
            
                      
if question=='day':
    while True:
        try: 
            day_=input('Which day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ')
            days.index(day_)
            pp=load_data(city_, 'all',day_)
            break
        except:
            print('\n Insert a valid day please!')             
            

if question =='not at all':
    pp=load_data(city_, 'all', 'all')
    

No_answer=['No','no', 'NO']    

q2=input('Do you want to see the raw date? ')

if q2 in ['Yes','yes', 'YES']:
    print(pp.head(5))

i=5
while True:
       try: 
            q3=input('Would you like to see 5 more rows of the data? ')
            No_answer.index(q3)
            break
       
       except:     
            print(pp.iloc[i:i+5,])
            i=i+5
    
#popular times of travel

print('\n Check out the results of your search. \n\n The most common month for a trip is {}'.format(pp['month'].mode()[0]))
print('\n The most common day of week for a trip is {}'.format(pp['day_of_week'].mode()[0]))
print('\n The most common hour of day for a trip is {}'.format(pp['hour'].mode()[0]))

#popular stations and trip
print('\n The most common start station is {}'. format(pp['Start Station'].mode()[0]))
print('\n The most common end station is {}'. format(pp['End Station'].mode()[0]))

start_end=pp['Start Station'] + " -- " + pp['End Station']                                           
print('\n The most common trip from start to end stations is {}'.format(start_end.mode()[0]))

#trip duration
print('\n The total travel time is {}'.format(pp['Trip Duration'].sum()))
print('\n The average travel time is {}'.format(pp['Trip Duration'].mean()))


#user info
#only available for NY nd Chicago

if city_ in ['New York','Chicago']:
    print('\n The user types are  \n {} '.format(pp['User Type'].value_counts()))
    print('\n Users by gender \n {} '.format(pp['Gender'].value_counts()))
    
    a=int(pp['Birth Year'].max())
    b=int(pp['Birth Year'].min())
    c=int(pp['Birth Year'].mode()[0]) 
    
    print('\n The youngest user was born in {} \n \n The oldest user was born in {} \n \n The most common year of birth is {}'.format(a,b,c))
    
    
    
    


# In[ ]:




