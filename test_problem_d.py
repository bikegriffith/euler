# vim:filetype=python:fileencoding=utf-8

import operator, string
import nose.tools as NT


# Problem D
# Given the list of domains in domains.txt, complete the following tasks:
# 1. Output a file called tlds.txt that contains an alphabetical list of unique tlds in the domains list and the number of occurrences of each, separated by a colon. e.g:
# 2. Assign each domain a score by assigning each letter a numerical value according to its position in the alphabet multiplied by its position in the domain and summing those values. Non-letter characters (such as numbers, hyphens, and periods) are worth nothing. For example:


class TestProblemD(object):

    def setup(self):
        self.domains = load_domains('input/domains.txt')

    def test_solution_1(self):
        result = write_alphabetical_list_of_tlds_with_count(
                        self.domains, 'output/tlds.txt')
        NT.assert_true(result)

    def test_solution_2(self):
        result = write_domain_scores(
                        self.domains, 'output/domain_scores.txt')
        NT.assert_true(result)


def load_domains(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()


def write_alphabetical_list_of_tlds_with_count(domains, filename):
    # Generate count by TLD
    tlds = {}
    for x in domains:
        if (':' in x):
            # TODO: input data had IP/port addresses, skip for now
            continue
        tld = x.split('.')[-1]
        tlds.setdefault(tld, 0)
        tlds[tld] += 1

    # Write output (sorted) to file
    with open(filename, 'w') as f:
        for (tld, count) in sorted(tlds.items()):
            f.write('{0}:{1}\n'.format(tld, count))

    return True


def write_domain_scores(domains, filename):
    # Generate score by domain
    scores = {}
    for x in domains:
        if (':' in x):
            # TODO: input data had IP/port addresses, skip for now
            continue
        scores[x] = score_of(x)

    # Write output (sorted) to file
    with open(filename, 'w') as f:
        sorted_scores = sorted(scores.items(),
                               key=operator.itemgetter(1), #by value, not key
                               reverse=True)
        for (domain, score) in sorted_scores:
            f.write('{0}:{1}\n'.format(domain, score))

    return True


def score_of(domain):
    score = 0
    for i, c in enumerate(domain):
        if c not in string.lowercase:
            continue
        alpha_position = string.lowercase.index(c)
        score += (i + 1) * (alpha_position + 1)
    return score
