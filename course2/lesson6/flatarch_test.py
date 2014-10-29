import unittest
import flatarch
import zipfile
import os
import shutil

class TestFlatarch(unittest.TestCase):
    """Testing the functionality of the flatarch function"""
    
    def setUp(self):
        #self.path = r"v:\workspace\Archives\src\archive_me"
        self.path = "archive_me"
        
        self.zip_filename = "test_flatzip.zip"
        self.exclude_dir = os.path.join(self.path, "exclude_me")
        
        os.mkdir(self.path)
        os.mkdir(self.exclude_dir)
        
        self.file_names = ["file1", "file2"]
        for fn in self.file_names:
            f = open(os.path.join(self.path, fn), "w")
            f.close()
        
    def test_archiving_excluding_dirs(self):
        """Tests a flat zip archiving function excluding directories"""
        source = self.path
        zipfile_name = self.zip_filename
        
        flatarch.flatarch(source,zipfile_name)
        
        zf = zipfile.ZipFile(zipfile_name, "r")
        files_in_archive = zf.namelist()
        zf.close()
        
        observed = set([os.path.basename(f) for f in files_in_archive])
        expected = set(self.file_names)

        self.assertEqual(observed, expected)
    
    def tearDown(self):
        os.remove(self.zip_filename)
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass

if __name__ == "__main__":
    unittest.main()