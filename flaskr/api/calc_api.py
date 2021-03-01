from flask_restx import Resource, reqparse, Namespace
import flaskr.calc.holdem_calc as holdem_calc

ns = Namespace('CalcApi', description='Calc Api')


@ns.route("tf/calc")
class CalcApi(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('hand_cards', type=str, required=False, location='args')
    parser.add_argument('board', type=str, required=False, location='args')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parser = reqparse.RequestParser()

    @ns.doc("calc winning rate")
    def get(self):
        args = CalcApi.parser.parse_args()
        board = str.split(args.get('board'), ',')
        hand_cards = str.split(args.get('hand_cards'), ',')
        print(board)
        print(hand_cards)
        return holdem_calc.main(board, hand_cards)
