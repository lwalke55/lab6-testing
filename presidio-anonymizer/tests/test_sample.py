import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

@pytest.mark.parametrize(
        #fmt: off
        'text,start,end',
        [
            ("My name is Bond.",11,15,),
        ],
)

def test_sample_run_anonymizer(text,start,end):
    # replace the following line with your test
    assert sample_run_anonymizer(text,start,end).text == "My name is BIP."
    assert sample_run_anonymizer(text,start,end).items[0].start == 11
    assert sample_run_anonymizer(text,start,end).items[0].end == 14
    #assert sample_run_anonymizer(text,start,end) == "text: My name is BIP.\nitems:\n[\t{'start': 11, 'end': 15, 'entity_type': 'PERSON', 'text': 'BIP', 'operator': 'replace'}\n]"