import requests
import json

from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, **kwargs):
    
    #print("GET from {} ".format(url))
    json_data={}
    try:
        if "apikey" in kwargs:
            response = requests.get(url, headers={'Content-Type':'application/json'}, params=kwargs, auth=HTTPBasicAuth("apikey", kwargs["apikey"]))
        else:
            response = requests.get(url, headers={'Content-Type':'application/json'}, params=kwargs)

        status_code = response.status_code
        #print("With status {} ".format(status_code))
        json_data = json.loads(response.text)
        #print(json_data)
    except Exception as e:
        print("Error " ,e)
    
    return json_data

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, payload, **kwargs):
    print("post-request-called")
    try:
        
       # response = requests.post(url,json=payload,params=kwargs)
        response=requests.post(url,data=payload)
       # response2=request.post(url,json=review)
        
        print(json)
    except Exception as e:
        print("Error" ,e)
    print("Status Code ", {response.status_code})
    data = json.loads(response.text)
    print(data)
    return data

# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    
    if json_result:
        # Get the row list in JSON as dealers
        if "rows" in json_result:

            dealers = json_result["rows"]
            for i in range(len(dealers)-3):
                    dealer_doc = dealers[i]["doc"]
                    # Create a CarDealer object with values in `doc` object
                    dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                            id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                            short_name=dealer_doc["short_name"],
                            st=dealer_doc["st"], zip=dealer_doc["zip"])
                    results.append(dealer_obj)

        else:
             dealers = json_result
             print(dealers)
       

        # For each dealer object
        # for dealer_doc in dealers:
            # Get its content in `doc` object
        for i in range(len(dealers)-3):
            dealer_doc = dealers[i]["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results
#Coding practice: create a get_dealer_by_id or get_dealers_by_state method in restapis.py. HINT, the only difference from the get_dealers_from_cf method is adding a dealer id or state URL parameter argument when calling the def get_request(url, **kwargs): method such as get_request(url, dealerId=dealerId).


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list
def get_dealer_reviews_from_cf(url, dealer_id):
    results = []
    reviews=[]
    # Call get_request with a URL parameter
    json_result = get_request(url, id=dealer_id)
    if "data" in json_result:

        #print(json_result)
        reviews = json_result["data"]["docs"]
        #print(reviews)
        # For each review object
    for review in reviews:
            review_obj = DealerReview(
                dealership=review["dealership"],
                name=review["name"],
                purchase=review["purchase"],
                review=review["review"],
                purchase_date=review["purchase_date"],
                car_make=review["car_make"],
                car_model=review["car_model"],
                car_year=review["car_year"],
                sentiment=analyze_review_sentiments(review["review"]),
                id=review['id']
                )
            results.append(review_obj)
    #print(results[0])
    return results

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
def analyze_review_sentiments(dealerreview, **kwargs):
    API_KEY="TbnbKpIvk3MkRuohijbOpnK_XhBGviWi6jN0aBkBn-ym"
    NLU_URL='https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/80cc5186-8fed-4423-bc45-b18f1467ce49'
    params = json.dumps({"text": dealerreview, "features": {"sentiment": {}}})
    response = requests.post(NLU_URL,data=params,headers={'Content-Type':'application/json'},auth=HTTPBasicAuth("apikey", API_KEY))
    
    
    try:
        sentiment=response.json()['sentiment']['document']['label']
        return sentiment
    except:
        return "neutral"
