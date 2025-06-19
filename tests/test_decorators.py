import os
import tempfile
import pytest
from decorators import log

def test_log_success_to_console(capsys):
    """Тест успешного логирования в консоль"""

    @log()
    def add(a: int, b: int) -> int:
        return a + b

    assert add(2, 3) == 5
    captured = capsys.readouterr()
    assert "INFO" in captured.out
    assert "add" in captured.out
    assert "Args: (2, 3)" in captured.out


def test_log_error_to_file():
    """Тест логирования ошибок в файл"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.close()

        @log(filename=tmp.name)
        def fail_func():
            raise ValueError("Test error")

        try:
            fail_func()
        except ValueError:
            pass

        with open(tmp.name, "r") as f:
            content = f.read()
            assert "ERROR" in content
            assert "fail_func" in content
            assert "ValueError" in content

        os.unlink(tmp.name)


def test_log_disabled_levels(capsys):
    """Тест отключения уровней логирования"""

    @log(log_errors=False, log_success=False)
    def no_log_func():
        return 42

    assert no_log_func() == 42
    captured = capsys.readouterr()
    assert captured.out == ""