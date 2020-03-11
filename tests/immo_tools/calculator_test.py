from immo_tools.calculator import convert_rate_per_month


def test_convert_rate_per_month():
    res = convert_rate_per_month(.015)
    assert res == (1.015 ** (1 / 12)) - 1, 'should have nb_per=12'


def test_convert_rate_per_month_with_custom_period():
    res = convert_rate_per_month(.015, 6)
    assert res == (1.015 ** (1 / 6)) - 1, 'should have nb_per=6'
