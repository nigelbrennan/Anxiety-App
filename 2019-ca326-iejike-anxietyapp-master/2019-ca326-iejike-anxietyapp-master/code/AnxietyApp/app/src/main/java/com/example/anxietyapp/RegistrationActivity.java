package com.example.anxietyapp;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.Switch;
import android.widget.Toast;

import com.google.android.gms.common.util.AndroidUtilsLight;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.regex.Pattern;

public class RegistrationActivity extends AppCompatActivity implements View.OnClickListener {
    EditText username, password ,email,age;
    ProgressBar progressBar;
    FirebaseDatabase database;
    DatabaseReference reference;
    private FirebaseAuth mAuth;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);

        username = findViewById(R.id.username);
        age = findViewById(R.id.age);
        email = findViewById(R.id.email);
        password = findViewById(R.id.password);
        progressBar = findViewById(R.id.progressBar);
        mAuth = FirebaseAuth.getInstance();
        findViewById(R.id.Register).setOnClickListener(this);


    }
    public void login(View view) {
        Intent login = new Intent(this, MainActivity.class);
        startActivity(login);

    }
    private void sendUserData() {

        String Age = age.getText().toString().trim();
        String Email = email.getText().toString().trim();
        String Name = username.getText().toString().trim();
        FirebaseDatabase firebaseDatabase = FirebaseDatabase.getInstance();
        DatabaseReference myRef = firebaseDatabase.getReference(mAuth.getUid());
        UserProfile userProfile = new UserProfile(Age, Email, Name);
        myRef.setValue(userProfile);
    }

    private void registerUser() {
        String username1 = username.getText().toString().trim();
        String password1 = password.getText().toString().trim();

        if (username1.isEmpty()) {
            username.setError("Email is required");
            username.requestFocus();
            return;

        }
        if (password1.isEmpty()) {
            password.setError("password is required");
            password.requestFocus();
            return;

        }
        if (!Patterns.EMAIL_ADDRESS.matcher(username1).matches()) {
            username.setError("Invalid email");
            username.requestFocus();
            return;
        }
        if (password1.length() < 6) {
            password.setError("Password can't be less than 6 characters");
            password.requestFocus();
            return;
        }

        progressBar.setVisibility(View.VISIBLE);
        mAuth.createUserWithEmailAndPassword(username1, password1).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()) {
                    sendUserData();
                    Toast.makeText(getApplicationContext(), "Registered successfull", Toast.LENGTH_SHORT).show();
                    progressBar.setVisibility(View.GONE);


                } else {
                    Log.i("Response", "Failed to create user:" + task.getException().getMessage());
                    Toast.makeText(getApplicationContext(), "Failed to create user", Toast.LENGTH_SHORT).show();
                    progressBar.setVisibility(View.GONE);
                }
            }
        });




}

    @Override
    public void onClick(View v) {
        switch(v.getId()){
            case R.id.Register:
                registerUser();

                break;
        }
    }
}