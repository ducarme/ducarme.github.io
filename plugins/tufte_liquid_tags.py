"""
Sidenote and Margin Tags
----------
This implements a Liquid-style tags margin and side notes
for Pelican

Syntax
------

{% newthought 'Start of new paragraph' %}
{% sidenote 'side-note-id' 'side-note' %}
{% marginnote 'margin-note-id' 'margin-note' %}
{% marginfigure 'margin-figure-id' 'path/to/image' 'this is the caption' ['alternate image text'] %}
{% fullwidth 'path/to/image' 'Caption for the image' ['alternate image text']%}
Output
------
<label for="margin-note-id" class="margin-toggle">+</label>
<input type="checkbox" id="margin-note-id" class="margin-toggle" />
<span class="marginnote">'margin-note'</span>

"""
import re
from pelican.plugins.liquid_tags.mdx_liquid_tags import LiquidTags

NEWTHOUGHTSYNTAX = '''{% newthought some text %}'''
newthought_RE = re.compile('''(?P<newthought_text>.*)''')

MARGINSYNTAX = '''{% marginnote ["margin-note-id"|'margin-note-id'] ["margin-note-id"|'margin-note-id']%}'''
marginnote_RE = re.compile(r'''(?:"|')(?P<marginid>[^"']+)(?:"|')\s+(?:"|')(?P<marginnote>[^"']+)(?:"|')''')

SIDESYNTAX = '''{% sidenote ["side-note-id"|'side-note-id'] ["side-note-id"|'side-note-id']%}'''
sidenote_RE = re.compile(r'''(?:"|')(?P<sideid>[^"']+)(?:"|')\s+(?:"|')(?P<sidenote>[^"']+)(?:"|')''')

FULLWIDTHSYNTAX = '''{% fullwidth [https?:/]/path/to/image "image caption"%}'''
fullwidth_RE = re.compile(r'''(?:"|')(?P<fullwidth_image_path>[^"']+)(?:"|')\s+(?:"|')(?P<fullwidth_image_caption>[^"']+)(?:"|')''')

MAINCOLUMNSYNTAX = '''{% maincolumn "[https?:/]/path/to/image" "image caption" %}'''
maincolumn_RE = re.compile(r'''((['"])(?P<maincolumn_image_path>.*)([^\1]))\s+((['"])(?P<maincolumn_image_caption>.*)([^\4]))''')

MARGINFIGURESYNTAX = '''{% marginfigure "marginfigure_id" "[https?:/]/path/to/image" "image caption"%}'''
marginfigure_RE = re.compile(r'''((['"])(?P<marginfigure_id>.*)([^\1]))\s+((['"])(?P<marginfigure_image_path>.*)([^\4]))\s+((['"])(?P<marginfigure_image_caption>.*)([^\7]))''')

@LiquidTags.register('marginnote')
def marginnote(preprocessor, tag, markup):
    marginnote_attrs = None

    # Parse the markup string
    marginnote_match = marginnote_RE.search(markup)
    if marginnote_match:
        marginnote_attrs = marginnote_match.groupdict()
    else:
        raise ValueError('Error processing input. '
                         'Expected syntax: {0}'.format(MARGINSYNTAX))

    marginnote_html = '''<label for="''' + marginnote_attrs['marginid']
    marginnote_html += '''" class="margin-toggle">&#8853;</label>'''
    marginnote_html += '''<input type="checkbox" id="'''
    marginnote_html += marginnote_attrs['marginid'] 
    marginnote_html += '''" class="margin-toggle" />'''
    marginnote_html += '''<span class="marginnote">'''
    marginnote_html += marginnote_attrs['marginnote']
    marginnote_html += '''</span>'''

    return marginnote_html


@LiquidTags.register('sidenote')
def sidenote(preprocessor, tag, markup):
    sidenote_attrs = None

    # Parse the markup string
    sidenote_match = sidenote_RE.search(markup)
    if sidenote_match:
        sidenote_attrs = sidenote_match.groupdict()
    else:
        raise ValueError('Error processing input. '
                         'Expected syntax: {0}'.format(SIDESYNTAX))

    sidenote_html = '''<label for="''' + sidenote_attrs['sideid']
    #This is the difference between sidenote and margin note
    sidenote_html += '''" class="margin-toggle sidenote-number"></label>'''
    sidenote_html += '''<input type="checkbox" id="'''
    sidenote_html += sidenote_attrs['sideid'] 
    sidenote_html += '''" class="margin-toggle" />'''
    sidenote_html += '''<span class="sidenote">'''
    sidenote_html += sidenote_attrs['sidenote']
    sidenote_html += '''</span>'''

    return sidenote_html


