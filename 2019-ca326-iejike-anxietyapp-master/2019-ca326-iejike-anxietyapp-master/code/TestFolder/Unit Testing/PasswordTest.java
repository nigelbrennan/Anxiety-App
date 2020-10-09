package com.example.anxietyapp;

import android.support.test.rule.ActivityTestRule;
import android.view.View;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;

import static org.junit.Assert.*;

public class PasswordTest {

    @Rule
    public ActivityTestRule<Password> mActivityTestRule = new ActivityTestRule<Password>(Password.class);

    private Password mActivity = null;


    @Before
    public void setUp() throws Exception {

        mActivity = mActivityTestRule.getActivity();
    }

    @Test
    public void resetPassword(){
        View view = mActivity.findViewById(R.id.btnPasswordReset);

        assertNotNull(view);
    }

    @After
    public void tearDown() throws Exception {

        mActivity = null;
    }
}