import nose
from PyKomoran.core import *
from PyKomoran.type import *

str_to_analyze = "① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."
komoran = None


def test_to_init_Komoran():
    """
    init Komoran with default model (models_full)
    :return:
    """
    global komoran

    komoran = Komoran(model_path='./models_full')

    assert komoran is not None
    assert komoran._komoran.isInitialized()


def test_to_set_user_dic():
    # TODO: implement test_to_set_user_dic() test code
    pass


def test_to_set_fw_dic():
    # TODO: implement test_to_set_fw_dic() test code
    pass


def test_to_analyze_get_nouns():
    """
    analyze test string with get_nouns() and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    nouns = komoran.get_nouns(str_to_analyze)

    assert isinstance(nouns, list)
    assert len(nouns) == 7
    assert set(nouns) == set(['대한민국', '민주공화국', '대한민국', '주권', '국민', '권력', '국민'])


def test_to_analyze_get_morphes_by_tags():
    """
     analyze test string with get_morphes_by_tags() and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    morphes = komoran.get_morphes_by_tags(str_to_analyze, tag_list=['NNP', 'NNG', 'SF'])

    assert isinstance(morphes, list)
    assert len(morphes) == 9
    assert set(morphes) == set(['대한민국', '민주공화국', '.', '대한민국', '주권', '국민', '권력', '국민', '.'])


def test_to_analyze_get_morphes_by_invalid_tags():
    """
    analyze test string with get_morphes_by_tags(tag_list=['INVALID','POS']) and invalid tag_list and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    morphes = komoran.get_morphes_by_tags(str_to_analyze, tag_list=['NNP', 'NNG', 'SF', 'ABC', '123'])

    assert isinstance(morphes, list)
    assert len(morphes) == 9
    assert set(morphes) == set(['대한민국', '민주공화국', '.', '대한민국', '주권', '국민', '권력', '국민', '.'])


def test_to_analyze_get_morphes_by_no_given_tags():
    """
    analyze test string with get_morphes_by_tags(tag_list=[]) and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    morphes = komoran.get_morphes_by_tags(str_to_analyze, tag_list=[])

    assert isinstance(morphes, list)
    assert len(morphes) == 0
    assert set(morphes) == set([])


def test_to_analyze_get_plain_text():
    """
    analyze test string with get_plain_text() and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    plain_text = komoran.get_plain_text(str_to_analyze)

    assert isinstance(plain_text, str)
    assert len(plain_text) == 156
    assert plain_text == '①/SW 대한민국/NNP 은/JX 민주공화국/NNP 이/VCP 다/EF ./SF ②/SW 대한민국/NNP 의/JKG 주권/NNP 은/JX ' \
                         '국민/NNG 에게/JKB 있/VV 고/EC ,/SP 모든/MM 권력/NNG 은/JX 국민/NNG 으로부터/JKB 나오/VV ㄴ다/EF ./SF'


def test_to_analyze_get_token_list_with_flatten():
    """
    analyze test string with get_token_list(flatten=False,use_pos_name=False) and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    tokens = komoran.get_token_list(str_to_analyze)

    # @formatter:off
    assert isinstance(tokens, list)
    assert len(tokens) == 25
    assert isinstance(tokens[0], Token)
    assert tokens[0] == Token({
                            'morph': '①',
                            'pos': 'SW',
                            'beginIndex': 0,
                            'endIndex': 1
                        })
    assert str(tokens[0]) == '①/SW(0,1)'
    assert tokens[8] == Token({
                            'morph': '대한민국',
                            'pos': 'NNP',
                            'beginIndex': 19,
                            'endIndex': 23
                        })
    assert str(tokens[8]) == '대한민국/NNP(19,23)'
    assert tokens[24] == Token({
                            'morph': '.',
                            'pos': 'SF',
                            'beginIndex': 55,
                            'endIndex': 56
                        })
    assert str(tokens[24]) == './SF(55,56)'
    # @formatter:on


