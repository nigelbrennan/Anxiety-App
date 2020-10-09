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


public class HomePageTest {
    @Rule
    public ActivityTestRule<HomePage> mActivityTestRule = new ActivityTestRule<HomePage>(HomePage.class);

    private HomePage mActivity = null;

    Instrumentation.ActivityMonitor monitor = getInstrumentation().addMonitor(HomePage.class.getName(),null, false);

    @Before
    public void setUp() throws Exception {

        mActivity = mActivityTestRule.getActivity();


    }

    @Test
    public void testLaunchOnSeconcActivityOnClick()
    {
        assertNotNull(mActivity.findViewById(R.id.loginbtn));
        onView(withId(R.id.loginbtn)).perform(click()); //should perform the click and launch
        Activity secondActivity = getInstrumentation().waitForMonitorWithTimeout(monitor, 5000);
        assertNotNull(secondActivity);
        secondActivity.finish();
    }


    @After
    public void tearDown() throws Exception {
        mActivity = null;
    }
}