from behave import *
from hamcrest import *

import electro_requests as util

def parse_antwoord(antwoord):
    if (antwoord == "Geen berekening mogelijk met de opgegeven parametercombinatie"):
        raise ValueError
    items = antwoord.split() # example: 'I = 2.000000 ampere'
    number = float(items[2])
    return number

@given(u'the battery calculation module is online and available')
def step_impl(context):
    assert_that(util.website_up("http://dingdata.nl/batterij"))


@when(u'I call the battery calculation module for I with {inp_Uk} and {inp_Rl}')
def step_impl(context, inp_Uk, inp_Rl):
    inp_Uk, inp_Rl = float(inp_Uk), float(inp_Rl)
    context.response = util.batterij_request({"UK": inp_Uk, "RL": inp_Rl})


@when(u'I call the battery calculation module for Uk with {inp_Ub}, {inp_Ri} and {inp_Rl}')
def step_impl(context, inp_Ub, inp_Ri, inp_Rl):
    inp_Ub, inp_Ri, inp_Rl  = float(inp_Ub), float(inp_Ri), float(inp_Rl)
    context.response = util.batterij_request({"UB": inp_Ub, "RI": inp_Ri, "RL": inp_Rl})


@then(u'The module calculates the correct value of {inp_outcome}')
def step_impl(context, inp_outcome):
    inp_outcome = float(inp_outcome)
    antwoord = context.response["resultaten"]["antwoord"]
    outcome = parse_antwoord(antwoord)
    assert_that(outcome, equal_to(inp_outcome))