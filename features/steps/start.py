import os
from behave import *

@given(u'There is an empty text file available to us')
def step_impl(context):
    outfile = open("text_file.txt", "w")
    outfile.close()

    context.outfile_name = "text_file.txt"

    assert os.stat("text_file.txt").st_size == 0

@when(u'I open this file')
def step_impl(context):
    outfile = open("text_file.txt", "wt")
    context.outfile = outfile
    #outfile.close()

@when(u'I write the following table in it')
def step_impl(context):
    outfile = context.outfile
    for row in context.table:
        line = f"{row['course']}\t{row['participants']}\n"
        outfile.write(line)
        #add_line_to_file(context.outfile_name, line)
    outfile.close()

@then(u'This file has {num_lines} lines in it')
def step_impl(context, num_lines):
    infile = open(context.outfile_name, "r")
    lines = infile.readlines()
    infile.close

    assert len(lines) == int(num_lines)

@given(u'The text file has been opened')
def step_impl(context):
    context.outfile = open("text_file.txt", "at")
    context.outfile_name = "text_file.txt"

    assert not context.outfile.closed

@then(u'I write the values {first}, {second} and {third}')
def step_impl(context, first, second, third):
    outfile = context.outfile
    outfile.write(f"{first}\t{second}\t{third}\n")
    outfile.close()

@then(u'I close the file')
def step_impl(context):
    context.outfile.close()
    assert context.outfile.closed
