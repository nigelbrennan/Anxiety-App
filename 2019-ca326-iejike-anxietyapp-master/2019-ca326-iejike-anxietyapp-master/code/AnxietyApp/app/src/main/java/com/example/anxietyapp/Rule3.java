package com.example.anxietyapp;

public class Rule3 {
/*
    // rule 3 to compare timestamp with altitude file, to see if timestamp matches a change in altitude like going up stairs etc.
    public class rule3(String dateTime){}
    void getData()
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
                             String dateTimeAltitude="";
                             String value = "";
                             double dateTimeAltitude = 0;
                             double value= 0;

                             //json = (json data)
                             JsonParser parser = new JsonParser();
                             //Parsing to json
                             JsonObject rootObj = parser.parse(response.body().toString()).getAsJsonObject();
                             //specify where it is exactly using the .
                             JsonArray paymentsArray = rootObj.getAsJsonObject("activities-altitude").getAsJsonArray("dataset");
                             //Iterable loop through


                             for (JsonElement pa : paymentsArray) {
                                 JsonObject paymentObj = pa.getAsJsonObject();
                                 dateTimeAltitude = paymentObj.get("dateTime").getAsString();
                                 value = paymentObj.get("value").getAsString();

                                 //dateTime passed in from rule 2.
                                 //datetimealtitude is the timestamp for the altitude value. if the datetime is the same as datetimealtitude it mean
                                 //that it can be assumed that there was a spike in altitude corresponding to a heart rate spike such as a user running up the stairs.

                                 if(dateTimeAltitude == dateTime && value>10)
                                 //return to rule 1 to continue searching fitbit data.
                                 rule1.rule1(dateTime);

						else{
                                    //send notification to the user using push notification
                                     Notification(dateTime);
                                     //upload the graph data to the firebase database
                                     DrawGraph.DrawGraph(dateTime);
                                     //return to rule1 to continue searching through fitbit data
                                     rule1.rule1(dateTime);

                                 }

                             }
                         }




    }


    @Override
    public void onFailure(Call<JsonObject> call, Throwable t) {
        Log.i("APP MATI", "DoneX: ");
        textViewResults.setText(t.getMessage());
    }
});
        }*/
}
