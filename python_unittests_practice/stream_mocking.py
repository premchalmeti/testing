
def read_file(file_stream):
    file_data = file_stream.read()
    print(file_data)
    # will give error
    # file_data = file_stream.read()


# with open('notes.txt') as fd:
#     read_file(fd)


from unittest.mock import Mock

stream = Mock()

read_file(stream)

stream.read.assert_called_once()
