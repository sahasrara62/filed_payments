from flask import Blueprint, request, abort, jsonify
import json
from application.services.payment import Card, ExternalPayment

blueprint = Blueprint("views", __name__, url_prefix="/")


@blueprint.route("/ProcessPayment", methods=["POST"])
def payment():

    if request.method == "POST":
        # getting the request data, which is send in request body as json
        data = request.get_data(as_text=True)
        # checking if there is any input data present or not, if not then throw bad request
        if not data:
            abort(400)
        # loading the data into json format
        request_data = json.loads(data)

        # loading the card object, to check the request data is same as the input data
        card_data = Card()
        print("request data {}".format(request_data))
        try:
            # verifying all the request data input whether they follow all the criteria or not
            # note assumption, date format is taken as %y:%m:%d as opposed to %m:%d in credit cards
            if not card_data.verify_input(**request_data):
                print("card data invalid")
                abort(400)
        except:
            abort(400)
        try:
            # payment procedure begins
            print("payment status started")
            payment_status = ExternalPayment(card_data.Amount, card_data)
            print("payment process started")
            # begin of payment process, starting from make connection, authenticate the user, made payment
            # will provide result if the transaction is sucessfull or not.

            payment_sccessfull = payment_status.make_payment()
            # checking the transaction status, if it is successful or not.
            if payment_sccessfull:
                return {"status code": 200}, 200
            else:
                abort(400)
        except:
            abort(500)
    else:
        abort(400)
