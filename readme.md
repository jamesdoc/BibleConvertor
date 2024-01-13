# BibleConvertor

This script will convert the `sqlite` files from [MyBible module repository](https://www.ph4.org/b4_index.php) to a file that [OpenLP](https://manual.openlp.org/bibles.html) and [OpenSong](http://www.opensong.org/home/importing) can read.

Please note that this this has _only_ been tested with the [NIV 2011](https://www.ph4.org/b4_index.php?y=NIV) file importing into OpenSong and will require work for other files…

## Setup

A small knowledge of Python is required to get this working… 


1. Download and unzip the translation of the Bible you want from [MyBible module repository](https://www.ph4.org/b4_index.php)
2. [pip install Unidecode](https://pypi.org/project/Unidecode/)
3. Update python script (line 9 and 10) to point to the correct file
4. `python convert.py`

## Pull Requests?

Yes. Please feel free. This was built quickly to scratch an itch I had.