package com.example.anxietyapp;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import com.jjoe64.graphview.DefaultLabelFormatter;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;
import java.text.SimpleDateFormat;
import java.util.Date;

public class ViewGraph extends AppCompatActivity {

    FirebaseDatabase database;
    DatabaseReference reference;
    GraphView graphView;
    LineGraphSeries series;
    private Button HomeButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_graph);
        HomeButton = (Button) findViewById(R.id.btnHome);
        HomeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(ViewGraph.this, HomePage.class));
            }
        });
        //set up the graph
        graphView = (GraphView) findViewById(R.id.graphView);
        series = new LineGraphSeries();
        graphView.addSeries(series);
        database = FirebaseDatabase.getInstance();
        //connect to the table in the database with the graph data
        reference = database.getReference("chartTable1");
        //set graph to display 3 numbers on the x axis for readability.
        graphView.getGridLabelRenderer().setNumHorizontalLabels(3);
    }

    @Override
    protected void onStart() {
        super.onStart();
        //update the graph in real time for the viewer.if new details are added to database theyll be shown here.
        reference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                DataPoint[] dp = new DataPoint[(int) dataSnapshot.getChildrenCount()];
                int index = 0;
                for (DataSnapshot myDataSnapshot : dataSnapshot.getChildren()) {
                    PointValue pointValue = myDataSnapshot.getValue(PointValue.class);
                   dp[index] = new DataPoint(pointValue.getxValue(), pointValue.getyValue());
                    index++;
                }
                series.resetData(dp);
            }
            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {
            }
        });

    }
}