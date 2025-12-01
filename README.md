# ofx2csv
Tired of searching for a good website to convert the ofx files I get every month, which are useless if they are not on csv, so I've made this.
The current encoding is iso-8859-1 (brazilian banks default) but you can change to the desired one directly in the code.

to run it create your virtual environment and install Ofx parser
```
python -m venv .venv
pip install ofxparser
```

then just run the program along the filename
```
python ofx2csv.py file.py
```



I'm planning on hosting this on my server using a github domain, if anybody wishes to collab on this are more than welcome.
