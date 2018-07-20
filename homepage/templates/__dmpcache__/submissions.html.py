# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1532121881.8047092
_enable_loop = True
_template_filename = '/Users/mac/Documents/BYU webdev/goldenspikes/homepage/templates/submissions.html'
_template_uri = 'submissions.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        submissions = context.get('submissions', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        submissions = context.get('submissions', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content col-md-12" style="overflow-x:auto;">\n        <table>\n          <tr>\n            <th>Entry Title</th>\n            <th>Client</th>\n            <th>Division</th>\n            <th>Category</th>\n            <th>Status</th>\n            <th>Name</th>\n            <th>Email</th>\n            <th>Entry Form</th>\n            <th>Summary</th>\n            <th>Supporting File</th>\n            <th>Supporting File</th>\n            <th>Supporting File</th>\n            <th>Links</th>\n            <th>Links</th>\n            <th>Links</th>\n          </tr>\n')
        for s in submissions:
            __M_writer('            <tr>\n              <td>')
            __M_writer(str(s.entryTitle))
            __M_writer('</td>\n              <td>')
            __M_writer(str(s.client))
            __M_writer('</td>\n              <td>')
            __M_writer(str(s.division))
            __M_writer('</td>\n              <td>')
            __M_writer(str(s.category))
            __M_writer('</td>\n              <td>')
            __M_writer(str(s.status))
            __M_writer('</td>\n              <td>')
            __M_writer(str(s.name))
            __M_writer('</td>\n              <td>')
            __M_writer(str(s.email))
            __M_writer('</td>\n              <td><a href="//goldenspikes.s3.amazonaws.com/media/')
            __M_writer(str(s.entryForm))
            __M_writer('">link</a></td>\n              <td><a href="')
            __M_writer(str(STATIC_URL))
            __M_writer('goldenspikes/media/')
            __M_writer(str(s.summary))
            __M_writer('">link</a></td>\n')
            if s.file1:
                __M_writer('                <td><a href="')
                __M_writer(str(STATIC_URL))
                __M_writer('goldenspikes/media/')
                __M_writer(str(s.file1))
                __M_writer('">link</a></td>\n')
            else:
                __M_writer('                <td></td>\n')
            if s.file2:
                __M_writer('                <td><a href="')
                __M_writer(str(STATIC_URL))
                __M_writer('goldenspikes/media/')
                __M_writer(str(s.file2))
                __M_writer('">link</a></td>\n')
            else:
                __M_writer('                <td></td>\n')
            if s.file3:
                __M_writer('                <td><a href="')
                __M_writer(str(STATIC_URL))
                __M_writer('goldenspikes/media/')
                __M_writer(str(s.file3))
                __M_writer('">link</a></td>\n')
            else:
                __M_writer('                <td></td>\n')
            __M_writer('\n')
            if s.link1 is not '':
                __M_writer('                <td><a href="')
                __M_writer(str(s.link1))
                __M_writer('">link</a></td>\n')
            else:
                __M_writer('                <td></td>\n')
            if s.link2 is not '':
                __M_writer('                <td><a href="')
                __M_writer(str(s.link2))
                __M_writer('">link</a></td>\n')
            else:
                __M_writer('                <td></td>\n')
            if s.link3 is not '':
                __M_writer('                <td><a href="')
                __M_writer(str(s.link3))
                __M_writer('">link</a></td>\n')
            else:
                __M_writer('                <td></td>\n')
            __M_writer('            </tr>\n')
        __M_writer('        </table>\n\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/mac/Documents/BYU webdev/goldenspikes/homepage/templates/submissions.html", "uri": "submissions.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 70, "48": 3, "56": 3, "57": 23, "58": 24, "59": 25, "60": 25, "61": 26, "62": 26, "63": 27, "64": 27, "65": 28, "66": 28, "67": 29, "68": 29, "69": 30, "70": 30, "71": 31, "72": 31, "73": 32, "74": 32, "75": 33, "76": 33, "77": 33, "78": 33, "79": 34, "80": 35, "81": 35, "82": 35, "83": 35, "84": 35, "85": 36, "86": 37, "87": 39, "88": 40, "89": 40, "90": 40, "91": 40, "92": 40, "93": 41, "94": 42, "95": 44, "96": 45, "97": 45, "98": 45, "99": 45, "100": 45, "101": 46, "102": 47, "103": 49, "104": 50, "105": 51, "106": 51, "107": 51, "108": 52, "109": 53, "110": 55, "111": 56, "112": 56, "113": 56, "114": 57, "115": 58, "116": 60, "117": 61, "118": 61, "119": 61, "120": 62, "121": 63, "122": 65, "123": 67, "129": 123}}
__M_END_METADATA
"""
