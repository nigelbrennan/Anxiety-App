package com.example.anxietyapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class FirstPage extends AppCompatActivity {



    private Button PatientLogin;
    private Button TherapistLogin;

    //first page of app. give user option to sign in as user or therapist.
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_first_page);
        TherapistLogin = (Button)findViewById(R.id.btnTherapistLogin);
        PatientLogin = (Button)findViewById(R.id.btnPatientLogin);


    TherapistLogin.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            startActivity(new Intent(FirstPage.this, TLPage.class));
        }
        });


    PatientLogin.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            startActivity(new Intent(FirstPage.this, MainActivity.class));
        }
        });
    }


}
