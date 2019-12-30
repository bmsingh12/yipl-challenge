import mysql.connector, requests, operator
import pandas as pd


class Report:
    def __init__(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="bmsingh",
            database="yipl")

        self.mycursor = self.my_db.cursor()
        self.api = "https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json"
        self.l_o_d = []

    def loadData(self):
        """
        Loads the data from the API.
        :return:
        """
        return requests.get(self.api).json()

    def insertDataToDB(self):
        """
        Insert data to MySQL db using execute method.
        :return:
        """
        sql = "INSERT INTO yipl.challenge(year, petroleumProduct, sale) VALUES (%s, %s, %s)"
        for values in self.loadData():  # doubt
            self.mycursor.execute(sql, [values["year"], values["petroleum_product"], values["sale"]])

    def fetchDataFromDB(self):
        """
        imp:: install mysql.connector using "pip3 install mysql-connector-python" (for python 3)

        This method fetches the data previously loaded to our db as a list of tuples.
        :return:
        """
        fetch_data_from_db_query = "select * from yipl.challenge"
        self.mycursor.execute(fetch_data_from_db_query)
        result = list(self.mycursor.fetchall())
        self.my_db.commit()

        return result

    def convert(self, tup):
        """
        A function  to convert list of tuple's to a list of dict with required keys.

        :param tup: take a list of tuples
        :return: list of dictionaries with keys:
                    -- year
                    -- petroleum_product
                    -- sale
        """
        for x in tup:
            self.l_o_d.append({"year": x[0], "petroleum_product": x[1], "sale": x[2]})
        return self.l_o_d

    def add_four_years(self, year):
        """
        Method to add 4 years to current year.
        :param year: int year
        :return: year + 4; e.g., 2000 + 4 = 2004
        """
        return year + 4

    def generateResult(self):
        """
        1. This method converts data from db to a list of dictionary's.
        2. Sorts the list of dicts using operator.itemgetter(arg) method [sorted w.r.t. 'petroleum_product'] for ease
            of use.
        3. gets the Petroleum Product list, Start Year and End Year from our data.
        4. Consists logic for storing list of dict for the years: 2000 - 2004, 2005 - 2009 and 2010 - 2014.
            4.1. checks of data lies between the range of date.
            4.2. checks of data and petroleum_product match.
            4.3. check if value of sale is '0' then returns that object as an empty dict.

                If all the above conditions are TRUE, the dict is added to a new list 's'.
        5. A new dictionary 'd1' has been created to store the new table data with the following columns:
            - Product
            - Year
            - Min
            - Max
            - Avg
        6. All these new dict columns are stored in the list 'final_list'.
        7. Finally, the list 'final_list' is sorted w.r.t. 'petroleum_product' using operator.itemgetter(arg) method.

        :return: list of all the data with minimum, maximum and average data (filtered 0 for the case of min)
        """
        self.convert(self.fetchDataFromDB()).sort(key=operator.itemgetter('petroleum_product'))
        pp_list = sorted(list(set([x['petroleum_product'] for x in self.convert(self.fetchDataFromDB())])))
        start_year = int(min([x['year'] for x in self.convert(self.fetchDataFromDB())]))
        end_year = int(max([x['year'] for x in self.convert(self.fetchDataFromDB())]))

        # set modified date (in year)
        modified_year = int()

        #  list to store sale values of all pp
        s = []

        # an empty dictionary to store key value of required result table
        d1 = {}

        # consider as final list to store all dictionaries d1
        final_list = []

        for p in pp_list:
            for x in self.convert(self.fetchDataFromDB()):
                if start_year <= int(x['year']) <= self.add_four_years(start_year):
                    if x['petroleum_product'] == p:
                        if x['sale'] == 0:
                            x = {}
                        else:
                            s.append(x['sale'])
            d1['Product'] = p
            d1['Year'] = str(start_year) + "-" + str(self.add_four_years(start_year))
            d1['Min'] = 0 if s == [] else min(s)
            d1['Max'] = 0 if s == [] else max(s)
            d1['Avg'] = (sum(s) / len(s)) if s != [] else 0
            final_list.append(d1)
            s = []
            d1 = {}

        # plus 4 years added
        modified_year = self.add_four_years(start_year) + 1

        # logic for year (2000 - 2004)
        for p in pp_list:
            for x in self.convert(self.fetchDataFromDB()):
                if modified_year <= int(x['year']) <= self.add_four_years(modified_year):
                    if x['petroleum_product'] == p:
                        if x['sale'] == 0:
                            x = {}
                        else:
                            s.append(x['sale'])
            d1['Product'] = p
            d1['Year'] = str(modified_year) + "-" + str(end_year)
            d1['Min'] = 0 if s == [] else min(s)
            d1['Max'] = 0 if s == [] else max(s)
            d1['Avg'] = (sum(s) / len(s)) if s != [] else 0
            final_list.append(d1)
            s = []
            d1 = {}

        # plus 4 years added
        modified_year = self.add_four_years(modified_year) + 1

        # logic for year (2000 - 2004)
        for p in pp_list:
            for x in self.convert(self.fetchDataFromDB()):
                if modified_year <= int(x['year']) <= self.add_four_years(modified_year):
                    if x['petroleum_product'] == p:
                        if x['sale'] == 0:
                            x = {}
                        else:
                            s.append(x['sale'])
            d1['Product'] = p
            d1['Year'] = str(modified_year) + "-" + str(self.add_four_years(modified_year))
            d1['Min'] = 0 if s == [] else min(s)
            d1['Max'] = 0 if s == [] else max(s)
            d1['Avg'] = (sum(s) / len(s)) if s != [] else 0
            final_list.append(d1)
            s = []
            d1 = {}

        final_list.sort(key=operator.itemgetter('Product'))
        return final_list

    def generateTable(self, insert=False):
        """
        This method generates a tabular view using the pandas library.
        This method also gives an option to insert the data fetched from the API to db.

        If 'insert=False' , then data is not inserted
        If 'insert=True' , then data will be inserted

            (This has been done because the data needs to be inserted only once)

        :return:
        """
        if insert == False:
            df = pd.DataFrame(self.generateResult())
            print(df)
        else:
            self.insertDataToDB()
            df = pd.DataFrame(self.generateResult())
            print(df)


report = Report()
report.generateTable(False)
