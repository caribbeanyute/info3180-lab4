import os
rootdir = os.getcwd()

def get_uploaded_images():
    included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
    imagename = []

    return ([fn for fn in os.listdir(rootdir + '/app/static/uploads')
              if any(fn.endswith(ext) for ext in included_extensions)])