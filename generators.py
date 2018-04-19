"""
    Dummy csv generator
"""
import unidecode

from random import randint, choice


EMAIL_DOMAINS = [
    (60, 'gmail.com'),
    (90, 'hotmail.com'),
    (100, 'mailinator.com')
]
EMAIL_TEMPLATES = [
    '{name}{lastname[0]}@{domain}',
    '{name[0]}{lastname}@{domain}',
    '{name}{lastname}@{domain}',
    '{name}.{lastname}@{domain}',
    '{name}{number}@{domain}',
    '{lastname[0]}{name}{number}@{domain}',
]


def add_new_column(header, rows, column_name, column_generator):
    """
        Add new column with generator
    """
    updated_rows = []
    for row in rows:
        mutable_row = list(row)
        mutable_row.append(column_generator(row))
        updated_rows.append(mutable_row)
    mutable_header = list(header)
    mutable_header.append(column_name)
    return mutable_header, updated_rows


def get_random_email_domain():
    """
        Return random email domain
    """
    random = randint(0, 100)
    for domain in EMAIL_DOMAINS:
        if random <= domain[0]:
            return domain[1]
    return None


def get_random_mail_template():
    """
        Return random mail template
    """
    return choice(EMAIL_TEMPLATES)


def email_generator(row):
    """
        Email generator
    """
    [name, lastname, *_] = row
    template = get_random_mail_template()
    mail = template.format(
        name=name,
        number=randint(1, 1000),
        lastname=lastname,
        domain=get_random_email_domain()
    )
    mail_unaccent = unidecode.unidecode(mail.lower())
    return mail_unaccent
