import pandas as pd

file_path = 'books-en.csv'
books_data = pd.read_csv(file_path, delimiter=';', encoding='latin1')

long_titles_count = (books_data['Book-Title'].str.len() > 30).sum()
print(f"Количество записей с названием длиннее 30 символов: {long_titles_count}")

author_search = input("Введите имя автора для поиска: ")
search_results = books_data[books_data['Book-Author'].str.contains(author_search, case=False, na=False)].head(5)
print("Результаты поиска:")
print(search_results[['Book-Author', 'Book-Title', 'Year-Of-Publication']])

bib_references = books_data.sample(20).apply(
    lambda row: f"{row['Book-Author']}. {row['Book-Title']} - {row['Year-Of-Publication']}", axis=1
)
output_file = 'bibliographic_references.txt'

with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(f"{i + 1}. {ref}\n" for i, ref in enumerate(bib_references))

print(f"Библиографические ссылки сохранены в файл {output_file}")
