import io
from contextlib import redirect_stdout

# def a():
#     return 1
#
# b = a()
# c = a
#
# d = c()


def get_print_output(tested_func):

    memory_buffer = io.StringIO()

    with redirect_stdout(memory_buffer):

        tested_func()

        return memory_buffer.getvalue()

