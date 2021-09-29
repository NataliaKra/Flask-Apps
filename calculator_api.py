# import Flask and jsonify
from flask import Flask, jsonify

# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

class Add (Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create arguments 'a' and 'b' 
        
        parser.add_argument('a', type=float)
        parser.add_argument('b', type=float)

        # parse 'a' and 'b'
        args = parser.parse_args()
        a = args.get('a')
        b = args.get('b')
        
        result = a + b
                
        return result
    
class Substract (Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create arguments 'a' and 'b' 
        
        parser.add_argument('a', type=float)
        parser.add_argument('b', type=float)

        # parse 'a' and 'b'
        args = parser.parse_args()
        a = args.get('a')
        b = args.get('b')
        
        result = a - b
               
        return result

class Multiply (Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create arguments 'a' and 'b' 
        
        parser.add_argument('a', type=float)
        parser.add_argument('b', type=float)

        # parse 'a' and 'b'
        args = parser.parse_args()
        a = args.get('a')
        b = args.get('b')
        
        result = a * b
                
        return result

class Divide (Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create arguments 'a' and 'b' 
        
        parser.add_argument('a', type=float)
        parser.add_argument('b', type=float)

        # parse 'a' and 'b'
        args = parser.parse_args()
        a = args.get('a')
        b = args.get('b')
        
        if b!=0:
            result = a / b
        else:
            result = 'Zero division error'
                
        return result
    
# assign endpoint
api.add_resource(Add, '/add')
api.add_resource(Substract, '/substract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)

