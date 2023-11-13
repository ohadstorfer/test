from flask import Flask, render_template, request, jsonify

app = Flask(__name__)





import tools.numbers.simp


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/call_simp_add', methods=['POST'])
def call_simp():
    try:
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = tools.numbers.simp.add(num1, num2)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400





@app.route('/call_simp_subtract', methods=['POST'])
def call_simp_subtract():
    try:
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        result = tools.numbers.simp.subtract(num1, num2)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400





@app.route('/call_comp_sum_of_digits', methods=['POST'])
def call_comp_sum_of_digits():

    import tools.numbers.comp 

    try:
        number = int(request.json['number'])
        result = tools.numbers.comp.sum_of_digits(number)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400





@app.route('/call_comp_ispal', methods=['POST'])
def call_comp_ispal():

    import tools.numbers.comp  # noqa

    try:
        number = int(request.json['number'])
        result = tools.numbers.comp.is_palindrome(number)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
import tools.col




@app.route('/call_myzip', methods=['POST'])
def call_myzip():
    try:
        it1 = request.json['it1']
        it2 = request.json['it2']
        
        result = list(tools.col.myzip(it1, it2))
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400












if __name__ == '__main__':
    app.run(debug=True)
