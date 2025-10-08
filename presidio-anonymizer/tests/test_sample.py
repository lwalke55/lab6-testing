import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # replace the following line with your test
    assert sample_run_anonymizer("My name is Bond.", 11, 15) == "text: My name is BIP.\nitems:\n[\t{'start': 11, 'end': 14, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}\n]"