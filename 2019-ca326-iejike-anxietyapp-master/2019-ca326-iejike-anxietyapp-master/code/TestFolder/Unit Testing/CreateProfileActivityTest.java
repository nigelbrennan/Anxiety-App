package com.example.anxietyapp;

import android.app.Activity;
import android.app.Instrumentation;
import android.support.test.rule.ActivityTestRule;

import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;

import static android.support.test.InstrumentationRegistry.getInstrumentation;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static org.junit.Assert.*;

public class CreateProfileActivityTest {
    @Rule
    public ActivityTestRule<CreateProfileActivity> mActivityTestRule = new ActivityTestRule<CreateProfileActivity>(CreateProfileActivity.class);

    private CreateProfileActivity mActivity = null;

    Instrumentation.ActivityMonitor monitor = getInstrumentation().addMonitor(CreateProfileActivity.class.getName(),null, false);

    @Before
    public void setUp() throws Exception {

        mActivity = mActivityTestRule.getActivity();


    }

    @Test
    public void nameEditText()
    {
        assertNotNull(mActivity.findViewById(R.id.create_profile_name_editText)); //Perform a click on the button
        onView(withId(R.id.create_profile_name_editText)).perform(click()); //should perform the click and launch
        Activity sActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(sActivity);
        sActivity.finish();
    }

    @Test
    public void emailEditText()
    {
        assertNotNull(mActivity.findViewById(R.id.create_profile_email_editText)); //Perform a click on the button
        onView(withId(R.id.create_profile_email_editText)).perform(click()); //should perform the click and launch
        Activity sActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(sActivity);
        sActivity.finish();
    }

    @Test
    public void dobTextView()
    {
        assertNotNull(mActivity.findViewById(R.id.create_profile_dob_textView)); //Perform a click on the button
        onView(withId(R.id.create_profile_dob_textView)).perform(click()); //should perform the click and launch
        Activity sActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(sActivity);
        sActivity.finish();
    }

    @Test
    public void createProfileButton()
    {
        assertNotNull(mActivity.findViewById(R.id.create_profile_name_editText)); //Perform a click on the button
        onView(withId(R.id.create_profile_name_editText)).perform(click()); //should perform the click and launch
        Activity sActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(sActivity);
        sActivity.finish();
    }


    @Test
    public void progressBar()
    {
        assertNotNull(mActivity.findViewById(R.id.create_profile_progressBar)); //Perform a click on the button
        onView(withId(R.id.create_profile_progressBar)).perform(click()); //should perform the click and launch
        Activity sActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(sActivity);
        sActivity.finish();
    }


    @After
    public void tearDown() throws Exception {
        mActivity = null;
    }
}