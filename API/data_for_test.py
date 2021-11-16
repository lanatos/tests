import requests

levels_all_combination = []
for i in range(6): 
    for j in range(6):
        levels_all_combination.append( ( str(i), str(j) ) ) 

class DataForTest():
    '''Параметры пользователя для тестирования'''

    def __init__(self):
        self.BASE_URL_DATA = "http://backend/admin/createbase1"
        self.BASE_URL_API = "http://backend/allf"
        self.level_longs = {"0":0, "1":6, "2":7, "3":8, "4": 9, "5":10}
        self.level_costs = {"0":0, "1":16, "2":17, "3":18, "4": 19, "5":20}
        self.change_active_count = 10
        self.change_active_cost = 13
        self.userid = 1
        self.active_count = 1000
        self.safe_count = 2000
        self.deposit_count = 33000

    def set_data_for_test(self,level):
        '''Установить параметры пользователя в веб-приложении для тестирования'''
        set_data = requests.get( self.BASE_URL_DATA, {'user_level': level} )