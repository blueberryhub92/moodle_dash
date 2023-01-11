from do_not_modify.sql_handler import SQLHandlerFacade
import pandas as pd


class GroupAssessment:
    def __init__(self, app, user):
        self.app = app
        self.user = user

    def operation(self):
        url = 'https://raw.githubusercontent.com/blueberryhub92/moodle-dashboard-backend/main/logs_LA_20__21_20221202-1706.csv'
        df = pd.read_csv(url)

        #  the list of all the enrolled users
        eu = ['anonfirstname31 anonlastname31', 'anonfirstname62 anonlastname62', 'anonfirstname65 anonlastname65',
         'anonfirstname51 anonlastname51', 'anonfirstname66 anonlastname66', 'anonfirstname47 anonlastname47',
         'anonfirstname48 anonlastname48', 'anonfirstname68 anonlastname68', 'anonfirstname59 anonlastname59',
         'anonfirstname64 anonlastname64', 'anonfirstname67 anonlastname67', 'anonfirstname53 anonlastname53',
         'anonfirstname49 anonlastname49', 'anonfirstname55 anonlastname55', 'anonfirstname73 anonlastname73',
         'anonfirstname60 anonlastname60', 'anonfirstname57 anonlastname57', 'anonfirstname70 anonlastname70',
         'anonfirstname63 anonlastname63', 'anonfirstname54 anonlastname54', 'anonfirstname56 anonlastname56',
         'anonfirstname61 anonlastname61', 'anonfirstname69 anonlastname69', 'anonfirstname58 anonlastname58',
         'anonfirstname52 anonlastname52', 'anonfirstname71 anonlastname71', 'anonfirstname72 anonlastname72',
         'anonfirstname21 anonlastname21']

        test_user = self.user
        print(test_user)
        
        default_user = str(63)
        print(default_user)
        return default_user
