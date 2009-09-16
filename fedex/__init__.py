"""
python-fedex API Documentation
==============================
The python-fedex module is a light wrapper around Fedex's Web Services SOAP API.
Using the excellent U{suds<https://fedorahosted.org/suds/>} SOAP client,
the Fedex requests and responses are trivial to work with.

What python-fedex is
--------------------
    - A light wrapper around Fedex Web Services SOAP API.
    - Simple and easy to use.
    - Minimal by design.

What python-fedex is not
------------------------
    - An abstraction layer. python-fedex only assembles the needed SOAP calls
        and returns a SOAP response through suds. This is easy enough to work with
        that no abstraction is needed. Doing so would limit your use of the data.
    - Anything more than a light wrapper.
    
A note on completeness
----------------------
python-fedex was created for use with some of my internal projects. For the
initial release, only the things that I needed at the time were implemented.
If there is missing functionality, please report an U{issue<http://code.google.com/p/python-fedex/issues/list>}
so that I may make this module more useful to others. Likewise, feel free to
submit patches as well if you would like to help.
    
Getting Support
---------------
If you have any questions, problems, ideas, or patch submissions, please visit
our U{Google Code project<http://code.google.com/p/python-fedex/>} and enter
an issue in the U{Issue Tracker<http://code.google.com/p/python-fedex/issues/list>}.
"""
VERSION = '0.1'