import investpy

def get_search(form,to):
    df = investpy.get_stock_historical_data(stock='AAPL',
                                        country='United States', 
                                        from_date=form, 
                                        to_date=to,
                                        as_json=True)

    return df

form="01/01/2021"
to="27/09/2021"
t=get_search(form,to)
print(t)