Pygments SaC Lexer
------------------

This repo provides a Python Pygments plugin to add syntax highlighting for the [Single-Assignment C][1] programming language.

Our lexer extends the Pygments builtin `CLexer` for the C-language.

Usage
=====

Ensure you have `setuptools` available for your preferred version of Python (2 or 3) and the `pygments` package as well. Then in
the repository directory do:

```bash
# to install in your home directory
$ python setup.py install --user
```

You can also call this directly from Pygments, see [in their documentation][2].

[1]: https://www.sac-home.org/
[2]: http://pygments.org/docs/lexerdevelopment/#adding-and-testing-a-new-lexer
