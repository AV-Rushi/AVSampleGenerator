import json

from flask import Flask, render_template, request, session, jsonify,send_file
import os
import sqlite3
from DemoReadFunction import readFile
from DemoWriteFunction import writeFile
import re

# import logger

app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/',methods=['GET','POST'])
def home():
    # config_url = '/configure'
    index_url='/index'
    confighome_url = '/configurationh'
    # conn = sqlite3.connect('DataBase/SampleGenerator.db')
    # cursor = conn.cursor()
    # cursor.execute("SELECT TemplateName from template_association")
    # tempName = cursor.fetchall()
    return render_template("homepage.html",index_url=index_url,confighome_url=confighome_url)

@app.route('/index',methods=['GET','POST'])
def index():
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT TemplateName from template_association")
    tempName = cursor.fetchall()
    return render_template("index.html",tempName = tempName)

@app.route('/configurationh',methods=['GET','POST'])
def configurationh():
    config_url = '/configure'
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT TemplateName from template_association")
    tempName = cursor.fetchall()
    return render_template("configurationh.html",config_url=config_url,tempName = tempName)

@app.route('/config',methods=['GET','POST'])
def config():
    selected_value = request.form['selectHK']
    session['selected_value'] = selected_value
    return render_template("configurationh.html")

@app.route('/samplegenerator', methods=['GET', 'POST'])
def samplegenerator():
    if request.is_json:
        data = request.get_json()
        selected_value = data['templateName']
        session['selected_value'] = selected_value
        file = data['templateName']
        batchNo = data['noOfBatch']
        txnNo = data['noOfTxn']
        amtType = data['amtTypeRadio']
        amount = data['amount']
        ccy = data['intrBkSttlmAmt']
        ccy1 = data['instdAmt']
        valueDate = data['valueDate']
        ccyCheck = data['ccyCheck']
        cdtrDataChoice = data['cdtrDataRadio']
        dbtrDataChoice = data['dbtrDataRadio']
        cdtrCountry = data['cdtrCountry']
        cdtrAccountLength = data['cdtrAccountLength']
        dbtrCountry = data['dbtrCountry']
        dbtrAccountLength = data['dbtrAccountLength']
        chkCdtrBic = data['chkCdtrAgtBic']
        cdtrBic = data['cdtrAgtBIC']
        chkCdtrClrSysId = data['chkCdtrAgtClrSysId']
        radioCdtrCdPrtry = data['CdtrAgtCdPrtryRadio']
        cdtrCd = data['cdtrAgtCd']
        cdtrPrtry = data['cdtrAgtPrtry']
        chkCdtrMmbId = data['chkCdtrAgtMmbId']
        cdtrMmbId = data['cdtrAgtMmbId']
        chkCdtrOtherId = data['chkCdtrAgtOtherId']
        cdtrOtherId = data['cdtrAgtOtherId']

        chkDbtrBic = data['chkDbtrAgtBic']
        dbtrBic = data['dbtrAgtBic']
        chkDbtrClrSysId = data['chkDbtrAgtClrSysId']
        radioDbtrCdPrtry = data['DbtrAgtCdPrtryRadio']
        dbtrCd = data['dbtrAgtCd']
        dbtrPrtry = data['dbtrAgtPrtry']
        chkDbtrMmbId = data['chkDbtrAgtMmbId']
        dbtrMmbId = data['dbtrAgtMmbId']
        chkDbtrOtherId = data['chkDbtrAgtOtherId']
        dbtrOtherId = data['dbtrAgtOtherId']

        cdtrAgtDataChoice = data['CdtrAgtRadio']
        dbtrAgtDataChoice = data['DbtrAgtRadio']

    else:
        selected_value = request.form['templateName']
        session['selected_value'] = selected_value
        file = request.form.get('templateName')
        batchNo = request.form.get('noOfBatch')
        txnNo = request.form.get('noOfTxn')
        amtType = request.form.get('amtTypeRadio')
        amount = request.form.get('amount')
        ccy = request.form.get('intrBkSttlmAmt')
        ccy1 = request.form.get('instdAmt')
        valueDate= request.form.get('valueDate')
        ccyCheck= request.form.get('ccyCheck')
        cdtrDataChoice= request.form.get('cdtrDataRadio')
        dbtrDataChoice= request.form.get('dbtrDataRadio')
        cdtrCountry = request.form.get('cdtrCountry')
        cdtrAccountLength= request.form.get('cdtrAccountLength')
        dbtrCountry = request.form.get('dbtrCountry')
        dbtrAccountLength = request.form.get('dbtrAccountLength')
        chkCdtrBic = request.form.get('chkCdtrAgtBic')
        cdtrBic = request.form.get('cdtrAgtBIC')
        chkCdtrClrSysId = request.form.get('chkCdtrAgtClrSysId')
        radioCdtrCdPrtry = request.form.get('CdtrAgtCdPrtryRadio')
        cdtrCd = request.form.get('cdtrAgtCd')
        cdtrPrtry = request.form.get('cdtrAgtPrtry')
        chkCdtrMmbId = request.form.get('chkCdtrAgtMmbId')
        cdtrMmbId = request.form.get('cdtrAgtMmbId')
        chkCdtrOtherId = request.form.get('chkCdtrAgtOtherId')
        cdtrOtherId = request.form.get('cdtrAgtOtherId')

        chkDbtrBic = request.form.get('chkDbtrAgtBic')
        dbtrBic =  request.form.get('dbtrAgtBic')
        chkDbtrClrSysId = request.form.get('chkDbtrAgtClrSysId')
        radioDbtrCdPrtry = request.form.get('DbtrAgtCdPrtryRadio')
        dbtrCd = request.form.get('dbtrAgtCd')
        dbtrPrtry = request.form.get('dbtrAgtPrtry')
        chkDbtrMmbId = request.form.get('chkDbtrAgtMmbId')
        dbtrMmbId = request.form.get('dbtrAgtMmbId')
        chkDbtrOtherId = request.form.get('chkDbtrAgtOtherId')
        dbtrOtherId = request.form.get('dbtrAgtOtherId')

        cdtrAgtDataChoice= request.form.get('CdtrAgtRadio')
        dbtrAgtDataChoice= request.form.get('DbtrAgtRadio')

    readFile(file,int(batchNo),int(txnNo))
    s1 = writeFile(file,int(batchNo),int(txnNo),int(amtType),float(amount), ccy, ccy1, valueDate,ccyCheck,int(cdtrDataChoice),int(dbtrDataChoice),int(cdtrAccountLength),int(dbtrAccountLength),chkCdtrBic,cdtrBic,chkCdtrClrSysId,int(radioCdtrCdPrtry),cdtrCd,cdtrPrtry,chkCdtrMmbId,cdtrMmbId,chkCdtrOtherId,cdtrOtherId,chkDbtrBic,dbtrBic,chkDbtrClrSysId,int(radioDbtrCdPrtry),dbtrCd,dbtrPrtry,chkDbtrMmbId,dbtrMmbId,chkDbtrOtherId,dbtrOtherId,int(cdtrAgtDataChoice),int(dbtrAgtDataChoice),cdtrCountry,dbtrCountry)
    os.remove("../Input/Temp/SampleFileDaynamic.xml")

    file_path = (f"../Output/{s1}")
    return send_file(file_path, as_attachment=True)

