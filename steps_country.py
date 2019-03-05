# file:features/steps/steps_country.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import *
from hamcrest import assert_that, equal_to, has_items
from country_api import Country


@given('I want to get the capital of "{country}"')
def step_given_add_country(context, country):
    context.set_country = Country()
    context.set_country.add_country(country)

@when('I send the API request')
def step_when_send_api(context):
    context.set_country.send_api()
    print("log.info: Request url: "+context.set_country.response_json_map['url'])

@then('response should return string "{parameter_string}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_string, parameter_country):
    assert_that(context.set_country.response_json_map[parameter_string], equal_to(parameter_country))

@then('response should return integer "{parameter_integer}" : "{parameter_country}"')
def step_and_should_return_string(context, parameter_integer, parameter_country):
    assert_that(context.set_country.response_json_map[parameter_integer], equal_to(int(parameter_country)))
