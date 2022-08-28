from flask import Flask,redirect,url_for

student=Flask(__name__)


# @student.route('/score/<int:marks>')
# def p(marks):
#     if marks >= 60:
#         return"You are pass and eligible for next clss %d" %marks
#     else:
#         return "Sorry ,you are fail and you got %d marks " %marks

@student.route('/school')
def school():
    return 'student is studying in school'

@student.route('/old')
def old_age():
    return 'He is leaving with family '

@student.route('/clg')
def clg():
    return 'student studying in college'

@student.route('/student/<int:age>')
def person(age):
    if (age >= 20) and (age <=30) :
        return redirect(url_for('clg'))
    elif age >= 30:
        return redirect(url_for('old_age'))    ### use function name here old_agew
    else:
        return redirect(url_for('school'))

if __name__=='__main__':
    student.run(debug=True, port=8900)
