from flask import Flask, render_template,request,url_for,session, redirect
import ReadFunction
import os
import  sqlite3
app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/',methods=['GET'])
def index():
    config_url = '/configure'
    conn = sqlite3.connect('DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    cursor.execute("SELECT TemplateName from template_association")
    tempName = cursor.fetchall()
    return render_template("index.html", config_url=config_url,tempName = tempName)

@app.route('/shortenurl1', methods=['GET', 'POST'])
def shortenurl1():
    # selected_value = request.form['selectHK']
    # session['selected_value'] = selected_value
    # return redirect(url_for('configure', selected_value=selected_value))

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
    cdtrAccountLength= request.form.get('cdtrAccountLength')
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

    ReadFunction.readFile(file,int(batchNo),int(txnNo),int(amtType),int(amount),ccy,ccy1)
    ReadFunction.writeFile(str(ccy),str(ccy1),valueDate,ccyCheck,int(cdtrDataChoice),int(dbtrDataChoice),int(cdtrAccountLength), int(dbtrAccountLength),chkCdtrBic,cdtrBic,chkCdtrClrSysId,int(radioCdtrCdPrtry),cdtrCd,cdtrPrtry,chkCdtrMmbId,cdtrMmbId,chkCdtrOtherId,cdtrOtherId,chkDbtrBic,dbtrBic,chkDbtrClrSysId,int(radioDbtrCdPrtry),dbtrCd,dbtrPrtry,chkDbtrMmbId,dbtrMmbId,chkDbtrOtherId,dbtrOtherId,int(cdtrAgtDataChoice),int(dbtrAgtDataChoice))
    os.remove("Input\Temp\SampleFile1.xml")
    return "File Generated Successfully"
    # return redirect(url_for('configurl'))
    # return redirect(url_for('configure', selected_value=selected_value))
    # return render_template('shortenurl.html', file=batchNo)

@app.route('/configure', methods=['GET', 'POST'])
def configure():
    # selected_value = session.get('selected_value', None)
    # if selected_value is None:
    #     return 'Selected value not set'
    # else:
    #     return f'The selected value is {selected_value}'
    conn = sqlite3.connect('DataBase/SampleGenerator.db')
    cursor = conn.cursor()
    # cursor.execute("SELECT TemplateName,FileName,BatchTag,TransactionTag FROM template_association where TemplateName=?", (file1,))
    conf = cursor.fetchall()
    for temp in conf:
        template = temp[0]
        file = temp[1]
        batchtag = temp[2]
        txntag = temp[3]
    cursor.execute('SELECT FieldName,Path FROM template_config where TemplateName="HKFPS_PACS008"')
    data = cursor.fetchall()
    return render_template("configure.html", data=data, template=template, file=file, batchtag=batchtag, txntag=txntag)
    # return render_template('shortenurl.html', file=selected_value)
if __name__== "__main__":
    app.run(debug=True,port='2024')


