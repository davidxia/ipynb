import ipynb.fs.full.a as a
import ipynb.fs.full.a.foo as foo


def test_a():
    assert a.init() == 'init'

def test_foo():
    assert foo.foo() == 'foo'

def test_execute():
    assert foo.bar == 'hi'

def test_allcaps_execute():
    assert foo.WAT == 'boo'