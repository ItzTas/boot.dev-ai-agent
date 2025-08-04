from webbrowser import get
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info


def test_get_files_info():
    print("Result for current directory:")
    print(get_files_info("calculator", "."))

    print("Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))

    print("Result for '/bin' directory")
    print(get_files_info("calculator", "/bin"))
    print("")

    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))
    print("")


def test_get_file_content():
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exits.py"))


if __name__ == "__main__":
    # test_get_files_info()
    test_get_file_content()
