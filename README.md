# deterfox-patch

Build & Run
1. Clone gecko-dev(https://github.com/nkdxczh/gecko-dev.git) and deterfox-patch, put them in the same directory.
2. Run patch.py in deterfox-patch.
3. Follow Mozilla build instruction to build and run firefox(https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Build_Instructions/Simple_Firefox_build).
   Instructions for Linx:
   1. enter gecko-dev dir.
   2. run "sudo apt-get install autoconf2.13"
   3. run "wget -q https://hg.mozilla.org/mozilla-central/raw-file/default/python/mozboot/bin/bootstrap.py -O bootstrap.py && python bootstrap.py"
   4. run "./mach build"
   5. run "./mach run"
