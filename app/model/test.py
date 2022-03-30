import pickle

model_columns = pickle.load(
    open(
        '/home/nemish/BeCode/BeCode_Projects/price_prediction_api/app/model/model_columns.pkl',
        'rb'))

print(model_columns)