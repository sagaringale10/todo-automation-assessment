# todo-automation-assessment
Assesment for cognizant

**Cognizant Internal Evaluation: Automation Technical Challenge**

This project was inspired also by Selene which is an attempt to implement Selenide + htmlelements in Python.

It differs from Selene
* by using Selenium explicit waits under the hood (Selene implements its own explicit waits)
* by using Selenium style of expected conditions to be used with explicit waits
* only manual webdriver creation (Selene creates and closes driver automatically)
* no Element Widgets support (like in htmlelements), though can be added soon rather easy
* no screenshots in error messages (though can be added very easy)
This simplified the implementation a lot, but have some drawbacks becuase selenium's expected conditions are not handy in use, limiting the possibilities.

## To start writing tests
* install python 
* install selenium and pytest
* install IDE (e.g. PyCharm CE)
* clone or download the repo
* open in IDE
* write your own tests under the tests folder
* run them from command line via py.test command executed from the project folder

(google on installation guides for all tools)

## TODOs
* add more docs and howtos on insallation and usage, etc.
* add "one test per feature" style tests with before/after hooks for clearing data
* tag smoke tests
* implement conditions in a simpler and smarter way

## Extra notes

### About PageObjects

This version of the project contains all "helpers to work with page's elements" in a separate PageObject implemented
as a simple Python module. 
