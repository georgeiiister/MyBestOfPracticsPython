import string
import random

import tkinter as tk
import tkinter.messagebox as mb


class CountAsciiLettersError(Exception):
    pass


class NoneCountAsciiLettersError(CountAsciiLettersError):
    pass


class CountDigitsError(Exception):
    pass


class NoneCountDigitsError(CountDigitsError):
    pass


def get_password(count_digits, count_ascii_letters, case_sensitive=False) -> str | None:
    password = None

    if not count_ascii_letters:
        raise NoneCountAsciiLettersError

    if not count_digits:
        raise NoneCountDigitsError

    count_digits = int(count_digits)
    count_ascii_letters = int(count_ascii_letters)
    case_sensitive = bool(case_sensitive)

    string_digits = string.digits
    while len(string_digits) < count_digits:
        string_digits += ''.join(random.sample(string_digits,1))

    password = ''.join(random.sample(string_digits, count_digits))
    letters = string.ascii_lowercase

    if case_sensitive:
        letters += string.ascii_uppercase

    while len(letters) < count_ascii_letters:
        letters += ''.join(random.sample(letters, 1))

    password += ''.join(random.sample(letters, count_ascii_letters))
    password = ''.join(random.sample(password, len(password)))

    return password


def get_password_mb(count_digits: str, count_ascii_letters: str, case_sensitive=False):
    mb.showinfo(title='password value',
                message=get_password(count_digits=count_digits
                                     , count_ascii_letters=count_ascii_letters
                                     , case_sensitive=case_sensitive
                                     )
                )


def get_password_by_command(count_digits: str, count_ascii_letters: str, case_sensitive: str):
    try:
        get_password_mb(count_digits=count_digits, count_ascii_letters=count_ascii_letters)
    except (NoneCountAsciiLettersError, NoneCountAsciiLettersError):
        mb.showerror(title='error', message='Not value for generate password')
    except ValueError:
        mb.showerror(title='error', message='Enter value is not digit')


def main():
    root = tk.Tk()
    root.title('generator of passwords')
    frm = tk.Frame(root)
    frm.grid(column=0, row=0)

    count_digits_label = tk.Label(frm, text='count_digits:')
    count_digits_label.grid(column=0, row=0, sticky=tk.W)

    count_digits_entry = tk.Entry(frm)
    count_digits_entry.grid(column=1, row=0)

    count_digits_label = tk.Label(frm, text='count_ascii_letters:')
    count_digits_label.grid(column=0, row=2)

    count_ascii_letters_entry = tk.Entry(frm)
    count_ascii_letters_entry.grid(column=1, row=2)

    d = count_digits_entry
    a = count_ascii_letters_entry

    count_digits_button = tk.Button(frm,
                                    text='generate',
                                    command=lambda: get_password_by_command(d.get(), a.get(),'')
                                    )

    count_digits_button.grid(column=3, row=0)

    root.mainloop()


if __name__ == '__main__':
    main()
