import os

folders = ['Folder1', 'Folder2']
file_contents = [
    'Testing python script using Azure Pipelines.',
    'Testing python script with Azure DevOps Pipelines.'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True) os.path.join(folder, exist_ok=True)
    for i, content in enumerate(file_contents, start=1):
        file_name = f'{folder}/file{i}.txt'
        with open(file_name, 'w') as file:
            file.write(content)
        print(f'Created {file_name}')
