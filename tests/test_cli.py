import pytest
from pgbackup import cli

url = "postgres://bob@example.com:5432/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    Without a specified driver the parser should exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):
    """
    The parses should exit if it receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local" ])

def test_parser_with_unknown_driver(parser):
    """
    The parser should fail if the driver name is different than 'local' and 's3'
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "azure", "/var/backups/my_db"])

def test_parser_with_known_drivers(parser):
    """
    The parser should not exit if it receives known drivers
    """
    for driver in ('local', 's3'):
        assert parser.parse_args([url, "--driver", driver, "/some/example/dest"])

def test_valid_parser(parser):
    """
    The parser should not exit if it receives a valid driver and destination
    """
    args = parser.parse_args([url, "--driver", "local", "/var/backups/my_db"])

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == "/var/backups/my_db"

