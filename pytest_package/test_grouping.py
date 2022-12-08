
from pytest import mark

@mark.smoke
def test_login():         #smoke testing
    print("Login is working")

@mark.regression
def test_mobiles():       #regression testing
    print("mobiles are purchased")

@mark.regression
def test_dress():         #regression testing
    print("dress are purchased")

@mark.smoke
def test_logout():        #smoke testing
    print("Logout is working")