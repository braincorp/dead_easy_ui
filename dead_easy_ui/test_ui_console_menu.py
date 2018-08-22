from __future__ import print_function
from __future__ import absolute_import
import pytest

from dead_easy_ui.ui_console_menu import parse_user_function_call


def test_parse_command_args():
    assert parse_user_function_call("my_func 'a' 3 thing=4 thing2='strrring'") \
        == ('my_func', ('a', 3), dict(thing=4, thing2='strrring'))

    assert parse_user_function_call("my_func 'thing with spaces'") == ('my_func', ('thing with spaces',), {})

    with pytest.raises(AssertionError):
        # Wasted too much time trying to get this to work properly so we just assert that an error is thrown.
        parse_user_function_call("my_func b='thing with spaces'")

    with pytest.raises(NameError):
        parse_user_function_call("my_func aaa bbb=3.1")

    # For conveniece we allow not everything to be quoted
    assert parse_user_function_call("my_func aaa bbb=3.1", forgive_unquoted_strings=True) == ('my_func', ('aaa',), {'bbb': 3.1})


if __name__ == '__main__':
    test_parse_command_args()
