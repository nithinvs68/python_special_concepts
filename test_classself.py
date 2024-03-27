# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print(id(self))
#     def pri(self):
#         print(self.a,self.b)
#         print(id(self))
#
# g=A(1,2)
# g.pri()
# print('g',id(g))
# h=A(2,2)
# h.pri()
# print('h',id(h))
# from enum import verify
import pytest
import pytest_check
from allure_commons.types import AttachmentType
from selenium import webdriver
# from selenium.
import allure
class TestDemo:
    # def __init__(self,driver):
    #     self.driver=driver

    @pytest.fixture(scope="function",autouse=True)
    def demo1(self):
        print('tttt')

    def test_printt(self,demo1):
        pass

#add severity of class
@allure.severity(allure.severity_level.NORMAL)

class Test1(TestDemo):
    #add severity for function
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logo(self):
        # io=Demo()
        # io.printt()
        self.driver=webdriver.Edge()
        self.driver.get("www.google.com")
        self.driver.scree
        #attach ss to allure report
        allure.attach(self.driver.get_screenshot_as_png(),'testdemoss',attachment_type=AttachmentType.PNG)
        print('gingalaka')

    @allure.severity(allure.severity_level.MINOR)
    def test_verify(self):
        # pytest.soft_assert(1==2,'error')
        assert 1==9
        print('nitin')
        assert 0==99

    def test_1(self):
        assert 1==1

    def test_skip(self):
        pytest.skip('this will be skipped')

    def test_2(self):
        assert 5==4


    def test_3(self):
        assert 'a'=="aa"


import datetime
from pytest_check import check
from assertpy import soft_assertions,assert_that
def test_date():
    a,b=8,9
    date=datetime.datetime.now()
    print(date)
    check.is_true(a==b)
    # pytest.fail('pppp')
    newdate=date.strftime("%Y%m%d%H%M%S")
    print('Login'+newdate)



