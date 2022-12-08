# import pytest
#
# @pytest.fixture()          #1.setup module.
#
# def design():
#     print("#### hi ###")
# def test_spam(design):
#     print("hello")
# def test_display(design):
#     print("Welcome for learning")

# @pytest.fixture(autouse = True)          #1.setup module. to apply by default to all function (autouse=true)
#
# def design():
#     print("#### hi ###")
# def test_spam():
#     print("hello")
# def test_display():
#     print("Welcome for learning")

# import pytest

# @pytest.fixture(scope="class")          #1.setup module. to apply by default to all function (autouse=true)

# def design():
#     print("#### hi ###")
#     yield
#     print("###bye###")
# using conftest
# class Testspam:
#     def test_spam(common):
#         print("hello")
# def test_display(common):
#     print("Welcome for learning")

# if fixture to be applied within class
# scope boundary for applying fixtures

# import pytest
# @pytest.fixture(scope="class")    #if scope= module, fixture gets applied for entire module.
#                                   #if scope = session, fixture will be applied for entire session.
# def design():
#     print("#### hi ###")
#     yield
#     print("###bye###")
#
#
# def test_display():
#     print("Welcome for learning")
#
#
# @pytest.mark.usefixtures("design")
# class TestSample:
#     def test_spam(self):
#         print("hello")
#
#     def test_spam1(self):
#         print("hello")
#
#
# class Testsample1:
#     def test_spam1(self):
#         print("it should allow fixture")


