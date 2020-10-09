package com.example.anxietyapp;

import android.app.DatePickerDialog;
import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.RadioButton;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.Calendar;

public class CreateProfileActivity extends AppCompatActivity {

    private EditText etname, etemail;
    private TextView tvdob;
    private DatePickerDialog datePickerDialog;
    private Button btnupdate;
    private ProgressBar progressBar;
    private FirebaseAuth mAuth;
    private FirebaseDatabase firebaseDatabase;
    private Button HomeButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_profile);

        HomeButton = (Button)findViewById(R.id.btnHome);

        HomeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(CreateProfileActivity.this, HomePage.class));
            }
        });

        mAuth = FirebaseAuth.getInstance();


        if (mAuth.getCurrentUser() == null) {

            finish();
            startActivity(new Intent(this, MainActivity.class));
        }

        firebaseDatabase = FirebaseDatabase.getInstance();
        firebaseDatabase.getReference("users").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
            }

            @Override
            public void onCancelled(DatabaseError error) {
            }
        });

        etname = findViewById(R.id.name);
        etemail = findViewById(R.id.email);
        tvdob = findViewById(R.id.dob);
        btnupdate = findViewById(R.id.btnupdate);
        progressBar = findViewById(R.id.progressBar);

        tvdob.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                final Calendar calendar = Calendar.getInstance();
                int mYear = calendar.get(Calendar.YEAR);
                int mMonth = calendar.get(Calendar.MONTH);
                int mDay = calendar.get(Calendar.DAY_OF_MONTH);

                datePickerDialog = new DatePickerDialog(CreateProfileActivity.this,
                        new DatePickerDialog.OnDateSetListener() {
                            @Override
                            public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                                tvdob.setText(dayOfMonth + "/" + (monthOfYear + 1) + "/" + year);
                            }
                        }, mYear, mMonth, mDay);
                datePickerDialog.show();
            }
        });

        btnupdate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                progressBar.setVisibility(View.VISIBLE);
                sendUserData();
                progressBar.setVisibility(View.GONE);
                startActivity(new Intent(CreateProfileActivity.this, MainActivity.class));
                finish();
            }
        });
    }


    private void sendUserData() {

        String Name = etname.getText().toString().trim();
        String Email = etemail.getText().toString().trim();
        String Age = tvdob.getText().toString().trim();
        FirebaseDatabase firebaseDatabase = FirebaseDatabase.getInstance();
        DatabaseReference myRef = firebaseDatabase.getReference(mAuth.getUid());
        UserProfile userProfile = new UserProfile(Age, Email, Name);
        myRef.setValue(userProfile);
        Toast.makeText(this, "Profile updated successfully", Toast.LENGTH_SHORT).show();
    }


}