# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1495301345.6365955
_enable_loop = True
_template_filename = '/home/tatoma/git/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content_header():
            return render_content_header(context._locals(__M_locals))
        permalink = context.get('permalink', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        pagination = _mako_get_namespace(context, 'pagination')
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content_header():
            return render_content_header(context)
        page_links = context.get('page_links', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        def content():
            return render_content(context)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        date_format = context.get('date_format', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('<div class="postindex">\n')
        for post in posts:
            __M_writer('    <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </header>\n')
            if index_teasers:
                __M_writer('    <div class="p-summary entry-summary">\n    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('    <div class="e-content entry-content">\n    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            __M_writer('    </div>\n    </article>\n')
        __M_writer('</div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        posts = context.get('posts', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.tmpl", "line_map": {"128": 26, "129": 26, "130": 26, "131": 29, "132": 30, "133": 30, "134": 30, "135": 30, "136": 30, "137": 31, "138": 32, "139": 32, "140": 32, "141": 34, "142": 35, "143": 35, "144": 35, "145": 35, "146": 35, "147": 35, "148": 35, "149": 35, "150": 36, "23": 4, "152": 37, "153": 37, "26": 2, "155": 41, "156": 42, "29": 3, "158": 43, "159": 44, "160": 45, "161": 46, "162": 46, "35": 0, "164": 51, "165": 52, "166": 52, "167": 53, "168": 53, "169": 54, "170": 54, "157": 43, "176": 7, "186": 7, "187": 8, "151": 37, "189": 9, "190": 10, "191": 10, "192": 10, "65": 2, "66": 3, "67": 4, "68": 5, "198": 15, "73": 12, "78": 55, "209": 198, "163": 48, "84": 14, "188": 8, "108": 14, "154": 39, "113": 15, "114": 16, "115": 17, "116": 17, "117": 17, "118": 19, "119": 20, "120": 20, "121": 20, "122": 22, "123": 23, "124": 24, "125": 24, "126": 24, "127": 26}, "source_encoding": "utf-8", "filename": "/home/tatoma/git/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/index.tmpl"}
__M_END_METADATA
"""
