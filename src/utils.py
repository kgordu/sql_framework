from os.path import dirname, join, abspath

#Merge the given directory with the given file path
def get_path(folder_name, file_name=None):
    current_path = dirname(abspath(__file__))
    project_path = dirname(current_path)
    if file_name:
        full_path = join(project_path, folder_name, file_name)
    else:
        full_path = join(project_path, folder_name)
    return full_path
