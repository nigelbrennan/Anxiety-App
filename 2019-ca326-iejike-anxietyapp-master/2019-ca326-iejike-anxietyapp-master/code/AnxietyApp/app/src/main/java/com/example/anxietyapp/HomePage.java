package com.example.anxietyapp;

import android.content.Intent;
import android.net.Uri;
import android.support.customtabs.CustomTabsIntent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import static android.content.Intent.FLAG_ACTIVITY_NEW_TASK;


public class HomePage extends AppCompatActivity {

    private FirebaseAuth mAuth;
    private Button logout;
    private Button graph;
    private Button profile;
    private TextView textViewResults;
    private static String clientSecrect = "02718e0d2086f47702ab1e61559d6365";
    private static String clientid = "22DBZN"; //it needs to know who is talking to
    private static String redirecturl = "myapp://callback"; //how can the server can send you back the information // call back needs to be an odd name to make chrome ihgnore it and go directly back to your app https://community.fitbit.com/t5/Web-API-Development/Redirect-url-need-URGENT-advice/td-p/2596999
    private String url = "https://www.fitbit.com/oauth2/authorize?" + "response_type=token&client_id=" + clientid + "&redirect_uri=" + redirecturl + "&scope=activity%20heartrate%20location%20nutrition%20profile%20settings%20sleep%20social%20weight&expires_in=604800";
    private static final String TAG = "festActivity";
    private String dataToken;
    private Button loginbtn;
    private int Num;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home_page);
        mAuth = FirebaseAuth.getInstance();
        graph = (Button) findViewById(R.id.btnViewGraph);
        profile = (Button) findViewById(R.id.btnprofile);
        logout = (Button) findViewById(R.id.btnLogout);
        logout.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Logout();
            }
        });
        graph.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(HomePage.this, ViewGraph.class));
            }
        });
        profile.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(HomePage.this, ProfileActivity.class));
            }
        });

        Button loginbtn = (Button) findViewById(R.id.loginbtn);
        loginbtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                CustomTabsIntent.Builder builder = new CustomTabsIntent.Builder();
                CustomTabsIntent intent = builder.build();

                intent.intent.setFlags(FLAG_ACTIVITY_NEW_TASK);
                Uri theLocationUri = Uri.parse(url);
                intent.launchUrl(HomePage.this, theLocationUri);
            }
        });


    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        String action = intent.getAction();
        String data = intent.getDataString();//parse this to get the data
        Uri uri = Uri.parse(String.valueOf(intent.getData()));


        if (Intent.ACTION_VIEW.equals(action) && data != null) {
            try {
                Toast.makeText(this, data, Toast.LENGTH_SHORT).show();
                dataToken = uri.toString();

                //Pattern
                Pattern p = Pattern.compile("(?<=access_token=).+?(?=&)");
                Matcher m = p.matcher(dataToken);
                if (m.find()) {
                    dataToken = m.group(); // contains access token after it's gone through regex to remove the expired by part
                }
                getData();

            } catch (Exception e) {
                e.printStackTrace();
            }
        } else {

        }
    }
    void getData() {
        //TeamView to get the results and print on android phone
        textViewResults = findViewById(R.id.text_view_result);

        //Retrofit
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("https://api.fitbit.com/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        FitbitApi fitbitApi = retrofit.create(FitbitApi.class);
       // Log.i("APP MATI", "Done00: "); //Log to know if function was executed

        //make a call to api using "Bearer"
        //Bearer advised by fitbit
        Call<JsonObject> call = fitbitApi.getJson("Bearer " + dataToken);
        //Log.i("APP MATI", "Done0: ");

        //enqueue to check if we got a response from the call
        call.enqueue(new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                Queue<Integer> myNumbers = new LinkedList<>();
                myNumbers.add(65);
                myNumbers.add(70);
                myNumbers.add(65);
                myNumbers.add(70);
                myNumbers.add(65);
                myNumbers.add(65);
                int N = 0;

                //getAsJsonArray("activities-heart")
                int HR = 0;
                String time= "";
                int Num = 0;

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

                    if (HR >= 100) {
                        N = (myNumbers.peek()); //Pop element from the queue

                        if ((HR - N) >= 10) {
                            //Rule2.rule2(dateTime);			//send dateTime value to rule 2 class.
                            Num++;
                            //DrawGraph.DrawGraph(Num, time);
                            //Notification.Notification();
                        }
                    } else {
                        myNumbers.remove();
                        myNumbers.add(HR); //add number to linked list
                    }
                }
                DrawGraph.DrawGraph(Num,time);
            }


            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                textViewResults.setText(t.getMessage());
            }
        });
    }

        private void Logout () {
            mAuth.signOut();
            finish();
            startActivity(new Intent(HomePage.this, MainActivity.class));
        }

        @Override
        public boolean onCreateOptionsMenu (Menu menu){
            getMenuInflater().inflate(R.menu.menu, menu);
            return true;
        }

        @Override
        public boolean onOptionsItemSelected (MenuItem item){

            switch (item.getItemId()) {
                case R.id.logoutMenu: {
                    Logout();
                    break;
                }
            }
            return super.onOptionsItemSelected(item);
        }
    }

