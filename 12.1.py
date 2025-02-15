import re


def clean_html(input_filename, output_filename="cleaned.txt"):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        text = infile.read()

    cleaned_text = re.sub(r'<[^>]+>', '', text)
    cleaned_text = '\n'.join([line for line in cleaned_text.split('\n') if line.strip()])

    with open(output_filename, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_text)


#clean_html(r'C:\Users\Igor\OneDrive\Рабочий стол\draft.html', r'C:\Users\Igor\OneDrive\Рабочий стол\cleaned.txt')
