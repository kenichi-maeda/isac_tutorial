def test_import_package():
    """Test that the package has the expected structure."""
    import isac_tutorial

    # Check that __version__ exists
    assert hasattr(isac_tutorial, "__version__"), "Package should have __version__ attribute"


def test_import_core():
    """Test that the core module can be imported."""
    from isac_tutorial import core

    assert core is not None
