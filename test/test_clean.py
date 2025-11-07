"""Test cleanprompt cleaning functions."""

import cleanprompt as cp


def test_clean():
    """Test the clean function."""
    raw_prompt = """

    You are a helpful assistant.
    Please summarize the following text:

    ...text...

    """

    clean = cp.clean(raw_prompt)
    assert clean.startswith("You are")
    assert clean.endswith("...text...")


def test_clean_leading():
    """Test clean_leading function."""
    raw_few_shot = """
        Q: What is 2+2?
        A: 4

        Q: What is the capital of France?
        A: Paris

        Q: Who was the first US president?
        A: """

    clean = cp.clean_leading(raw_few_shot)
    assert clean.startswith("Q: What is 2+2?")
    assert clean.endswith("A: ")
    assert not cp.clean(raw_few_shot).endswith("A: ")


def test_clean_trailing():
    """Test clean_trailing function."""
    raw_prompt = """


    Here begins the epic poem:

    [The model should start writing here]


    """

    clean = cp.clean_trailing(raw_prompt)
    assert not cp.clean(raw_prompt).startswith("\n\n\nHere begins")
    assert clean.startswith("\n\n\nHere begins")
    assert not clean.endswith("\n")
