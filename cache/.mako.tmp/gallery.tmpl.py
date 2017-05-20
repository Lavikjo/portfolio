# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1495301918.8561718
_enable_loop = True
_template_filename = 'templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('{#  -*- coding: utf-8 -*- #}\n{% extends \'base.tmpl\' %}\n{% import \'comments_helper.tmpl\' as comments with context %}\n{% import \'crumbs.tmpl\' as ui with context %}\n{% block sourcelink %}{% endblock %}\n\n{% block content %}\n    {{ ui.bar(crumbs) }}\n    {% if title %}\n    <h1>{{ title }}</h1>\n    {% endif %}\n    {% if text %}\n    <p>\n        {{ text }}\n    </p>\n    {% endif %}\n    {% if photo_array %}\n    <ul class="thumbnails">\n        {% for image in photo_array %}\n            <li><a href="{{ image[\'url\'] }}" class="thumbnail image-reference" title="{{ image[\'title\'] }}">\n                <img src="{{ image[\'url_thumb\'] }}" alt="{{ image[\'title\'] }}" /></a>\n        {% endfor %}\n    </ul>\n    {% endif %}\n{% if enable_comments %}\n    {{ comments.comment_form(None, permalink, title) }}\n{% endif %}\n{% endblock %}')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "templates/gallery.tmpl", "line_map": {"16": 0, "27": 21, "21": 1}, "uri": "gallery.tmpl"}
__M_END_METADATA
"""
