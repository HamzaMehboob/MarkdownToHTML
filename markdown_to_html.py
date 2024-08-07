import re

def markdown_to_html(markdown_text):
    html_output = []

    # Convert headings
    markdown_text = re.sub(r'###### (.*)', r'<h6>\1</h6>', markdown_text)
    markdown_text = re.sub(r'##### (.*)', r'<h5>\1</h5>', markdown_text)
    markdown_text = re.sub(r'#### (.*)', r'<h4>\1</h4>', markdown_text)
    markdown_text = re.sub(r'### (.*)', r'<h3>\1</h3>', markdown_text)
    markdown_text = re.sub(r'## (.*)', r'<h2>\1</h2>', markdown_text)
    markdown_text = re.sub(r'# (.*)', r'<h1>\1</h1>', markdown_text)

    # Convert bold and italic text
    markdown_text = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', markdown_text)
    markdown_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown_text)
    markdown_text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown_text)
    
    # Convert inline code
    markdown_text = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown_text)

    # Convert links
    markdown_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown_text)

    # Convert images
    markdown_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', markdown_text)

    # Convert unordered lists
    markdown_text = re.sub(r'^\* (.*)', r'<ul>\n<li>\1</li>\n</ul>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'</ul>\n<ul>', r'', markdown_text)  # Remove extra ul tags

    # Convert ordered lists
    markdown_text = re.sub(r'^\d+\. (.*)', r'<ol>\n<li>\1</li>\n</ol>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'</ol>\n<ol>', r'', markdown_text)  # Remove extra ol tags

    # Convert blockquotes
    markdown_text = re.sub(r'^> (.*)', r'<blockquote>\1</blockquote>', markdown_text, flags=re.MULTILINE)

    # Convert horizontal rules
    markdown_text = re.sub(r'^---$', r'<hr>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^\*\*\*$', r'<hr>', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'^___$', r'<hr>', markdown_text, flags=re.MULTILINE)

    # Convert code blocks
    markdown_text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', markdown_text, flags=re.DOTALL)

    # Convert paragraphs
    lines = markdown_text.split('\n')
    in_paragraph = False
    for line in lines:
        if line.strip():
            if not in_paragraph:
                html_output.append('<p>')
                in_paragraph = True
            html_output.append(line)
        else:
            if in_paragraph:
                html_output.append('</p>')
                in_paragraph = False
    if in_paragraph:
        html_output.append('</p>')

    return ''.join(html_output)

