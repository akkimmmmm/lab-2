import pandas as pd

file_path = 'books-en.csv'
books_data = pd.read_csv(file_path, delimiter=';', encoding='latin1')

unique_publishers = books_data['Publisher'].dropna().unique()
print("Перечень издательств без повторений:")
print(unique_publishers)

top_books = books_data.nlargest(20, 'Downloads')[['Book-Title', 'Downloads']]
print("\nСамые популярные 20 книг:")
print(top_books)
