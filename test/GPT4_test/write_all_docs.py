import openpyxl
from openpyxl import load_workbook

# from DocDoc_with_wic_globalview import write
def write(prompt:str, title:str):
    """this function is to stimulate the write function in DocDoc_with_wic_globalview.py, which can generate a text based on the prompt"""
    print(f"I am writing {title}")
    with open(f"{title}.md", "w") as f:
        f.write(prompt)
    file_path:str = f"{title}.md"
    print(f"{title} has been written to {file_path}")
    return file_path


class ExcelHandler:
    def __init__(self, filename):
        self.filename = filename
        try:
            # Try to load an existing workbook
            self.wb = load_workbook(self.filename)
            self.ws = self.wb.active
        except FileNotFoundError:
            # If the file doesn't exist, create a new one
            self.wb = openpyxl.Workbook()
            self.ws = self.wb.active
            self.ws.append(["id", "Title", "Title_ch", "Category", "Type", "Strategy", "Prompt", "Plan", "Text"])  # Add headers if it's a new file

    def __iter__(self):
        for row in self.ws.iter_rows(min_row=2, values_only=True):
            yield dict(zip([cell.value for cell in self.ws[1]], row))
    
    def update_row(self, row_num, col_name, value):
        col_idx = [cell.value for cell in self.ws[1]].index(col_name) + 1
        self.ws.cell(row=row_num, column=col_idx, value=value)

    def save(self):
        self.wb.save(self.filename)

def make_prompt(title:str, category:str) -> str:
    prompt:str = f"""I want to write one {category}, titled "{title}" Could you generate the table of contents for the opinion article and provide a detailed explanation of the dependencies between the items in the table of contents?"""
    return prompt

# - test for make_prompt" 
# print(make_prompt("AAa", "BBB"))

xlsx_file_path:str =  "/root/AI4E/lzd/DocDoc/test/GPT4_test/output_refined.xlsx"
excel = ExcelHandler(xlsx_file_path)

# Iterate through each row in the Excel file
for row_num, row in enumerate(excel, start=2):
    title: str = row['Title']
    category: str = row['Category']
    prompt: str = make_prompt(title, category)
    file_path: str = write(prompt, title)
    excel.update_row(row_num, 'Text', file_path)

# Save the updated Excel file
excel.save()

print("completed successfully!")