file_path_elements = input().split('\\')
file_name_and_extension = file_path_elements[-1].split('.')
file_name = file_name_and_extension[0]
file_extension = file_name_and_extension[1]
print(f'File name: {file_name}')
print(f'File extension: {file_extension}')

