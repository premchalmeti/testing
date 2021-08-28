# mock excel parser

from unittest.mock import Mock

# parser = ExcelParser()
# parser.parse_and_load_excel("admin.xlsx")
# parser.prepare_mapping()
# parser.output_mapping(echo=False)

parser = Mock()

# do all the functionality
parser.parse_and_load_excel('admin.xlsx')
parser.prepare_mapping()
parser.output_mapping(echo=False)

# then check if the mock objects is handled correctly
# parser.parse_and_load_excel.assert_called()
# parser.parse_and_load_excel.assert_called_once()
parser.parse_and_load_excel.assert_called_with('admin.xlsx')


# parser.prepare_mapping.assert_called()
parser.prepare_mapping.assert_called_once()

# parser.output_mapping.assert_called()
# parser.output_mapping.assert_called_once()
parser.output_mapping.assert_called_with(echo=False)

parser.parse_and_load_excel.call_args
parser.parse_and_load_excel.call_args_list
parser.parse_and_load_excel.call_count
parser.parse_and_load_excel.method_calls

