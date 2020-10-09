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

public class FirstPageTest {

    @Rule
    public ActivityTestRule<FirstPage> mActivityTestRule = new ActivityTestRule<FirstPage>(FirstPage.class);

    private FirstPage mActivity = null;

    Instrumentation.ActivityMonitor monitor = getInstrumentation().addMonitor(FirstPage.class.getName(),null, false);

    @Before
    public void setUp() throws Exception {

        mActivity = mActivityTestRule.getActivity();


    }

    @Test
    public void TherapistLogin()
    {
        assertNotNull(mActivity.findViewById(R.id.btnTherapistLogin)); //Perform a click on the button
        onView(withId(R.id.btnTherapistLogin)).perform(click()); //should perform the click and launch
        Activity sActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(sActivity);
        sActivity.finish();
    }

    @Test
    public void PatientLogin()
    {
        assertNotNull(mActivity.findViewById(R.id.btnPatientLogin)); //Perform a click on the button
        onView(withId(R.id.btnPatientLogin)).perform(click()); //should perform the click and launch
        Activity sActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(sActivity);
        sActivity.finish();
    }
    @After
    public void tearDown() throws Exception {
        mActivity = null;
    }
}