msg_template = """Hello {name},
Thank you for joining {website}. We are very happy to have you with us.
"""

def format_msg(my_name="Loc", my_website="fabico.vn"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg