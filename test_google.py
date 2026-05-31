from app.services.google_sheets import get_sheet

sheet = get_sheet()

data = sheet.get_all_records()

print(data)