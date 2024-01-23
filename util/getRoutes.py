import os
import importlib.util
import util.badModCheck

def import_files_from_folder(folder_path):
    imported_files = {}
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):  # Adjust the file extension if needed
                module_path = os.path.join(root, file_name)
                module_name = os.path.splitext(os.path.relpath(module_path, folder_path))[0].replace(os.sep, "/")
                module_spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(module_spec)
                module_spec.loader.exec_module(module)
                if module_name.endswith("index"):
                    module_name = module_name[:-len("index")]
                imported_files[module_name] = module
    util.badModCheck.checkForBadModuleNames(imported_files)
    return imported_files
