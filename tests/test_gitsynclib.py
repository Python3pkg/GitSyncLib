from gitsynclib import GitSync
from gitsynclib import GitNotified

def test_module():
    assert hasattr(GitSync, 'main')
    assert hasattr(GitSync, 'GitSync')
    assert hasattr(GitNotified, 'GitNotified')

