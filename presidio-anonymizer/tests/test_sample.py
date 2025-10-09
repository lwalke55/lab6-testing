import pytest
from presidio_anonymizer.sample import sample_run_anonymizer
"""
@pytest.mark.parametrize(
        #fmt: off
        'text,start,end',
        [
            ("My name is Bond.",11,15,),
        ],
)
"""
def test_sample_run_anonymizer():
    # replace the following line with your test
    result = sample_run_anonymizer("My name is Bond.",11,15)
    assert result.text == "My name is BIP."
    assert len(result.text) == len ("My name is BIP.")
    assert result.items[0].start == 11
    assert result.items[0].end == 14