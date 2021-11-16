import pytest
import allure
import requests
from data_for_test import DataForTest, levels_all_combination


@pytest.fixture(scope="function")
def SetData():
    TestData = DataForTest() 
    return TestData


def helper_for_levels(SetData, from_level, to_level):
    SetData.set_data_for_test(from_level)   # установить начальные данные пользователя
    res = requests.get(f"{SetData.BASE_URL_API}/rent_level_type", 
                        {'userid': SetData.userid, 'level': to_level, 'type': from_level} 
                        ).json()
    assert res["result"] == 1, "Функция перехода на другой уровень завершилась успешно"
    
    if from_level != to_level:
        assert res["changelevel"] == to_level, "Уровень установлен успешно"
        new_count = str(SetData.active_count - SetData.level_costs[to_level])
        assert res["params"]["active_count"] == new_count, "Средства на активном счете списались правильно"
        new_long = str(SetData.level_longs[to_level])
        assert res["params"]["counter_rent"] == new_long, "Длительность указана правильно"

@allure.feature("API")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест перехода с {from_level} уровня на {to_level} уровень")
@pytest.mark.regress
@pytest.mark.parametrize('from_level,to_level', levels_all_combination)
def test_rent_level_all_combination(SetData, from_level, to_level):
    '''Тестировать переход на другой уровень - все комбинации'''
    helper_for_levels(SetData, from_level, to_level)

@allure.feature("API")
@pytest.mark.smoke
@allure.title("Тест перехода с {from_level} уровня на {to_level} уровень")
@pytest.mark.parametrize('from_level, to_level',  [('1', '5')] )
@allure.severity(allure.severity_level.CRITICAL)
def test_rent_level(SetData, from_level, to_level):
    '''Тестировать переход на другой уровень'''
    helper_for_levels(SetData, from_level, to_level)

@allure.feature("API")
@pytest.mark.smoke
@allure.title("Перевод средств с депозитного счета на активный с параметром {param}")
@pytest.mark.parametrize('param', [17, 1, 0, -5])
@allure.severity(allure.severity_level.CRITICAL)
def test_change_specpoints(SetData, param):
    '''Тестировать перевод средств с депозитного счета на активный'''
    SetData.set_data_for_test(1)   # установить начальные данные пользователя
    res = requests.get(f"{SetData.BASE_URL_API}/change_specpoints", 
                    {'userid': SetData.userid, 'level': 1, 'k': param} 
                    ).json()
    assert res["result"] == 1, "Проверка успешного завершения функции"
    
    delta = param if param>0 else 0
    new_count = str(SetData.active_count + delta)
    assert res["active_count"] == new_count, "Проверка средств на активном счете"
    
    delta = int(SetData.change_active_cost * param / SetData.change_active_count) if param>0 else 0
    new_count = str(SetData.deposit_count - delta)    
    assert res["deposit_count"] == new_count, "Проверка средств на депозитном счете"
