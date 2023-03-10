from do_not_modify.sql_handler import SQLHandlerFacade
import pandas as pd


class GroupAssessment:
    def __init__(self, app):
        self.app = app

    def operation(self):
        #print(self.user)
        handler = SQLHandlerFacade(app=self.app, query="SELECT * FROM mdl_quiz_grades")
        operation_result, pd_dataframe = handler.operation()
        # print(handler)
        # # Work with pandas.
        # print(pd_dataframe.head())
        # print(pd_dataframe["id"])
        # print(pd_dataframe.loc[:5, ["id", "grade"]])
        # print(pd_dataframe.iloc[0])
        # print(pd_dataframe[pd_dataframe["grade"] == '8.50000'])
        # print(pd_dataframe[pd_dataframe["timemodified"].isin([1577442881, 1577442882])])
        # Work with json data.
        data = operation_result.get("result")
        return operation_result