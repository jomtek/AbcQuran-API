from flask import Flask, render_template, request
app = Flask(__name__)

def replace_line(file_name, line_num, text):
	with open(file_name, "r") as txt:
		lines = txt.readlines()
		lines[line_num] = text + "\n"
		with open(file_name, "w") as txt:
			txt.writelines(lines)

@app.route('/contribute')
def contribute():
	reciter_id = request.args.get("reciter")
	sura_num = int(request.args.get("sura"))
	verse_num = int(request.args.get("cursor"))
	new_timecode = int(request.args.get("timecode"))
	padded_sura_num = str(sura_num).zfill(3)

	fn = f"./reciters/{reciter_id}/timecodes/{padded_sura_num}.txt"
	replace_line(fn, verse_num, str(new_timecode))
	return {"response": 200}

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int("5000"), debug=True)
