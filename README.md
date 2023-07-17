# gitignore-this

CLI helper to quickly add a file to .gitignore in its parent folder.


## Usage

Append entry `bar.txt` to `foo/.gitignore`:

    gitignore-this.py foo/bar.txt


Append entry `*.txt` to `foo/.gitignore`:

    gitignore-this.py --glob-stem foo/bar.txt
