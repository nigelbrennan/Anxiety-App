package com.example.anxietyapp;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.jjoe64.graphview.DefaultLabelFormatter;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.LineGraphSeries;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;


public class DrawGraph {

    //method to push the graph data to the firebase database. the num is the y axis and the x is the x axis.
    public static void DrawGraph(int Num, String dateTime) {
        FirebaseDatabase database;
        DatabaseReference reference;
        database = FirebaseDatabase.getInstance();
        reference = database.getReference("chartTable1");
        String id = reference.push().getKey();
        long x =  1;
        PointValue pointValue = new PointValue(x, Num);
        reference.child(id).setValue(pointValue);
        x = x+ 1;

    }
    //return to rule 1
}

