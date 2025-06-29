from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор который автоматически логирует начало и конец выполнения функции, а также ее результаты
    или возникшие ошибки. Декоратор должен принимать необязательный аргумент filename, который определяет,
    куда будут записываться логи (в файл или в консоль):
    Если filename задан, логи записываются в указанный файл.
    Если filename не задан, логи выводятся в консоль.
    """

    def decorator(func: Callable) -> Callable:

        def write_log(message: str, filename: Optional[str] = None) -> None:
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(message)
            else:
                print(message)

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} - OK - {result}\n"
                write_log(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__} - {type(e)} - args: {args}, kwargs: {kwargs}\n"
                write_log(message, filename)
                raise

        return wrapper

    return decorator


# Example usage
# @log()
# def foo(x, y):
#     return x + y
#
#
# foo(3, "2")
