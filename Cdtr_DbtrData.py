import sqlite3
from faker import Faker
fake = Faker()

conn = sqlite3.connect('DataBase/SampleGenerator.db')  # Connect to the database
cur = conn.cursor()  # Create a cursor object

cur.execute('SELECT AccountNumber,AccountName FROM account_info')
AccountData = cur.fetchall()

Acc_no = [temp[0] for temp in AccountData]
Acc_name = [temp[1] for temp in AccountData]

def existingAccountNo(count,AccountNo1):
    for AccNo in AccountNo1:
        if (count < len(AccountData)):
            AccNo.text = str(Acc_no[count])
            count = count + 1

        else:
            count = 0
            AccNo.text = str(Acc_no[count])
            count = count + 1

def existingAccountName(count,AccountNm1):
    for AccNm in AccountNm1:
        if (count < len(AccountData)):
            AccNm.text = str(Acc_name[count])
            count = count + 1

        else:
            count = 0
            AccNm.text = str(Acc_name[count])
            count = count + 1

def DummyAccountNo(cdtrAccountLength,AccountNo1):
    for AccNo in AccountNo1:
        account_no = fake.random_number(digits=cdtrAccountLength)
        AccNo.text = str(account_no)


def DummyAccountNm(Country,AccountNm1):
    for AccNm in AccountNm1:
        country = Faker(f"en_{Country}")
        name = country.name()
        AccNm.text = str(name)