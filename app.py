from flask import Flask,render_template,jsonify


#app is the instance of the class Flask
app = Flask(__name__) 

#route is simply used for registring a part of the url that comes after domain name
#only "/" means empty path or the first page
JOBS = [
    
            {
                'id':1,
                'title':'Data Analyst',
                'location':'pune',
                'salary':'100000'
            },

            {
                'id':2,
                'title':' Research Analyst',
                'location':'pune',
                'salary':'10000'
            }

        ]


@app.route("/")
def hello_world():

    #render template is used for rendering the html pages
    return render_template('home.html',jobs = JOBS)


@app.route("/jobs")
def list_jobs():

    #render template is used for rendering the html pages
    return jsonify(JOBS)


if __name__ == "__main__":
    
    app.run()
    # app.run(host = '0.0.0.0' , debug =  True )