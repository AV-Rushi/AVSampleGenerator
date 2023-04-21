from flask import Flask, render_template,request,session
import os
import sqlite3
from DemoReadFunction import readFile
from DemoWriteFunction import writeFile
# import logger

app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/',methods=['GET'])
def index():
    config_url = '/configure'
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT TemplateName from template_association")
    tempName = cursor.fetchall()
    return render_template("index.html", config_url=config_url,tempName = tempName)

@app.route('/samplegenerator', methods=['GET', 'POST'])
def samplegenerator():
    selected_value = request.form['selectHK']
    session['selected_value'] = selected_value

    file = request.form.get('selectHK')
    batchNo = request.form.get('batchNo')
    txnNo = request.form.get('txnNo')
    amtType = request.form.get('flexRadioDefault1')
    amount = request.form.get('Amount')
    ccy = request.form.get('ccy')
    ccy1 = request.form.get('ccy1')
    valueDate= request.form.get('valueDate')
    ccyCheck= request.form.get('ccyCheck')
    cdtrDataChoice= request.form.get('flexRadioDefaultCdtr')
    dbtrDataChoice= request.form.get('flexRadioDefaultDbtr')
    cdtrCountry = request.form.get('CdtrCountry')
    cdtrAccountLength= request.form.get('cdtrAccountLength')
    dbtrCountry = request.form.get('DbtrCountry')
    dbtrAccountLength = request.form.get('dbtrAccountLength')
    chkCdtrBic = request.form.get('chkCdtrBic')
    cdtrBic = request.form.get('cdtrBic')
    chkCdtrClrSysId = request.form.get('chkCdtrClrSysId')
    radioCdtrCdPrtry = request.form.get('radioCdtrCdPrtry')
    cdtrCd = request.form.get('cdtrCd')
    cdtrPrtry = request.form.get('cdtrPrtry')
    chkCdtrMmbId = request.form.get('chkCdtrMmbId')
    cdtrMmbId = request.form.get('cdtrMmbId')
    chkCdtrOtherId = request.form.get('chkCdtrOtherId')
    cdtrOtherId = request.form.get('cdtrOtherId')

    chkDbtrBic = request.form.get('chkDbtrBic')
    dbtrBic =  request.form.get('dbtrBic')
    chkDbtrClrSysId = request.form.get('chkDbtrClrSysId')
    radioDbtrCdPrtry = request.form.get('radioDbtrCdPrtry')
    dbtrCd = request.form.get('dbtrCd')
    dbtrPrtry = request.form.get('dbtrPrtry')
    chkDbtrMmbId = request.form.get('chkDbtrMmbId')
    dbtrMmbId = request.form.get('dbtrMmbId')
    chkDbtrOtherId = request.form.get('chkDbtrOtherId')
    dbtrOtherId = request.form.get('dbtrOtherId')

    cdtrAgtDataChoice= request.form.get('flexRadioDefaultCdtrAgt')
    dbtrAgtDataChoice= request.form.get('flexRadioDefaultDbtrAgt')

    readFile(file,int(batchNo),int(txnNo))
    writeFile(file,int(batchNo),int(txnNo),int(amtType),float(amount), ccy, ccy1, valueDate,ccyCheck,int(cdtrDataChoice),int(dbtrDataChoice),int(cdtrAccountLength),int(dbtrAccountLength),chkCdtrBic,cdtrBic,chkCdtrClrSysId,int(radioCdtrCdPrtry),cdtrCd,cdtrPrtry,chkCdtrMmbId,cdtrMmbId,chkCdtrOtherId,cdtrOtherId,chkDbtrBic,dbtrBic,chkDbtrClrSysId,int(radioDbtrCdPrtry),dbtrCd,dbtrPrtry,chkDbtrMmbId,dbtrMmbId,chkDbtrOtherId,dbtrOtherId,int(cdtrAgtDataChoice),int(dbtrAgtDataChoice),cdtrCountry,dbtrCountry)
    os.remove("../Input/Temp/SampleFileDaynamic.xml")
    return ("File Generated !!")


@app.route('/configure', methods=['GET', 'POST'])
def configure():
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
    cursor.execute('SELECT Key,Path FROM template_config where TemplateName=?', (tempNm,))
    data = cursor.fetchall()
    if template == 'Add_New_Format':
        template = ''
    conn.close()
    if request.method == 'POST':
        conn = sqlite3.connect('../DataBase/SampleGenerator.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE template_association SET FileName = ?, BatchTag = ? ,TransactionTag=? WHERE TemplateName = ?",(filename, batchelement, transactionelement, formatname,))
        conn.commit()
        save=request.form.get('save')
        if save=='clicked':
            checkbox_value = request.form.get('checkbox')
            labels = request.form.getlist('labels[]')
            if checkbox_value == 'unchecked':
                labels = request.form.getlist('labels[]')
                cursor.execute("UPDATE template_config SET Required='true' WHERE Required ='false'")
                conn.commit()
                for i in labels:
                    cursor.execute("UPDATE template_config SET Required='false' WHERE FieldName =?", (i,))
                conn.commit()
            conn.close()

            # else:
            #     cursor.execute("UPDATE template_config SET Required='true' WHERE Required ='false'")
            #     conn.commit()
        conn = sqlite3.connect('../DataBase/SampleGenerator.db')
        cursor = conn.cursor()
        if request.method == 'POST':
            labels = request.form.getlist('labels[]')
            current_brnch_ids = request.form.getlist('current_brnch_ids[]')
            new_brnch_ids = request.form.getlist('BrnchId[]')
            if len(labels) == len(current_brnch_ids) == len(new_brnch_ids)and len(labels) > 0:
                for i in range(len(labels)):
                    label = labels[i]
                    current_brnch_id = current_brnch_ids[i]
                    new_brnch_id = new_brnch_ids[i]
                    query = "UPDATE template_config SET Path = ? WHERE FieldName = ? AND Path = ?"
                    cursor.execute(query, (new_brnch_id,label,current_brnch_id))
                    conn.commit()
        if request.method=='POST':
            if 'btnsubmit' in request.form:
                query = "INSERT OR IGNORE INTO template_association (TemplateName, FileName, BatchTag,TransactionTag) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (formatname, filename, batchelement, transactionelement))
                conn.commit()
                conn.close()
    return render_template("configure.html", data=data, template=template, file=file, batchtag=batchtag, txntag=txntag,selected_value=selected_value,keyList=keyList)

@app.route('/add', methods=['GET', 'POST'])
def addValues():
    formatname = request.form.get('formatname')
    conn = sqlite3.connect('../DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        require='true'
        name = request.form.get('newfieldname')
        value = request.form.get('newpath')
        query1 = "INSERT INTO template_config (TemplateName,FieldName,Path,Required) VALUES (?, ?,?,?)"
        cursor.execute(query1, (formatname, name, value, require))
        conn.commit()
    return render_template("configure.html")

if __name__== "__main__":
    app.run(debug=True,port='5523')



