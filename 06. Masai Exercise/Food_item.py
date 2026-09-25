Food_Delivery = {
    "Customer" : 'Rahul Vajpayee',
    "Item": 'Burger',
    "Rate" : 150,
    "Quantity" : 2,
    "Address" : 'Bangalore',
    "Total" : 150 * Food_Delivery["Quantity"]
}

Movie_Ticket = {
    Movie_Director : 'Christopher Nolan',
    Movie_Name : 'Inception',
    movie_Rate : 250,
    movie_Cast : ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'],
    movie_Release_Date : '2010-07-16',
    movie_Theater : 'PVR Cinemas',
    movie_Seat_Number : 'A12',
    movie_Total : 250 * 1
}   

print(type(Food_Delivery.items()))
