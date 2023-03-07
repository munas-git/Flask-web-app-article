from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/landing", methods= ["POST", "GET"]) # Endpoint and request methods it will be handling/
def hello_world():

    if request.method == "GET": # Checks if the front end is trying to retreive info
        return render_template("index.html") # Rendering the appropriate html file for the endpoint.
    else:
        # This is a post request meaning the frontend is trying to send data to the server
        # It can also be written as
        #   elif request.method == "POST":        
        # Next lines of code will be for data extraction from frontend.
        first_name = request.form.get("f-name") # Extracting text using get format
        last_name = request.form["l-name"] # Extracting text using regular square bracket format

        print("First name is:", first_name.title())
        print("Last name is:", last_name.title())
        return redirect(url_for("result_page"))


# All methods must be written inside a list otherwise, there will be an error.
# You do not nee to specify any method if the endpoint is performing a GET request alone.
@app.route("/result", methods=["GET"]) # The method for this end point is get alone because the frontend is getting result from server
def result_page():
    return render_template("result.html", full_name = "tom tack")


if __name__ == "__main__":
    app.run()