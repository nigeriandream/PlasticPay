from django.shortcuts import render
from web3 import Web3
from django.http import JsonResponse
from eth_account import Account
from inspect import Traceback
import traceback
import dotenv
import os


# Load .env variables
config = dotenv.dotenv_values(".env")

w3 = Web3(Web3.HTTPProvider(config["httpProvider"]))
contract_address = config["plasticpay_address"]
contract_abi = config["plasticpay_abi"]

# Load contract
PlasticPay_contract = w3.eth.contract(address=contract_address, abi=contract_abi)


def connect_wallet(request):
    try:
        if request.method == "POST":
            ethereum_address = request.POST.get("ethereum_address")

            # Process the address as needed, on the frontend print the wallet address
            # e.g., save it to the database, perform additional actions, etc.

            # Redirect or render a response as desired
        return render(
            request, "connect_wallet.html", {"ethereum_address": ethereum_address}
        )

    # Handle invalid requests or other HTTP methods
    # return render(request, 'invalid_request.html')
    except Exception as e:
        print(f"Error: {e}")


# Display connected wallet address
def get_connect_wallet():
    # check if wallet is connected
    if not w3.isConnected():
        raise Exception("No wallet connected")
    # get current selected metamask wallet
    user_wallet = w3.eth.accounts
    if not user_wallet:
        raise Exception("No account found")
    return user_wallet[0].lower()


# Get all items ever recycled by users
def totalItemsRecycled(request):
    try:
        result = PlasticPay_contract.functions.recycled_items().call
        return JsonResponse({"success": True, "Total_items_recycled": result})
    except Exception as e:
        print(f"Error: {e}")


# get total rewards recieved by user and current items recycled
def user_reward(request):
    try:
        result = PlasticPay_contract.functions.myreward().call
        return JsonResponse({"success": True, "user_reward": result})
    except Exception as e:
        print(f"Error: {e}")


# get addres of admin and current value of exchange rate for recycling items
def getExchangeRate(request):
    try:
        result = PlasticPay_contract.functions.getSummary().call
        return JsonResponse({"success": True, "result": result})
    except Exception as e:
        print(f"Error: {e}")


# get contract balance
def getBalance(request):
    try:
        result = PlasticPay_contract.functions.getContractBalance().call
        return JsonResponse({"success": True, "contract balance": result})
    except Exception as e:
        print(f"Error: {e}")


# redeem rewards. get Matic value for recycled items
def recieve_payment(request):
    try:
        result = PlasticPay_contract.functions.redeemRewards().transact()
        receipt = web3.eth.get_transaction_receipt(result)
        return JsonResponse({"success": True, "receipt": receipt})
    except Exception as e:
        print(f"Error: {e}")


# recycle items
def recycle_item(request, items):
    try:
        result = PlasticPay_contract.functions.recycleItems(items).transact()
        receipt = web3.eth.get_transaction_receipt(result)
        return JsonResponse({"success": True, "receipt": receipt})
    except Exception as e:
        print(f"Error : {e}")


# donate to plasticPay
def donate(request, amount):
    try:
        result = PlasticPay_contract.functions.donatefunds(amount).transact()
        receipt = web3.eth.get_transaction_receipt(result)
        return JsonResponse({"success": True, "receipt": receipt})
    except Exception as e:
        print(f"Error : {e}")
