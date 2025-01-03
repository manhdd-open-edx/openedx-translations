import os
import json

base_dir = os.path.expanduser('~/Documents/Code/dich/translations')

list_of_files = []

for root, dirs, files in os.walk(base_dir):
    if 'transifex_input.json' in files:
        if 'node_modules' not in root:
          path_parts = root.split('/')
          if len(path_parts) >= 7:
              folder_name = path_parts[7]
              list_of_files.append(folder_name)
print("Extracted Folder Names:", list_of_files)
for item in list_of_files:
    try:
        target_file_path = os.path.join(base_dir, item, 'src', 'i18n', 'messages', 'id.json')
        translated_file_path = os.path.join(base_dir, item, 'src', 'i18n', 'messages', 'vi.json')
        export_file_path = os.path.join(base_dir, item, 'src', 'i18n', 'messages', 'vi.json')

        with open(target_file_path, 'r') as file:
            target_file = json.load(file)

        with open(translated_file_path, 'r') as file:
            translated_file = json.load(file)

        missing_keys = [key for key in target_file if key not in translated_file]

        combined_file = translated_file.copy()
        for key in missing_keys:
            combined_file[key] = ""

        with open(export_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(combined_file, output_file, ensure_ascii=False, indent=4)

    except FileNotFoundError as e:
        target_file_path = os.path.join(base_dir, item, 'i18n', 'messages', 'id.json')
        translated_file_path = os.path.join(base_dir, item, 'i18n', 'messages', 'vi.json')
        export_file_path = os.path.join(base_dir, item, 'i18n', 'messages', 'vi.json')

        black_list = ['frontend-app-ora', 'frontend-app-publisher'];
        if item in black_list:
          continue

        with open(target_file_path, 'r') as file:
            target_file = json.load(file)

        with open(translated_file_path, 'r') as file:
            translated_file = json.load(file)

        missing_keys = [key for key in target_file if key not in translated_file]

        combined_file = translated_file.copy()
        for key in missing_keys:
            combined_file[key] = ""

        with open(export_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(combined_file, output_file, ensure_ascii=False, indent=2)

    except json.JSONDecodeError as e:
        print(f"JSON decoding error for folder '{item}': {e}")

    except Exception as e:
        print(f"An error occurred for folder '{item}': {e}")
