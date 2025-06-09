import argparse, pathlib, shutil, re, subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--upstream", default="../ai-swiss-workflows",
                    help="Path or git URL of the upstream repo")
args = parser.parse_args()

if args.upstream.startswith("http"):
    # clone into a temp dir if a URL is given
    import tempfile, subprocess, os
    tmp = tempfile.TemporaryDirectory()
    subprocess.run(["git", "clone", "--depth", "1", args.upstream, 
tmp.name],
                   check=True)
    UPSTREAM = pathlib.Path(tmp.name)
else:
    UPSTREAM = pathlib.Path(args.upstream).expanduser()

