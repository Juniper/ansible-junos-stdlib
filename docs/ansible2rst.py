#!/usr/bin/env python
# (c) 2012, Jan-Piet Mens <jpmens () gmail.com>
#
# This file is part of Ansible
#
# Modified to support stand-alone Galaxy documentation
# Copyright (c) 2014, Juniper Networks Inc.
#               2014, Rick Sherman
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import re
import sys
import datetime
import cgi
from jinja2 import Environment, FileSystemLoader

import ansible.utils
from ansible.utils import module_docs

#####################################################################################
# constants and paths

_ITALIC = re.compile(r"I\(([^)]+)\)")
_BOLD = re.compile(r"B\(([^)]+)\)")
_MODULE = re.compile(r"M\(([^)]+)\)")
_URL = re.compile(r"U\(([^)]+)\)")
_CONST = re.compile(r"C\(([^)]+)\)")

MODULEDIR = "../library/"
OUTPUTDIR = "."

#####################################################################################


def rst_ify(text):
    ''' convert symbols like I(this is in italics) to valid restructured text '''

    t = _ITALIC.sub(r'*' + r"\1" + r"*", text)
    t = _BOLD.sub(r'**' + r"\1" + r"**", t)
    t = _MODULE.sub(r'``' + r"\1" + r"``", t)
    t = _URL.sub(r"\1", t)
    t = _CONST.sub(r'``' + r"\1" + r"``", t)

    return t

#####################################################################################


def html_ify(text):
    ''' convert symbols like I(this is in italics) to valid HTML '''

    t = cgi.escape(text)
    t = _ITALIC.sub("<em>" + r"\1" + "</em>", t)
    t = _BOLD.sub("<b>" + r"\1" + "</b>", t)
    t = _MODULE.sub("<span class='module'>" + r"\1" + "</span>", t)
    t = _URL.sub("<a href='" + r"\1" + "'>" + r"\1" + "</a>", t)
    t = _CONST.sub("<code>" + r"\1" + "</code>", t)

    return t


#####################################################################################

def rst_fmt(text, fmt):
    ''' helper for Jinja2 to do format strings '''

    return fmt % (text)

#####################################################################################


def rst_xline(width, char="="):
    ''' return a restructured text line of a given length '''

    return char * width

#####################################################################################


def write_data(text, outputname, module, output_dir=None):
    ''' dumps module output to a file or the screen, as requested '''

    if output_dir is not None:
        f = open(os.path.join(output_dir, outputname % module), 'w')
        f.write(text.encode('utf-8'))
        f.close()
    else:
        print text

#####################################################################################


def jinja2_environment(template_dir, typ):

    env = Environment(loader=FileSystemLoader(template_dir),
                      variable_start_string="@{",
                      variable_end_string="}@",
                      trim_blocks=True,
                      )
    env.globals['xline'] = rst_xline

    if typ == 'rst':
        env.filters['convert_symbols_to_format'] = rst_ify
        env.filters['html_ify'] = html_ify
        env.filters['fmt'] = rst_fmt
        env.filters['xline'] = rst_xline
        template = env.get_template('rst.j2')
        outputname = "%s.rst"
    else:
        raise Exception("unknown module format type: %s" % typ)

    return env, template, outputname

#####################################################################################


def process_module(fname, template, outputname):

    print MODULEDIR + fname
    doc, examples, returndocs = module_docs.get_docstring(MODULEDIR + fname)

    all_keys = []

    if 'version_added' not in doc:
        sys.stderr.write("*** ERROR: missing version_added in: %s ***\n".format(fname))
        sys.exit(1)

    added = 0
    if doc['version_added'] == 'historical':
        del doc['version_added']
    else:
        added = doc['version_added']

    # don't show version added information if it's too old to be called out
    if added:
        added_tokens = str(added).split(".")
        added = added_tokens[0] + "." + added_tokens[1]
        added_float = float(added)

    for (k, v) in doc['options'].iteritems():
        all_keys.append(k)
    all_keys = sorted(all_keys)
    doc['option_keys'] = all_keys

    doc['filename'] = fname
    doc['docuri'] = doc['module'].replace('_', '-')
    doc['now_date'] = datetime.date.today().strftime('%Y-%m-%d')
    doc['plainexamples'] = examples  # plain text

    # here is where we build the table of contents...

    text = template.render(doc)
    write_data(text, outputname, fname, OUTPUTDIR)

#####################################################################################


def main():

    env, template, outputname = jinja2_environment('.', 'rst')
    modules = []

    for module in os.listdir(MODULEDIR):
        if module.startswith("junos_"):
            process_module(module, template, outputname)
            modules.append(module)

    index_file_path = os.path.join(OUTPUTDIR, "index.rst")
    index_file = open(index_file_path, "w")
    index_file.write('Juniper.junos Ansible Modules\n')
    index_file.write('=================================================\n')
    index_file.write('\n')
    index_file.write('Contents:\n')
    index_file.write('\n')
    index_file.write('.. toctree::\n')
    index_file.write('   :maxdepth: 1\n')
    index_file.write('\n')

    for module in modules:
        index_file.write('   %s\n' % module)

if __name__ == '__main__':
    main()
