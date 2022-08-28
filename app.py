from first_flask import create_app

app= create_app()

if __name__=='__main__':
    # app.run(debug=True)
    app.run(debug=False)

# from second_flask import create_app
#
# app=create_app()
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5609)