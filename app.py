from flask import Flask, request, render_template
from src.pipeline.prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home_page():
    """
    Render the home page template.

    Returns:
        Rendered home page template.
    """
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    """
    Handle prediction requests.

    Returns:
        Rendered result template with the prediction.
    """
    if request.method == "GET":
        # Render form template for GET requests
        return render_template("form.html")
    else:
        # Extract data from form submission
        data = CustomData(
            carat=float(request.form.get("carat")),
            depth=float(request.form.get("depth")),
            table=float(request.form.get("table")),
            x=float(request.form.get("x")),
            y=float(request.form.get("y")),
            z=float(request.form.get("z")),
            cut=request.form.get("cut"),
            color=request.form.get("color"),
            clarity=request.form.get("clarity")
        )
        
        # Convert data to DataFrame
        final_data = data.get_data_as_dataframe()

        # Use prediction pipeline to predict
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)

        # Round prediction to two decimal places
        result = round(pred[0], 2)

        # Render result template with prediction
        return render_template("result.html", final_result=result)

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=8000)