def test_to_analyze_get_token_list_with_flatten_and_use_pos_name():
    """
    analyze test string with get_token_list(flatten=True,use_pos_name=True) and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    tokens = komoran.get_token_list(str_to_analyze, use_pos_name=True)

    # @formatter:off
    assert isinstance(tokens, list)
    assert len(tokens) == 25
    assert isinstance(tokens[0], Token)
    assert tokens[0] == Token({
                            'morph': '①',
                            'pos': 'SW',
                            'beginIndex': 0,
                            'endIndex': 1
                        })
    assert str(tokens[0]) == '①/기타기호(논리수학기호,화폐기호)(0,1)'
    assert tokens[8] == Token({
                            'morph': '대한민국',
                            'pos': 'NNP',
                            'beginIndex': 19,
                            'endIndex': 23
                        })
    assert str(tokens[8]) == '대한민국/고유 명사(19,23)'
    assert tokens[24] == Token({
                            'morph': '.',
                            'pos': 'SF',
                            'beginIndex': 55,
                            'endIndex': 56
                        })
    assert str(tokens[24]) == './마침표,물음표,느낌표(55,56)'
    # @formatter:on


def test_to_analyze_get_token_list_without_flatten():
    """
    analyze test string with get_token_list(flatten=False,use_pos_name=False) and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    tokens = komoran.get_token_list(str_to_analyze, flatten=False)

    # @formatter:off
    assert isinstance(tokens, list)
    assert len(tokens) == 12
    assert isinstance(tokens[0], list)
    assert isinstance(tokens[0][0], Token)
    assert tokens[0][0] == Token({
                            'morph': '①',
                            'pos': 'SW',
                            'beginIndex': 0,
                            'endIndex': 1
                        })
    assert str(tokens[0][0]) == '①/SW(0,1)'
    assert tokens[4][0] == Token({
                            'morph': '대한민국',
                            'pos': 'NNP',
                            'beginIndex': 19,
                            'endIndex': 23
                        })
    assert str(tokens[4][0]) == '대한민국/NNP(19,23)'
    assert tokens[11][2] == Token({
                            'morph': '.',
                            'pos': 'SF',
                            'beginIndex': 55,
                            'endIndex': 56
                        })
    assert str(tokens[11][2]) == './SF(55,56)'
    # @formatter:on


def test_to_analyze_get_token_list_without_flatten_and_use_pos_name():
    """
    analyze test string with get_token_list(flatten=False,use_pos_name=True) and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    tokens = komoran.get_token_list(str_to_analyze, flatten=False, use_pos_name=True)

    # @formatter:off
    assert isinstance(tokens, list)
    assert len(tokens) == 12
    assert isinstance(tokens[0], list)
    assert isinstance(tokens[0][0], Token)
    assert tokens[0][0] == Token({
                            'morph': '①',
                            'pos': 'SW',
                            'beginIndex': 0,
                            'endIndex': 1
                        })
    assert str(tokens[0][0]) == '①/기타기호(논리수학기호,화폐기호)(0,1)'
    assert tokens[4][0] == Token({
                            'morph': '대한민국',
                            'pos': 'NNP',
                            'beginIndex': 19,
                            'endIndex': 23
                        })
    assert str(tokens[4][0]) == '대한민국/고유 명사(19,23)'
    assert tokens[11][2] == Token({
                            'morph': '.',
                            'pos': 'SF',
                            'beginIndex': 55,
                            'endIndex': 56
                        })
    assert str(tokens[11][2]) == './마침표,물음표,느낌표(55,56)'
    # @formatter:on


def test_to_analyze_get_list():
    """
    analyze test string with get_list() and check result is as expected
    :return:
    """
    global komoran
    global str_to_analyze

    pairs = komoran.get_list(str_to_analyze)

    # @formatter:off
    assert isinstance(pairs, list)
    assert len(pairs) == 25
    assert isinstance(pairs[0], Pair)
    assert pairs[0] == Pair({
                            'first': '①',
                            'second': 'SW'
                        })
    assert str(pairs[0]) == '①/SW'
    assert pairs[8] == Pair({
                            'first': '대한민국',
                            'second': 'NNP'
                        })
    assert str(pairs[8]) == '대한민국/NNP'
    assert pairs[24] == Pair({
                            'first': '.',
                            'second': 'SF'
                        })
    assert str(pairs[24]) == './SF'
    # @formatter:on


if __name__ == '__main__':
    nose.runmodule()
