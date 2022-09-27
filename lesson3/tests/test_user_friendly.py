import pytest
from lesson3.user_friendly_size import user_friendly_size

file_cases = ((1024, '1.00 kB'), (9999, '9.76 kB'), (9999999, '9.54 MB'), (9999999999, '9.31 GB'),
              (99999999999999, '90.95 TB'), ('9999999999', '9.31 GB'), ('/etc/services', '662.09 kB'))

@pytest.mark.parametrize('file_size, expected_size', file_cases)
def test_user_friendly_size(file_size, expected_size):
    assert user_friendly_size(file_size) == expected_size