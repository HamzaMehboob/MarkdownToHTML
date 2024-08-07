import markdown_to_html


sample_markdown = """
# Sample Markdown File

This is a sample Markdown file to demonstrate various Markdown features.

## Headings

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

*Italic* and **bold** text.

### Links
[GitHub](https://github.com/)

### Images
![OpenAI Logo](https://github.com/images/modules/search/mona-love.png)

### Lists
* Item 1
* Item 2

1. Item 1
2. Item 2

### Blockquote
> This is a blockquote.

### Code
`inline code`
"""

html_output = markdown_to_html.markdown_to_html(sample_markdown)
print(html_output)