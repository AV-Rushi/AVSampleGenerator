import sqlite3
import time
import xml.etree.ElementTree as ET
from faker import Faker
import uuid
import datetime


def readFile(file, batchNo, txnNo):
    conn = sqlite3.connect('DataBase/SampleGenerator.db')  # Connect to the database
    cur = conn.cursor()  # Create a cursor object
    cur.execute('SELECT FileName FROM template_association where TemplateName=?', (file,))
    FileName = cur.fetchone()
    file1 = (f"Input\Sample_Template\{FileName[0]}")
    tree = ET.parse(file1)

    ns = dict([node for (_, node) in ET.iterparse(file1, events=['start-ns'])])
    nskeys = list(ns.keys())
    for i in nskeys:
        ET.register_namespace(i, ns[i])
    root = tree.getroot()

    cur.execute('SELECT BatchLevel, BatchTag,TransactionLevel,TransactionTag FROM template_association where TemplateName=?', (file,))
    Data = cur.fetchall()

    BatchLevel = Data[0][0]
    BatchTag = Data[0][1]
    TransactionLevel = Data[0][2]
    TransactionTag = Data[0][3]

    if txnNo>0:
        if TransactionTag is not None:
            TransactionLevelElement = root.find(f".//{TransactionLevel}", ns)  # Transaction Level Element
            for j in range(txnNo - 1):
                txnElement = root.find(f".//{TransactionTag}", ns)    # CdtTrfTxInf Element
                TransactionLevelElement.append(txnElement)

    elif txnNo==0:
        txnElement = root.find(f".//{TransactionTag}", ns)
        for elem in root.findall(".//*"):
            if txnElement in elem:
                elem.remove(txnElement)
        print("Txn Removed")

    if batchNo>0:
        if BatchTag is not None:
            BatchLevelElement = root.find(f".//{BatchLevel}", ns)  # Batch Level Element
            for i in range(batchNo - 1):
                batchElement = root.find(f".//{BatchTag}", ns)  # Batch Element
                BatchLevelElement.append(batchElement)
    elif batchNo==0:
        batchElement = root.find(f".//{BatchTag}", ns)
        for elem in root.findall(".//*"):
            if batchElement in elem:
                elem.remove(batchElement)
        print("Batch Removed")

    tree.write("Input\Temp\SampleFileDaynamic.xml", xml_declaration=True, encoding='utf-8')
    time.sleep(5)


readFile('HKFPS_PACS003',5, 4)
# readFile('RTP_PACS008',5, 4, 1, 35684, 'HKD', None)
# readFile('Demo',3, 5, 1, 35684, 'HKD', None)