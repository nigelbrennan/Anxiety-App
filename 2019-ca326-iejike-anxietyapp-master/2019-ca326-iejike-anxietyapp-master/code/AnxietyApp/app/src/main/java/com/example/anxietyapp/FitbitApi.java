package com.example.anxietyapp;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import org.json.JSONObject;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Header;


public interface FitbitApi {
   //Get request that requests permission to access Data from Fitbit using AccessToken
    //@GET("1/user/-/activities/steps/date/today/7d.json")
    @GET("1/user/-/activities/heart/date/2019-03-02/1d/1sec.json")
    Call<JsonObject> getJson(@Header("Authorization") String authToken);

}
