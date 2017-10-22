import pytest

from pycantonese.jyutping import parse_jyutping


def test_parse_jyutping_wrong_data_type():
    with pytest.raises(ValueError):
        parse_jyutping(123)


def test_parse_jyutping_syllabic_nasals():
    # TODO assert parse_jyutping('hm4') == [('h', 'm', '', '4')]
    assert parse_jyutping('ng5') == [('', 'ng', '', '5')]
    assert parse_jyutping('m4') == [('', 'm', '', '4')]
    assert parse_jyutping('n3') == [('', 'n', '', '3')]


def test_parse_jyutping_invalid_tone():
    with pytest.raises(ValueError) as e:
        parse_jyutping('lei7')
    assert 'tone error' in str(e.value)


def test_parse_jyutping_no_tone():
    with pytest.raises(ValueError) as e:
        parse_jyutping('lei')
    assert 'tone error' in str(e.value)


def test_parse_jyutping_fewer_than_2_characters():
    with pytest.raises(ValueError) as e:
        parse_jyutping('3')
    assert 'fewer than 2 characters' in str(e.value)


def test_parse_jyutping_invalid_coda():
    with pytest.raises(ValueError) as e:
        parse_jyutping('leil3')
    assert 'coda error' in str(e.value)


def test_parse_jyutping_invalid_nucleus():
    with pytest.raises(ValueError) as e:
        parse_jyutping('sk3')
    assert 'nucleus error' in str(e.value)


def test_parse_jyutping_invalid_onset():
    with pytest.raises(ValueError) as e:
        parse_jyutping('shaa1')
    assert 'onset error' in str(e.value)


def test_parse_jyutping_coda_ng():
    assert parse_jyutping('hoeng1') == [('h', 'oe', 'ng', '1')]


def test_parse_jyutping_no_noda():
    assert parse_jyutping('gaa1') == [('g', 'aa', '', '1')]