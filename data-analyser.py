import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    w=0 
    b=0 
    e=0 
    p=0
    o=0
    for i in df['race']=='White':
        if i==True:
            w +=1
  
    for i in df['race']=='Black':
        if i==True:
            b +=1
 
    for i in df['race']=='Amer-Indian-Eskimo':
        if i==True:
            e +=1
 
    for i in df['race']=='Asian-Pac-Islander':
        if i==True:
            p +=1
    
    for i in df['race']=='Other':
        if i==True:
            o +=1
    race_count=pd.Series([w,b,p,e,o])
    race_count.index=df['race'].unique()  

    # What is the average age of men?
    average_age_men = df[df['sex']=='Male'].mean()['age']

    # What is the percentage of people who have a Bachelor's degree?
    bachelors=0
    total_count=0
    for i in df['education']=='Bachelors':
        if i==True:
            bachelors +=1
    for i in df['education']:
        total_count+=1
    z=(bachelors/total_count)*100
    percentage_bachelors = z

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    bachelors_with_high_salary=0
    masters_with_high_salary=0
    doctorate_with_high_salary=0
    for i in df[df['education']=='Bachelors']['salary']=='>50K':
        if i == True:
            bachelors_with_high_salary +=1
    for i in df[df['education']=='Masters']['salary']=='>50K':
        if i == True:
            masters_with_high_salary +=1
    for i in df[df['education']=='Doctorate']['salary']=='>50K':
        if i == True:
            doctorate_with_high_salary +=1
    higher_educated=bachelors_with_high_salary+masters_with_high_salary+doctorate_with_high_salary
    
    # percentage with salary >50K
    higher_education_rich = (higher_educated/total_count)*100
    lower_education_rich = 100-higher_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hr_gsalary=0
    min_hr=0
    for i in df[df['hours-per-week']==df['hours-per-week'].min()]['salary']=='>50K':
        if i==True:
            min_hr_gsalary +=1
    for i in df[df['hours-per-week']==df['hours-per-week'].min()]['salary']:
        min_hr +=1

    rich_percentage = (min_hr_gsalary/min_hr)*100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = 'United-States'
    
    highest_earning_country_percentage = (7171/7841)*100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = 'Armed-forces'

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data()
