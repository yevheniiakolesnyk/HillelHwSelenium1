def test_title(incognito):
    assert incognito.title == 'Google'


def test_title_1(headless):
    assert headless.title == 'Google'
