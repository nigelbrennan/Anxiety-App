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

    private static final String TAG = CreateProfileActivity.class.getSimpleName();

    private EditText nameEditText, emailEditText;
    private TextView dobTextView;
    private DatePickerDialog datePickerDialog;

    private Button createProfileButton;
    private ProgressBar progressBar;
    private FirebaseAuth auth;
    private FirebaseDatabase firebaseDatabase;
    private DatabaseReference databaseReference;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_profile);

        //To hide AppBar for fullscreen.
        //ActionBar ab = getSupportActionBar();
        //if (ab != null) {
          //  ab.hide();
        //}

        //Get Firebase auth instance
        auth = FirebaseAuth.getInstance();

        // If the user is not logged in then start LoginActivity
        if (auth.getCurrentUser() == null) {
            // close this activity
            finish();
            // start login activity
            startActivity(new Intent(this, MainActivity.class));
        }

        firebaseDatabase = FirebaseDatabase.getInstance();

        // get reference to 'users' node
        databaseReference = firebaseDatabase.getReference("users");

        // store app title to 'app_title' node
        firebaseDatabase.getReference("app_title").setValue("Login Firebase");

        // app_title change listener
        firebaseDatabase.getReference("app_title").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot) {
                Log.e(TAG, "App title updated");

                //String appTitle = dataSnapshot.getValue(String.class);

                // update toolbar title
                //getSupportActionBar().setTitle(appTitle);
            }

            @Override
            public void onCancelled(DatabaseError error) {
                // Failed to read value
                Log.e(TAG, "Failed to read app title value.", error.toException());
            }
        });

        nameEditText = findViewById(R.id.create_profile_name_editText);
        emailEditText = findViewById(R.id.create_profile_email_editText);
        dobTextView = findViewById(R.id.create_profile_dob_textView);
        createProfileButton = findViewById(R.id.create_profile_button);
        progressBar = findViewById(R.id.create_profile_progressBar);

        dobTextView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // calender class's instance and get current date , month and year from calender
                final Calendar calendar = Calendar.getInstance();
                int mYear = calendar.get(Calendar.YEAR); // current year
                int mMonth = calendar.get(Calendar.MONTH); // current month
                int mDay = calendar.get(Calendar.DAY_OF_MONTH); // current day
                // date picker dialog
                datePickerDialog = new DatePickerDialog(CreateProfileActivity.this,
                        new DatePickerDialog.OnDateSetListener() {
                            @Override
                            public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                                // set day of month , month and year value in the edit text
                                dobTextView.setText(dayOfMonth + "/" + (monthOfYear + 1) + "/" + year);
                            }
                        }, mYear, mMonth, mDay);
                datePickerDialog.show();
            }
        });

        createProfileButton.setOnClickListener(new View.OnClickListener() {
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

        String Name = nameEditText.getText().toString().trim();
        String Email = emailEditText.getText().toString().trim();
        String Age = dobTextView.getText().toString().trim();
        FirebaseDatabase firebaseDatabase = FirebaseDatabase.getInstance();
        DatabaseReference myRef = firebaseDatabase.getReference(auth.getUid());
        UserProfile userProfile = new UserProfile(Age, Email, Name);
        myRef.setValue(userProfile);
        Toast.makeText(this, "Profile created successfully", Toast.LENGTH_SHORT).show();
    }


}