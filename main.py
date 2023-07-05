from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
import engine as en


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["OUTPUT_FOLDER"] = "outputs/"

default_prompt = en.config["DefaultPrompt"]


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/outputs/<filename>")
def output_file(filename):
    return send_from_directory(app.config["OUTPUT_FOLDER"], filename)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")

        if not file:
            return render_template("upload.html", prompt=default_prompt)

        if file:
            prompt_text = request.form.get('promptbox')
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            processed_name, detected_texts = en.execute(filepath, prompt_text)
            processed_filepath = os.path.join(
                app.config["OUTPUT_FOLDER"], processed_name
            )

            return render_template(
                "display.html",
                orig_image=filepath,
                proc_image=processed_filepath,
                texts=detected_texts,
            )
    return render_template("upload.html", prompt=default_prompt)




if __name__ == "__main__":
    app.run(debug=True)
