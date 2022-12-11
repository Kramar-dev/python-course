### Free parking mini-service imitation <br>
When we go to some supermarket we usually enter car's number and save it to <br> supermarket's database that not to pay for parking. <br>
Tablet (or any another device) in supermarket - is kind of interface. It is our http-client for saving data in db. <br>
Also http-server is running and when get some car's number from http-client (writer) -> <br> save it to db if not exists (with time and date). <br>
Second http-client (reader) is number's checker. It will get from database if car's number is already saved in database and <br>
how long the car stay on parking. <br>
If time elapsed -> we should leave the parking bill under wiper =) <br>


