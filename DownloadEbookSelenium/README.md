# Title

Test for downloading ebooks from https://www.salesmanago.com written in Python and Selenium library.

# Requirements

* `python 3.9`
* `selenium 3.141.0`
* `pytest 6.2.5`

# Installation

Using `virtualenv` install all required packages with:

```commandline
pip install -r requirements.txt
```

Script needs for working chromedriver.exe which can be downloaded from below location (be aware that main version 
of chromedriver must be the same as your Chrome browser version):
https://chromedriver.chromium.org/downloads

Additionally, it is required to place chromedriver executable file i.ex. at "C:\Test_Files" 
and add this location to windows PATH.

# Run scenario using pytest

You need to invoke command window in location of project files and then write:
```commandline
pytest --stringinput name_of_ebook
```

# Run scenario without pytest

You need to invoke command window in location of project files and then write:
```commandline
python test_ebook_downloading.py ebook_name
```
