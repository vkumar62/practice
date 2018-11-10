'''
Given a list of Contacts, where each contact consists of a contact ID and a list of email IDs. Output a unique list of contacts by removing duplicates. Two contacts are considered to be the same, if they share at least one email ID.
'''
class Contact:
    def __init__(self, id, emails):
        self.id = id
        self.emails = list(emails)

def rem_duplicates(contacts):
    uniqs = set()
    email2id = dict()

    for contact in contacts:
        is_uniq = True
        for email in contact.emails:
            if email in email2id and email2id[email] is not contact:
                uniqs.discard(email2id[email])
                is_uniq = False
            else:
                email2id[email] = contact
        if is_uniq:
            uniqs.add(contact)

    return uniqs


def verify(contacts, uniqs):
    emails = set()

    for contact in uniqs:
        for email in contact.emails:
            assert email not in emails, pdb.set_trace()
            emails.add(email)
    # Now verify the dups

    for i in range(len(contacts)):
        contact = contacts[i]
        if contact in uniqs:
            continue

        #At least one email of this contact should be with someone else
        found = False
        for email in contact.emails:
            for j in range(len(contacts)):
                if i == j or contacts[j] in uniqs:
                    continue
                if email in contacts[j].emails:
                    found = True
                    break
            if found:
                break
        assert found, pdb.set_trace()

import random
def create_contacts(N, email_count, email_range = 100000000):
    contacts = []
    for i in range(N):
        emails = random.sample(range(email_range), email_count)
        contacts.append(Contact(i, emails))
    random.shuffle(contacts)
    return contacts

import pdb
random.seed(1234)
contacts = create_contacts(100, 100)
uniqs = rem_duplicates(contacts)
print(len(contacts), len(uniqs))
verify(contacts, uniqs)
