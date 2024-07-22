import os

#Merge the given directory with the given file path
def get_path(folder_name, file_name=None):
    current_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.dirname(current_path)
    if file_name:
        full_path = os.path.join(project_path, folder_name, file_name)
    else:
        full_path = os.path.join(project_path, folder_name)
    return full_path
