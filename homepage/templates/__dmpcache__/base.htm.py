# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1532115166.0021
_enable_loop = True
_template_filename = '/Users/mac/Documents/BYU webdev/goldenspikes/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>Golden Spike Submissions</title>\n\n')
        __M_writer('        <!-- <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css"> -->\n        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,700" rel="stylesheet">\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n\n        <!-- <link type="text/css" rel="stylesheet" href="//cloud.typography.com/75214/6517752/css/fonts.css" media="all" /> -->\n        <link rel="stylesheet" href="https://cdn.byu.edu/byu-theme-components/latest/byu-theme-components.min.css" />\n        <script async src="https://cdn.byu.edu/byu-theme-components/latest/byu-theme-components.min.js"></script>\n        <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        __M_writer('        <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script> -->\n\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/js/bootstrap.min.js"></script>\n        <!-- Customized colors included in bootstrap -->\n        <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap-theme.min.css">\n        <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap/css/bootstrap.min.css">\n\n        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n\n      <byu-header>\n          <h1 slot="Golden Spikes Registration">Golden Spikes Registration</h1>\n      </byu-header>\n        <main>\n          <div class="container-fluid center">\n\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n            </div>\n          </div>\n        </main>\n\n        <footer>\n            <div><a href="http://goldenspikeawards.com/">Golden Spikes Site</a></div>\n            <div><a href="http://goldenspikeawards.com/entries/categories/">Golden Spikes Awards Categories</a></div>\n        </footer>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n                  Site content goes here in sub-templates.\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/mac/Documents/BYU webdev/goldenspikes/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "26": 2, "27": 10, "28": 19, "29": 21, "30": 21, "31": 23, "32": 23, "33": 24, "34": 24, "35": 27, "36": 27, "41": 40, "47": 38, "53": 38, "59": 53}}
__M_END_METADATA
"""
