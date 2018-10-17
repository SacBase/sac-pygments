from setuptools import setup, find_packages

setup (
  name='saclexer',
  version='1.0.0',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  saclexer = saclexer.lexer:SaCLexer
  """,
)
