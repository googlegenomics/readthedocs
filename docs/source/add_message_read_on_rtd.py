#! /usr/bin/env python

# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# add_message_read_on_rtd.py
#
# If someone lands on one of our pages on github, we want to direct
# them to read the content on Read The Docs.
#
# The content on github can look incomplete, as the includes used
# are not rendered by the github viewer.
#
# To make this work, we add some reStructuredText to each page that
# is hidden on Read The Docs.
#
# We use the reStructuredText "container"
# (http://docutils.sourceforge.net/docs/ref/rst/directives.html#container)
# which creates a DIV with a CSS "class" of the same name.
# We then add that class to the Read The Docs CSS with attributes to hide it.
#

import os
import subprocess
import sys
import StringIO

# Wrap the block of text that we write in reStructuredText comments so
# that we can easily change the text here and re-run it over the docs
#
# Note that a "comment" is any unknown directive, but I have used ".. comment"
# as a convention.

TARGET_START = ".. comment: begin: goto-read-the-docs"
TARGET_END = ".. comment: end: goto-read-the-docs"

TARGET_TEXT = TARGET_START + """

.. container:: visible-only-on-github

   +-----------------------------------------------------------------------------------+
   | **The properly rendered version of this document can be found at Read The Docs.** |
   |                                                                                   |
   | **If you are reading this on github, you should instead click** `here`__.         |
   +-----------------------------------------------------------------------------------+

.. _RenderedVersion: http://googlegenomics.readthedocs.org/en/latest/%s

__ RenderedVersion_

""" + TARGET_END + """
"""

# Simple utility function to run a command
def run_command(argv):
  return subprocess.check_output(argv)

# Process all RST files in the use_cases directory
def get_file_list():
  return run_command(["find", "use_cases/", "-name", "*.rst"])

# The function below, "find_target" returns a list with three elements
# indicating where we found:
#   0: the start of the inserted content
#   1: the end of the inserted content
#   2: the end of the page title
#
# This simplifies the writer function update_file() such that it can
# more trivially handle both a "clean" file and one that already has
# the targeted "goto-read-the-docs" content inserted.

TARGET_START_IDX = 0
TARGET_END_IDX = 1
TITLE_END_IDX = 2

# find_target
#
# Find the start of the target content (if present), then end of the
# target content (if present), and the end of the page title.
#
# Finding the page title is not precise - we look for the last line
# (in the first 20) that starts with "====".
#
def find_target(file):
  lines = [-1, -1, -1]
  line_no = 0
  for line in open(file, 'r'):
    line_no += 1
    if line.startswith(TARGET_START):
      lines[TARGET_START_IDX] = line_no
    elif line.startswith(TARGET_END):
      lines[TARGET_END_IDX] = line_no
    elif line_no < 20 and \
         line.startswith("===="):
      lines[TITLE_END_IDX] = line_no

  return lines

# update_file
#
# Creates a temporary file that is a copy of the source file, with the
# exception that the "target text" is added.
def update_file(file, target_loc):
  print "Update %s: %s" % (file, target_loc)

  # Sanity check the input

  # Every page must have a title
  assert target_loc[TITLE_END_IDX] != -1

  # Every page either has both the "start" and "end" marker, or neither
  assert ((target_loc[TARGET_START_IDX] == -1 and
           target_loc[TARGET_END_IDX] == -1) or
          (target_loc[TARGET_START_IDX] != -1 and
           target_loc[TARGET_END_IDX] != -1))

  # Set up the start and end line numbers in the source file as to where
  # to insert the new text
  if target_loc[TARGET_START_IDX] > -1:
    start_line_no = target_loc[TARGET_START_IDX]
    end_line_no = target_loc[TARGET_END_IDX]
    pad = False
  else:
    start_line_no = target_loc[TITLE_END_IDX] + 1
    end_line_no = start_line_no
    pad = True  # throw in a blank line at the start/end of the inserted text

  print "updating %s: %s, %s" % (file, start_line_no, end_line_no)

  # Open a temporary file for output
  outfile = file + ".tmp"
  output = open(outfile, 'w')

  line_no = 0
  for line in open(file, 'r'):
    line_no += 1

    # 4 different "states" handled here:
    #  1- prior to the start: emit the current line
    #  2- after to the end: emit the current line
    #  3- found the start line: emit the target text
    #  4- between the start and end lines: do nothing
    if line_no < start_line_no or \
       line_no > end_line_no:
      output.write(line)
    elif line_no == start_line_no:
      inpath = os.path.splitext(file)
      rendered_filename = inpath[0] + ".html"

      if pad: output.write("\n")
      output.write(TARGET_TEXT % rendered_filename)
      if pad: output.write("\n")

  output.close()

  os.remove(file)
  os.rename(outfile, file)
file_list = StringIO.StringIO(get_file_list())

for file in file_list.readlines():
  file = file.rstrip()

  # Make a full pass over the file to see if it contains the target content
  target_loc = find_target(file)

  # Now insert the target content, either at the location of the existing
  # target content, or just below the title
  update_file(file, target_loc)