@LiquidTags.register('newthought')
def newthought(preprocessor, tag, markup):
    newthought_attrs = None

    # Parse the markup string
    newthought_match = newthought_RE.search(markup)
    if newthought_match:
        newthought_attrs = newthought_match.groupdict()
    else:
        raise ValueError('Error processing input. '
                         'Expected syntax: {0}'.format(NEWTHOUGHTSYNTAX))

    newthought_html = '''<span class='newthought'>''' 
    newthought_html += newthought_attrs['newthought_text']
    newthought_html += '''</span>'''

    return newthought_html

@LiquidTags.register('fullwidth')
def fullwidth(preprocessor, tag, markup):
    fullwidth_attrs = None

    # Parse the markup string
    fullwidth_match = fullwidth_RE.search(markup)
    if fullwidth_match:
        fullwidth_attrs = fullwidth_match.groupdict()
    else:
        raise ValueError('Error processing fullwidth input.'
                         'Expected syntax: {0}'.format(FULLWIDTHSYNTAX))

    fullwidth_html = '''<figure class="fullwidth">'''
    fullwidth_html += '''<img src="'''
    fullwidth_html += fullwidth_attrs['fullwidth_image_path']
    fullwidth_html += '''">'''
    fullwidth_html += '''<figcaption>'''
    fullwidth_html += fullwidth_attrs['fullwidth_image_caption']
    fullwidth_html += '''</figcation></figure>'''

    return fullwidth_html


@LiquidTags.register('maincolumn')
def maincolumn(preprocessor, tag, markup):
    maincolumn_attrs = None

    # Parse the markup string
    maincolumn_match = maincolumn_RE.search(markup)
    if maincolumn_match:
        maincolumn_attrs = maincolumn_match.groupdict()
    else:
        raise ValueError('Error processing maincolumn input. '
                         'Expected syntax: {0}'.format(MAINCOLUMNSYNTAX))

    maincolumn_html = '''<figure>'''
    maincolumn_html += '''<figcaption>'''
    maincolumn_html += maincolumn_attrs['maincolumn_image_caption']
    maincolumn_html += '''</figcaption>'''
    maincolumn_html += '''<img src="'''
    maincolumn_html += maincolumn_attrs['maincolumn_image_path']
    maincolumn_html += '''"/></figure>'''
    
    return maincolumn_html


@LiquidTags.register('marginfigure')
def marginfigure(preprocessor, tag, markup):
    marginfigure_attrs = None

    # Parse the markup string
    marginfigure_match = marginfigure_RE.search(markup)
    if marginfigure_match:
        marginfigure_attrs = marginfigure_match.groupdict()
    else:
        raise ValueError('Error processing marginfigure input. \n'
                         'Expected syntax: {0}'.format(MARGINFIGURESYNTAX))

    marginfigure_html = '''<label for="''' + marginfigure_attrs['marginfigure_id']
    marginfigure_html += '''" class="margin-toggle">&#8853;</label>'''
    marginfigure_html += '''<input type="checkbox" id="'''
    marginfigure_html += marginfigure_attrs['marginfigure_id'] 
    marginfigure_html += '''" class="margin-toggle" />'''
    marginfigure_html += '''<span class="marginnote">'''
    marginfigure_html += '''<img class="fullwidth" src="'''
    marginfigure_html += marginfigure_attrs['marginfigure_image_path']
    marginfigure_html += '''" alt="'''
    marginfigure_html += marginfigure_attrs['marginfigure_image_caption']
    marginfigure_html += '''"/><br/>'''
    marginfigure_html += marginfigure_attrs['marginfigure_image_caption']
    marginfigure_html += '''</span>'''

    return marginfigure_html



#----------------------------------------------------------------------
# This import allows Tufte tags to be a Pelican plugin
from pelican.plugins.liquid_tags import register