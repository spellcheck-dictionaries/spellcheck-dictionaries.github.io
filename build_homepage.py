#!/usr/bin/python

import os

htmlheader = """
<!DOCTYPE html>
<html>
<head>
    <title>Spell-check Dictionaries</title>
</head>
<body>
    <div style="max-width: 700px; margin: 20px auto">
    <h1>Spell-check Dictionaries</h1>
    <p>Original source from: </p>
    <pre>
        <code>
            git clone https://chromium.googlesource.com/chromium/deps/hunspell_dictionaries
        </code>
    </pre>
    <p>
        This GitHub page is implemented for spellcheck feature of Githuber MD, a WordPress <a href="https://markdown-editor.github.io/">Markdown</a> plugin.
    </p>
    <ul>
        <li><a href="https://github.com/terrylinooo/githuber-md" title="Markdown editor">https://github.com/terrylinooo/githuber-md</a> (GitHub project)</li>
        <li><a href="https://wordpress.org/plugins/wp-githuber-md/" title="Markdown editor">https://wordpress.org/plugins/wp-githuber-md/</a> (WordPress plugin)</li>
    </ul>
    <h2>How to Use</h2>
    <pre>
        <code>
            https://spellcheck-dictionaries.github.io/{lang_code}/{lang_code}.dic
            https://spellcheck-dictionaries.github.io/{lang_code}/{lang_code}.aff
        </code>
    </pre>
    <h2>Support Languages</h2>
    <div>
        <table border="1" cellspacing="3" cellpadding="5" width="100%" style="border: 1px #dddddd solid">
            <tr>
                <th>Language code</th><th>URL</th>
            </tr>
"""

htmlfooter = """
        </table>
        <p>Created by <a href="https://terryl.in">Terry L.</a>, a programmer from Taiwan.</p>
    </div>
</body>
</html>
"""

fo = open('index.html', 'w')

content = htmlheader

for dirname, dirnames, filenames in os.walk('.'):
    # print path to all subdirectories first.
    if '.git' in dirnames:
        dirnames.remove('.git')


    for subdirname in dirnames:
        path = os.path.join(dirname, subdirname)
        langcode = path.replace('./', '')
        url_dic = 'https://spellcheck-dictionaries.github.io/' + langcode + '/' + langcode + '.dic'
        url_aff = 'https://spellcheck-dictionaries.github.io/' + langcode + '/' + langcode + '.aff'
        content = content + '<tr><td>' + langcode + '</td>'
        content = content + '<td>' + url_dic + '<br />' + url_aff + '</td>'

content = content + htmlfooter

fo.write(content)

