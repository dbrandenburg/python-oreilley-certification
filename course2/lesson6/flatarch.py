import zipfile
import os
import glob

def flatarch(source,zipfile_name):
    """Creates a flat arhive including files only"""
    files = glob.glob(os.path.join(source, "*"))
    files_to_archive = []
    for file in files:
        if os.path.isfile(file):
            files_to_archive.append(file)
    zf = zipfile.ZipFile(zipfile_name, "w", zipfile.ZIP_DEFLATED)
    #try zf = zipfile.ZipFile(zipfile_name, "w")
    for fn_to_archive in files_to_archive:
        zf.write(fn_to_archive, os.path.basename(fn_to_archive))
        #try zf.write(fn_to_archive, os.path.basename(fn_to_archive))
    zf.close()