@app.route('/configure', methods=['GET', 'POST'])
def configure():
    validate_url='/validation'
    selected_value = request.args.get('selected_value', None)
    tempNm = selected_value
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Keys from config_keys")
    keyList = cursor.fetchall()
    formatname = request.form.get('formatname')
    filename = request.form.get('filename')
    batchelement = request.form.get('batchelement')
    transactionelement = request.form.get('transactionelement')
    template = ''
    file=''
    batchtag=''
    txntag=''
    cursor.execute(
        'SELECT TemplateName,FileName,BatchTag,TransactionTag FROM template_association where TemplateName=?',
        (tempNm,))
    conf = cursor.fetchall()
    for temp in conf:
        template = temp[0]
        file = temp[1]
        batchtag = temp[2]
        txntag = temp[3]
    cursor.execute('SELECT Key,Path,Required FROM template_config where TemplateName=?', (tempNm,))
    data = cursor.fetchall()
    if template == 'Add_New_Format':
        template = ''
    if request.method == 'POST':
        conn = sqlite3.connect('../DataBase/SampleGenerator.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE template_association SET FileName = ?, BatchTag = ? ,TransactionTag=? WHERE TemplateName = ?",(filename, batchelement, transactionelement, formatname,))
        conn.commit()
    btnsubmit = request.form.get('btnsubmit')
    if btnsubmit == 'submitvalue':
        query = "INSERT OR IGNORE INTO template_association (TemplateName, FileName, BatchTag,TransactionTag) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (formatname, filename, batchelement, transactionelement))
        conn.commit()
    conn.close()
    return render_template("configure.html", data=data, template=template, file=file, batchtag=batchtag, txntag=txntag,selected_value=selected_value,keyList=keyList,validate_url=validate_url)

@app.route('/updateValues', methods=['GET', 'POST'])
def updateValues():
    if request.method == 'POST':
        conn = sqlite3.connect('../DataBase/SampleGenerator.db')
        cursor = conn.cursor()
        pattern = request.form.get('validatekey[]')
        print(pattern)
        checked_labels = request.form.getlist('checked_labels[]')
        unchecked_labels = request.form.getlist('unchecked_labels[]')
        # labels = request.form.getlist('labels[]')
        for label in checked_labels:
            cursor.execute("UPDATE template_config SET Required='true' WHERE FieldName=?", (label,))
            conn.commit()
        for label in unchecked_labels:
            cursor.execute("UPDATE template_config SET Required='false' WHERE FieldName=?", (label,))
            conn.commit()
        conn = sqlite3.connect('../DataBase/SampleGenerator.db')
        cursor = conn.cursor()
        if request.method == 'POST':
            labels = request.form.getlist('labels[]')
            current_brnch_ids = request.form.getlist('current_brnch_ids[]')
            new_brnch_ids = request.form.getlist('BrnchId[]')
            if len(labels) == len(current_brnch_ids) == len(new_brnch_ids) and len(labels) > 0:
                for i in range(len(labels)):
                    label = labels[i]
                    current_brnch_id = current_brnch_ids[i]
                    new_brnch_id = new_brnch_ids[i]
                    query = "UPDATE template_config SET Path = ? WHERE FieldName = ? AND Path = ?"
                    cursor.execute(query, (new_brnch_id, label, current_brnch_id))
                    conn.commit()
        conn.close()
    return render_template("configure.html",value1=checked_labels,value2=unchecked_labels)


@app.route('/add', methods=['GET', 'POST'])
def addValues():
    formatname = request.form.get('formatname')
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        require='true'
        name = request.form.get('newfieldname')
        value = request.form.get('newpath')
        query1 = "INSERT INTO template_config (TemplateName,Key,Path,Required,FieldName) VALUES (?, ?,?,?,?)"
        cursor.execute(query1, (formatname, name, value,require,name))
        conn.commit()
    return render_template("configure.html")

@app.route('/validation', methods=['GET', 'POST'])
def validation():
    selected_value = request.args.get('selected_value', None)
    tempNm = selected_value
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Keys from config_keys")
    keyList = cursor.fetchall()
    cursor.execute('SELECT IdType,path FROM template_config WHERE IdType IS NOT NULL')
    idtype = cursor.fetchall()

    labels = request.form.getlist('labels[]')
    paths = request.form.getlist('path[]')
    patterns = request.form.getlist('Validate[]')
    pattern_str = ''.join(patterns)
    if pattern_str:
        try:
            compiled_pattern = re.compile(pattern_str)
            success_message = 'Valid expression'
            response = {'status': 'success', 'message': success_message}
            with sqlite3.connect('../DataBase/SampleGenerator.db') as conn:
                cursor = conn.cursor()
                for label, path, pattern in zip(labels, paths, patterns):
                    cursor.execute("SELECT * FROM template_config WHERE IdType = ? AND Path = ?", (label, path))
                    row = cursor.fetchone()
                    if row is not None:
                        query = "UPDATE template_config SET RegEx_Pattern = ? WHERE IdType = ? and Path = ?"
                        cursor.execute(query, (pattern, label, path))
                    else:
                        query = "INSERT INTO template_config (IdType,Path,RegEx_Pattern) VALUES(?,?,?)"
                        cursor.execute(query, (label, path, pattern))
                    conn.commit()
        except re.error as e:
            error_message = 'Invalid regex pattern'
            response = {'status': 'error', 'message': error_message,
                        'errors': {f"{i}": str(e) for i, _ in enumerate(patterns)}}
        finally:
            if 'response' not in locals():
                response = {'status': 'success', 'message': 'Valid expression'}
            return jsonify(response)

        # try:
        #     compiled_pattern = re.compile(pattern_str)
        #     success_message = 'Valid expression'
        #     response = {'status': 'success', 'message': success_message}
        #     with sqlite3.connect('../DataBase/SampleGenerator.db') as conn:
        #         cursor = conn.cursor()
        #         for label, path, pattern in zip(labels, paths, patterns):
        #             cursor.execute("SELECT * FROM template_config WHERE IdType = ? AND Path = ?", (label, path))
        #             row = cursor.fetchone()
        #             if row is not None:
        #                 query = "UPDATE template_config SET TempValue = ? WHERE IdType = ? and Path = ?"
        #                 cursor.execute(query, (pattern, label, path))
        #             else:
        #                 query = "INSERT INTO template_config (IdType,Path,TempValue) VALUES(?,?,?)"
        #                 cursor.execute(query, (label, path, pattern))
        #             conn.commit()
        # except re.error:
        #     error_message = 'Invalid regex pattern'
        #     response = {'status': 'error', 'message': error_message}
        # finally:
        #     if 'response' not in locals():
        #         response = {'status': 'success', 'message': 'Valid expression'}
        #     return jsonify(response)

    return render_template('validation.html', selected_value=tempNm, keyList=keyList, idtype=idtype)

@app.route('/addvalidation', methods=['GET', 'POST'])
def addvalidation():
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form.get('newfieldname')
        print(name)
        value = request.form.get('newpath')
        query1 = "INSERT INTO template_config (IdType,Path) VALUES (?, ?)"
        cursor.execute(query1, (name,value))
        conn.commit()
    return render_template("validation.html")

if __name__== "__main__":
    app.run(debug=True,port='5523')



