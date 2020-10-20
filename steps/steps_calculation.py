# file:features/steps/steps_calculation.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import *
from hamcrest import assert_that, equal_to
from lib.calculate import Calculate

@given('I have 2 numbers "{x}" and "{y}"')
def load_numbers(context, x, y):
    context.math = Calculate()
    context.math.load_number(x, y)


@when('I "{operate}" them')
def do_math(context, operate):
    context.math.get_result(operate, context.math.first_integer, context.math.second_integer)

@then('I get the result "{result}"')
def check_result(context, result):
    assert_that(context.math.answer, equal_to(int(result)))


