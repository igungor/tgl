#!/usr/bin/env python
# coding: utf8

import os
import sys
import re
import pycparser.c_generator


def parse_constant(node):
    if isinstance(node, pycparser.c_ast.Constant):
        return node.value
    elif isinstance(node, pycparser.c_ast.UnaryOp) and node.op == '-':
        return '-' + parse_constant(node.expr)
    else:
        raise TypeError(node)


class PrintEnumsVisitor(pycparser.c_ast.NodeVisitor):
    def visit_Enum(self, node):
        value = 0
        if not node.values:
            return
        for enumerator in node.values.enumerators:
            if enumerator.value is not None:
                value_string = parse_constant(enumerator.value)
                value = int(value_string, 0)
            else:
                value_string = str(value)
            print(('%s = %s' % (enumerator.name, value_string)))
            value += 1
        print('')


def preprocess(source, keep_defines=False):

    #remove stuff not supported by pycparser or cffi
    #TODO: this damages the update_callback struct, needs manual edit
    source = re.sub(r'^.*__attribute__.*$', '', source, flags=re.MULTILINE)
    source = re.sub(
        '/\*.*?\*/'
        r'|//.*?\n',
        '',
        source,
        flags=re.DOTALL | re.MULTILINE)

    if not keep_defines:
        source = re.sub(r'^\s*#.*?[^\\]\n', '', source, flags=re.MULTILINE)
    else:
        #remove all directives except #define
        source = re.sub(r'^\s*#(?!define).*?[^\\]\n', '', source, flags=re.MULTILINE)

        #remove macro definitions as they are not supported by cffi
        source = re.sub(r'^\s*#define.*?\(.*?[^\\]\n', '', source, flags=re.MULTILINE)

        #remove #defines defining strings like #define foo "bar", not supported
        source = re.sub(r'^\s*#define.*?".*?[^\\]\n', '', source, flags=re.MULTILINE)

        #remove #define __TGL_H__ line
        source = re.sub(r'^\s*#define.*?_H__.*?$', '', source, flags=re.MULTILINE)

    source = re.sub('\n{3,}', '\n\n', source)
    return source


def read_header(tgl_source_dir, fl):
    filename = os.path.join(tgl_source_dir, fl)
    return open(filename).read()


def generate(tgl_source_dir):
    source = '''
typedef unsigned long size_t;
'''

    source += read_header(tgl_source_dir, 'tgl-serialize.h')
    source += read_header(tgl_source_dir, 'tgl-net.h')
    source += read_header(tgl_source_dir, 'tgl-timers.h')
    source += read_header(tgl_source_dir, 'tgl-layout.h')
    source += read_header(tgl_source_dir, 'tgl-binlog.h')
    source += read_header(tgl_source_dir, 'tgl-structures.h')
    source += read_header(tgl_source_dir, 'tgl-eventloop.h')
    source += read_header(tgl_source_dir, 'tgl.h')

    # Remove comments, preprocessor instructions and macros.
    ast = pycparser.CParser().parse(preprocess(source))

    print('# *** Do not edit this file ***')
    print('# Generated by utils/mkconstants.py\n')
    PrintEnumsVisitor().visit(ast)
    #here we write headers to python file along with the '#define foo NUMBER' definitions
    print(('_TGL_HEADERS = r"""%s"""' % preprocess(source, keep_defines=True)))


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        generate(sys.argv[1])
    else:
        print(('Usage: %s path/to/tgl_source_dir' % sys.argv[0]))
