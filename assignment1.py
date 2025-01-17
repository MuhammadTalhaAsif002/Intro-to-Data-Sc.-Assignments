# -*- coding: utf-8 -*-
"""22l-7510B.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AK4frIVtBMz93PyP_XXhJ7CR9ipCLI8i
"""

#1.1number of lines
def NumOfLines(filename):
  with open('Text_File.txt','r')as file:
    r=file.readlines()
    count=len(r)
    return count

count = NumOfLines('Text_File.txt')
print("Number of Lines are ", count)

#1.2number of words
def NumOfwords(filename):
  with open('Text_File.txt','r')as file:
    r=file.read()
    words=r.split()
    count=0
    for word in words:
      count+=1
    return count

count = NumOfwords('Text_File.txt')
print("Number of words are ", count)

#2 Stopwords and their count
from nltk.corpus import stopwords
import nltk
import pandas as pd

nltk.download('stopwords')

def create_df(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        stop_words = set(stopwords.words('english'))
        count = 0
        for word in words:
            if word.lower() in stop_words:
                count += 1
        return count


stopword_count = create_df('Text_File.txt')

stop_words = list(set(stopwords.words('english')))
word_counts = [stop_words.count(word) for word in stop_words]

df = pd.DataFrame({'Stop Word': stop_words, 'Count': word_counts})

print(df)

#3 all content excluding stopwords
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

def remove_stopwords(input_text):
    stop_words = set(stopwords.words('english'))
    words = input_text.split()
    for word in words:
            if word.lower() not in stop_words:
               filtered_words=word

    return ' '.join(filtered_words)

def main(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    text_without_stopwords = remove_stopwords(text)

    with open(output_file, 'w') as file:
        file.write(text_without_stopwords)

main('Text_File.txt', 'RollnumberWS.txt')


print('Stopwords removed and saved to {RollnumberWS.txt}')

#4 words greater than 5
def words_greater_than_length_in_file(file_path, length):

        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            result = [word for word in words if len(word) > length]
            return result



file_path = 'Text_File.txt'
length = 5
long_words = words_greater_than_length_in_file(file_path, length)
df=pd.DataFrame(long_words)
df

#5 words ending at y
def count_words_ending_with_y(file_path):

        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            count = 0

            for word in words:
                if word.endswith('y'):
                    count += 1
            return count

file_path = 'Text_File.txt'
word_count = count_words_ending_with_y(file_path)
print(f"Number of words ending with 'y': {word_count}")

def count_lowercase_letters(file_path):

        with open(file_path, 'r') as file:
            text = file.read()
            lowercase_count = sum(1 for char in text if char.islower())
            print(f"Count of lowercase letters in the file: {lowercase_count}")



count_lowercase_letters('Text_File.txt' )

def replace_the_with_thee(input_text):

    modified_text = input_text.replace("the", "thee")

    return modified_text

modified_text = replace_the_with_thee('Text_File.txt')

def ZICount_from_file(file_path):

        with open(file_path, 'r') as file:
            text = file.read()

            lower_text = text.lower()

            count_z = lower_text.count('z')
            count_i = lower_text.count('i')

            count_z_upper = lower_text.count('Z')
            count_i_upper = lower_text.count('I')


            total_count_zi = count_z + count_i + count_z_upper + count_i_upper


            print(f"I or i : {count_i + count_i_upper}")
            print(f"Z or z : {count_z + count_z_upper}")


file_path = 'Text_File.txt'
ZICount_from_file(file_path)

def display_content_in_ascending_order(file_path):

        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = {}

            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

            sorted_words = sorted(word_count.items(), key=lambda x: x[1])

            sorted_words = [word[0] for word in sorted_words]
            sorted_text = ' '.join(sorted_words)
            print(sorted_text)



display_content_in_ascending_order('Text_File.txt' )

def alter_Upper_from_file(file_path):

        with open(file_path, 'r') as file:
            lines = file.readlines()
            altered_lines = []

            for i, line in enumerate(lines):
                if i % 2 == 0:
                    altered_lines.append(line.lower())
                else:
                    altered_lines.append(line.upper())

            altered_text = ''.join(altered_lines)
            print(altered_text)

alter_Upper_from_file('Text_File.txt' )

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_number(self):
        return self.account_number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def print_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0.0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_interest_rate(self):
        return self.interest_rate

    def post_interest(self):
        interest_earned = self.balance * (self.interest_rate / 100)
        self.balance += interest_earned

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            if amount <= 1000:
                self.balance -= amount
            else:
                print("Withdrawal limit exceeded for a savings account.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def print_account_info(self):
        print("Savings Account Information:")
        super().print_account_info()
        print(f"Interest Rate: {self.interest_rate:.2f}%")

# Example usage:
# Create a savings account and perform operations
savings_account = SavingsAccount(12345, 1000.0, 2.5)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.set_interest_rate(3.0)
savings_account.post_interest()
savings_account.print_account_info()

import numpy as np

# Create a 10x10 NumPy array with random integer values between 1 and 100
random_array = np.random.randint(1, 101, size=(10, 10))


sum_of_elements = np.sum(random_array)


mean_value = np.mean(random_array)

std_deviation = np.std(random_array)

max_value = np.max(random_array)
max_index = np.unravel_index(np.argmax(random_array), random_array.shape)

min_value = np.min(random_array)
min_index = np.unravel_index(np.argmin(random_array), random_array.shape)


print("Sum of all elements:", sum_of_elements)
print("Mean value of elements:", mean_value)
print("Standard deviation of elements:", std_deviation)
print("Maximum value in the array:", max_value)
print("Index of maximum value:", max_index)
print("Minimum value in the array:", min_value)
print("Index of minimum value:", min_index)

import pandas as pd

# Load the countries.csv dataset into a DataFrame
countries_df = pd.read_csv('countries.csv')

# 1. Number of countries in the dataframe
num_countries = len(countries_df)

# 2. List of continents
continents = countries_df['Continent'].unique().tolist()

# 3. Total population of all countries
total_population = countries_df['Population'].sum()

# 4. Overall life expectancy (corrected column name)
overall_life_expectancy = countries_df['Life Expectancy'].mean()

# 5. DataFrame with 10 countries with the highest population
top_10_countries = countries_df.nlargest(10, 'Population')

# 6. Add a new column for GDP (Population * GDP per Capita)
countries_df['GDP'] = countries_df['Population'] * countries_df['GDP(per capita)']

# Print the results
print("1. Number of countries:", num_countries)
print("2. List of continents:", continents)
print("3. Total population of all countries:", total_population)
print("4. Overall life expectancy:", overall_life_expectancy)
print("5. DataFrame with 10 countries with the highest population:")
print(top_10_countries)
print("6. Updated DataFrame with GDP column:")
print(countries_df[['Country', 'GDP']])