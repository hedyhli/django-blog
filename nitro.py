from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace

class NitroStyle(Style):
    """Colorful, modern Bulma-inspired style"""

    default_style = ""
    styles = {
        Whitespace:             '#bbbbbb',
        Comment:                '#888',
        Comment.Preproc:        '#557799',
        Comment.Special:        'bold #c55d5d',

        Keyword:                'bold #36a092',
        Keyword.Pseudo:         '#2d2c77',
        Keyword.Type:           '#2d2c77',

        Operator:               '#333',
        Operator.Word:          'bold #000',

        Name.Builtin:           '#36a092',
        Name.Function:          '#4f58db',
        Name.Class:             'bold #4f58db',
        Name.Namespace:         'bold #4f58db',
        Name.Exception:         '#c2324f',
        Name.Variable:          '#996633',
        Name.Constant:          '#003366',
        Name.Label:             '#4f58db',
        Name.Entity:            'bold #38181c',
        Name.Attribute:         '#4f58db',
        Name.Tag:               'bold #36a092',
        Name.Decorator:         '#555555',
        Name.Variable.Magic:    '#3298dc',

        String:                 '#baa44c',
        String.Char:            '#3b3dbe',
        String.Doc:             'italic',
        String.Interpol:        '#AA0000',
        String.Escape:          'bold #CC3300',
        String.Regex:           '#33AAAA',
        String.Symbol:          '#FFCC33',
        String.Other:           '#CC3300',

        Number:             '#FF6600',
        Number.Hex:         '#baa44c',
        Number.Integer:     '#baa44c',

        Generic.Heading:    'bold #003300',
        Generic.Subheading: 'bold #003300',
        Generic.Deleted:    'border:#CC0000 bg:#FFCCCC',
        Generic.Inserted:   'border:#00CC00 bg:#CCFFCC',
        Generic.Error:      '#FF0000',
        Generic.Emph:       'italic',
        Generic.Strong:     'bold',
        Generic.Prompt:     'bold #000099',
        Generic.Output:     '#AAAAAA',
        Generic.Traceback:  '#99CC66',

        Error:              'bg:#FFAAAA #AA0000'
    }