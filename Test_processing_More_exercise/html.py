templates = {
    'title_open_tag': '<h1>', 'title_close_tag': '</h1>',
    'content_open_tag': '<article>', 'content_close_tag': '</article>',
    'comment_open_tag': '<div>', 'comment_close_tag': '</div>'
}


title = input()
print(f"""{templates['title_open_tag']}
    {title}
{templates['title_close_tag']}""")
content = input()
print(f"""{templates['content_open_tag']}
    {content}
{templates['content_close_tag']}""")
comment = input()
while comment != 'end of comments':
    print(f"""{templates['comment_open_tag']}
    {comment}
{templates['comment_close_tag']}""")
    comment = input()
