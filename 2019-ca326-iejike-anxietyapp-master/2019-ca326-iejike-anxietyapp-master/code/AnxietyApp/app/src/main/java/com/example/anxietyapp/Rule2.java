package com.example.anxietyapp;

public class Rule2 {
    /*
    //rule 2 to compare timestamp from heart rate with activities from activities file. like walki,exercise etc.

    public class rule2(String dateTime){}
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
                String starttime="";
                String endtime = "";
                double startTime = 0;
                double endtime= 0;

                //json = (json data)
                JsonParser parser = new JsonParser();
                //Parsing to json
                JsonObject rootObj = parser.parse(response.body().toString()).getAsJsonObject();
                //specify where it is exactly using the .
                JsonArray paymentsArray = rootObj.getAsJsonObject("activities-exercise").getAsJsonArray("dataset");
                //Iterable loop through
                for (JsonElement pa : paymentsArray) {
                    JsonObject paymentObj = pa.getAsJsonObject();
                    endtime = paymentObj.get("lastModified").getAsString();
                    starttime = paymentObj.get("startTime").getAsString();

                    while(startTime != endtime)
                    {
                        if(startTime == dateTime)


                        //jump back to rule 1 to continue with rest of json heartrate file because this heart rate spike was a result of activity
						rule1.rule1(dateTime);

						else{
                        startTime = startTime + 00:00:01;
                         //time method to increment start time by 1 second , then minutes then hours until its equal to finish time
                            String string = dateTime;
				            String[] parts = string.split(":");
				            //hour
				            String part1 = parts[0];
				            //minute
				            String part2 = parts[1];
				            //seconds
				            String part3 = parts[2];

                            double x = Double.parseDouble(part1));
                            double y = Double.parseDouble(part2);
                            double z = Double.parseDouble(part3);

                            double z= z+1;
                            starttime = x + ":" + y + ":" + z;
                            //has seconds reached 60
                            if (z = 60)
                            {
                                z = 0;
                                y = y+1;
                                starttime = x + ":" + y + ":" + z;
                                //has minutes reached 60
                                if {(y==60)
                                    y=0;
                                    x=x+1;
                                    starttime = x + ":" + y + ":" + z;
                                   }
                             }



                    }
                    }
                    rule3.rule3(dateTime); 	//jump to rule 4 if the date/time of heart rate spike isnt found in activity to check the altitude data.
                }




            }



            //Log to declare the end of method
                Log.i("APP MATI", "Done2: ");

        }


        @Override
        public void onFailure(Call<JsonObject> call, Throwable t) {
        Log.i("APP MATI", "DoneX: ");
        textViewResults.setText(t.getMessage());
    }
    });
}*/


}
