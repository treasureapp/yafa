from yafa.foo import bar


def test_foo():
    # type: () -> ()
    assert "bar method" == bar()
