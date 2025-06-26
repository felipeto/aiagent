# tests.py

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


class TestMain(unittest.TestCase):

    # def test_get_files_info_same_folder(self):
    #     print(get_files_info("calculator", "."))

    # def test_get_files_info_pkg(self):
    #     print(get_files_info("calculator", "pkg"))

    # def test_get_files_info_non_existent(self):
    #     try:
    #         get_files_info("calculator", "/bin")
    #     except Exception as e:
    #         print(str(e))
    #         self.assertEqual(str(e), 'Error: Cannot list "/bin" as it is outside the permitted working directory')

    # def test_get_files_info_non_outsise(self):
    #     try:
    #         get_files_info("calculator", "..")
    #     except Exception as e:
    #         print(str(e))
    #         self.assertEqual(str(e), 'Error: Cannot list ".." as it is outside the permitted working directory')

    # def test_get_file_content_root(self):
    #     file_content = get_file_content('calculator', 'main.py')
    #     print(file_content)
    #     self.assertTrue(file_content.startswith("# main.py"))

    # def test_get_file_content_inner(self):
    #     file_content = get_file_content('calculator', 'pkg/calculator.py')
    #     print(file_content)
    #     self.assertTrue(file_content.startswith("# calculator.py"))

    # def test_get_file_content_error(self):
    #     try:
    #         file_content = get_file_content('calculator', '/bin/cat')
    #         print(file_content)
    #     except Exception as e:
    #         error_message = str(e)
    #         print(error_message)
    #         self.assertEqual('Error: Cannot read "/bin/cat" as it is outside the permitted working directory', error_message)

    # def test_get_file_content_truncate(self):
    #     file_content = get_file_content('calculator', 'lorem.txt')
    #     print(file_content)
    #     self.assertTrue(file_content.endswith('truncated at 10000 characters]'))


    # def test_wite_file(self):
    #     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #     print(result)
    #     self.assertEqual(result, 'Successfully wrote to "calculator/lorem.txt" (28 characters written)')


    # def test_wite_file_subfolder(self):
    #     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #     print(result)
    #     self.assertEqual(result, 'Successfully wrote to "calculator/pkg/morelorem.txt" (26 characters written)')

    # def test_wite_file_error(self):
    #     try:
    #         result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #     except Exception as e:
    #         error_message = str(e)
    #         print(error_message)
    #         self.assertEqual(error_message, 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory')


    def test_run_py(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_run_py_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_run_py_tests(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_run_py_error(self):
        try:
            result = run_python_file("calculator", "../main.py")
        except Exception as e:
            print(str(e))

    def test_run_py_error_nonexistent(self):
        try:
            result = run_python_file("calculator", "nonexistent.py")
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    unittest.main()