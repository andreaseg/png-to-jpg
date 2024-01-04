import sys
import os
from PIL import Image
import zipfile

_debug = False

def traverse_files(rootFileName: str, delete_after_extract = False):
    for root, dirs, files in os.walk(rootFileName):
        for filename in files:
            filepath = os.path.join(root, filename)
            extension = filename.split('.')[-1]
            if (extension == 'zip'):
                if _debug:
                    print(f"Unzipping file {filepath}")
                zip_extract_target_dir = filepath.removesuffix('.zip')
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                     zip_ref.extractall(zip_extract_target_dir)
                traverse_files(zip_extract_target_dir, delete_after_extract = True)

            elif (extension == 'png'):
                if _debug:
                    print(f"Converting file {filepath}")
                Image.open(filepath).convert('RGB').save(f"{filepath.removesuffix('png')}jpg")
                if delete_after_extract:
                    if _debug:
                        print(f"Deleting file  {filepath}")
                    os.remove(filepath) 

            else:
                if _debug:
                    print(f"Skipping file {filepath}")
            

if __name__ == '__main__':

    _debug = True

    argpath = ' '.join(sys.argv[1:])
    if (argpath == ''):
       traverse_files('.')
    else:
        traverse_files(argpath)