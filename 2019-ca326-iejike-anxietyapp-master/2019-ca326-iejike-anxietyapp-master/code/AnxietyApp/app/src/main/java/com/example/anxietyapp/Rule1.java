package com.example.anxietyapp;

public class Rule1 {

    /*
    public class rule1(String dateTime){}
{

    //TeamView to get the results and print on android phone
    textViewResults = findViewById(R.id.text_view_result);

    //Retrofit
    Retrofit retrofit = new Retrofit.Builder()
            .baseUrl("https://api.fitbit.com/")
            .addConverterFactory(GsonConverterFactory.create())
            .build();

    FitbitApi fitbitApi = retrofit.create(FitbitApi.class);
    Log.i("APP MATI", "Done00: " ); //Log to know if function was executed

    //make a call to api using "Bearer"
    //Bearer advised by fitbit
    Call<JsonObject> call  = fitbitApi.getJson("Bearer " + dataToken);
    Log.i("APP MATI", "Done0: " );

    //enqueue to check if we got a response from the call
    call.enqueue(new Callback<JsonObject>() {
        @Override
        public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
            //getAsJsonArray("activities-heart")
            String time="";
            String value = "";
            int HR = 0;
            double dateTime = 0;

            //json = (json data)
            JsonParser parser = new JsonParser();
            //Parsing to json
            JsonObject rootObj = parser.parse(response.body().toString()).getAsJsonObject();
            //specify where it is exactly using the .
            JsonArray paymentsArray = rootObj.getAsJsonObject("activities-heart-intraday").getAsJsonArray("dataset");
            //Iterable loop through

          for (JsonElement pa : paymentsArray) {
                    JsonObject paymentObj = pa.getAsJsonObject();
                    time = paymentObj.get("time").getAsString();
                    HR = paymentObj.get("value").getAsInt(); //Get value as integer

                    if (HR >= 90) {
                        N = (myNumbers.peek()); //Pop element from the queue

                        if ((HR - N) >= 10) {
                            //Rule2.rule2(dateTime);			//send dateTime value to rule 2 class.
                            Num++;
                            DrawGraph.DrawGraph(Num, time);
                            //Notification.Notification();
                            //Notification.notify(dateTime);
                            Log.e("MATI", "response 34: " + N + " " + time + " " + HR); //Ouput on Logcat

                        }
                    } else {
                        myNumbers.remove();
                        myNumbers.add(HR); //add number to linked list
                        //myNumbers.remove();

                    }



        @Override
        public void onFailure(Call<JsonObject> call, Throwable t) {
            Log.i("APP MATI", "DoneX: ");
            textViewResults.setText(t.getMessage());
        }
    });
}*/
}
