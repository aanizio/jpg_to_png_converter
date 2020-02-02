import unittest
from jpg_to_png_converter import is_jpg_file, jpg_to_png_path

class TestJpgToPngConverter(unittest.TestCase):
    def test_is_jpg_file_jpg_ext(self):
        ret = is_jpg_file("file.jpg")
        self.assertTrue(ret)

    def test_is_jpg_file_jpeg_ext(self):
        ret = is_jpg_file("file.jpeg")
        self.assertTrue(ret)

    def test_is_jpg_file_png_ext(self):
        ret = is_jpg_file("file.png")
        self.assertFalse(ret)

    def test_jpg_to_png_path(self):
        filename = "image.jpg"
        jpg_path = "path\\to\\image\\"
        png_path = "new\\path\\to\\image\\"
        ret = jpg_to_png_path(filename, jpg_path, png_path)
        self.assertEqual(ret, (jpg_path + filename, png_path + "image.png"))

if __name__ == "__main__":
    unittest.main()