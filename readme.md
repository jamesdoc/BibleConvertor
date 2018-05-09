# BibleConvertor

This script will convert the `sqlite` files from [Liu DongMiao's Bible Data repo](https://github.com/liudongmiao/bibledata) to a file that [OpenLP](https://manual.openlp.org/bibles.html) and [OpenSong](http://www.opensong.org/home/importing) can read.

Please note that this this has _only_ been tested with the [NIV2011](https://www.dropbox.com/s/7l8u3fr5e3dmpjc/niv2011?dl=0) file importing into OpenLP and will require work for other files…

## Setup

A small knowledge of Python is required to get this working… 


1. Download and unzip the translation of the Bible you want from [Liu DongMiao's Bible Data repo](https://github.com/liudongmiao/bibledata)
2. [pip install Unidecode](https://pypi.org/project/Unidecode/)
3. Update python script (line 7 and 8) to point to the correct file
4. `python convert.py`

## Pull Requests?

Yes. Please feel free. This was built quickly to scratch an itch I had.