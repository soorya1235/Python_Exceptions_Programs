"""
Abstract method is a method without any defintion.
A class with contains Abstract method is called Abstract calss

"""
from abc import ABC,abstractmethod

class Webdriver(ABC):

    def __init__(self):
        print("construtor is called ")

    @abstractmethod
    def click(self):
        pass

#chrome = Webdriver()
#chrome.click()

""""
If you see we can call the method of class,using the object..which we are not supposed to do..with like 16 and 17
so we need to import the abstract

"""

class ChromeDriver(Webdriver):

    def click(self):
        print("providing defintion of abstract in A")

    def printscreenshot(self):
        print("screenshot")

c1 = ChromeDriver()
print(c1.printscreenshot())