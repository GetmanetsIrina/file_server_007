from mock import mock_open
from src import file_system


def test_create_file_success_flow(mocker):
    mocked_open = mock_open()
    mocker.patch('builtins.open', mocked_open, create=True)
    mocker.patch('src.utils.get_random_string').return_value = "test_file_name"

    file_system.create_file('test_content', 5)

    mocked_open.assert_called_with('test_file_name', 'w')
    mocked_open().write.assert_called_with('test_content')


def test_read_file_success_flow(mocker):
    mocked_open = mock_open()
    mocker.patch('builtins.open', mocked_open, create=True)

    mocked_open().read.return_value = 'test_file_content'

    return_value = file_system.read_file('test_file_name')

    mocked_open.assert_called_with('test_file_name', 'r')
    assert return_value == 'test_file_content'


def test_list_dir_success_flow(mocker):
    ls_mock = mocker.patch('os.listdir')
    ls_mock.return_value = ['abc']
    assert file_system.list_dir() == ['abc']


def test_change_dir_success_flow(mocker):
    mocker_cd_dir = mocker.patch('os.chdir')
    mocker_is_directory = mocker.patch('os.path.isdir')
    mocker_is_directory.return_value = True

    result = file_system.change_dir('some_existed_folder')

    mocker_cd_dir.assert_called_once()
    assert result == True


def test_change_dir_not_exist(mocker):
    mocker_cd_dir = mocker.patch('os.chdir')
    mocker_is_directory = mocker.patch('os.path.isdir')
    mocker_is_directory.return_value = False

    result = file_system.change_dir('some_non_existent_directory')

    mocker_cd_dir.assert_not_called()
    assert result == False


def test_get_metadata(mocker):
    mocker_os_stat = mocker.patch('os.stat')
    result = {"a": "aaa", "b": "bbb", "c": "ccc"}
    mocker_os_stat.return_value = result

    mocker_is_file_exist = mocker.patch('os.path.isfile')
    mocker_is_file_exist.return_value = True

    actual_result = file_system.get_file_metadata('some_existed_file')

    mocker_os_stat.assert_called_once()
    assert result == actual_result