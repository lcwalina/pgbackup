from pgbackup import storage
from tempfile import TemporaryFile, NamedTemporaryFile

def test_storing_file_locally():
    """
    Writes content from one file-like to another
    """
    infile = TemporaryFile()
    infile.write(b'Testing')
    infile.seek(0)

    outfile = NamedTemporaryFile(delete=False)
    storage.local(infile, outfile)
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing'
