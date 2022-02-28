import gzip

def sample_lines(file, lines):
    unzipped_file = gzip.open(file, "rb")
    contents = unzipped_file.read()
    for line in contents:
        print(line)
