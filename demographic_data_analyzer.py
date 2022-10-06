import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.groupby('sex').age.mean()[1],1)

    # What is the percentage of people who have a Bachelor's degree?
    educationaldf = df['education']
    bachelors = educationaldf[educationaldf == 'Bachelors']
    total_edu = educationaldf.count()
    percentage_bachelors = round(bachelors.count() * 100 / total_edu, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    salarydf = df['salary']
    over50 = df[salarydf == '>50K']

    education_salary_df = df[(educationaldf == 'Bachelors') | (educationaldf == 'Masters') | (educationaldf == 'Doctorate')]
    noneducation_salary_df = df[(educationaldf != 'Bachelors') & (educationaldf != 'Masters') & (educationaldf != 'Doctorate')]

    # percentage with salary >50K
    higher_education_rich = round((education_salary_df['education'][salarydf == '>50K'].count() / education_salary_df['education'].count()) * 100, 1)
    lower_education_rich = round((noneducation_salary_df['education'][salarydf == '>50K'].count() / noneducation_salary_df['education'].count()) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df['hours-per-week'] == min_work_hours].index)
    rich_test = len(df.loc[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].index)
    rich_percentage = round(rich_test * 100 /num_min_workers, 1)

    # What country has the highest percentage of people that earn >50K?
    salary_counter = df.groupby('native-country')['salary'].count().to_frame()
    salary_rich = df.loc[df['salary'] == '>50K'].groupby('native-country')['salary'].count().to_frame()
    salary_perc = round(salary_rich['salary'] * 100 / salary_counter['salary'], 1) 
    highest_earning_country  = salary_perc.idxmax()
    highest_earning_country_percentage = salary_perc.max()
    print(highest_earning_country_percentage)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[df['native-country'] == 'India']['occupation'].value_counts().idxmax()

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
