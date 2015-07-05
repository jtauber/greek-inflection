#!/usr/bin/env python3

import yaml

from characters import strip_length

from stemming import Stemmer


TEST_FILES = [
    "tests/pratt.yaml"
]


stemmer = Stemmer("lexicons/pratt.yaml")

for TEST_FILE in TEST_FILES:
    with open(TEST_FILE) as f:
        for test in yaml.load(f):
            lemma = strip_length(test.pop("lemma"))
            test_length = test.pop("test_length", True)
            location = test.pop("location", "")

            for parse, forms in test.items():
                for form in forms.split("/"):
                    norm = strip_length(form)

                    stemmer.stem(location, lemma, parse, norm)

stemmer.counter.results()