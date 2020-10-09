package com.example.anxietyapp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;
import static org.junit.Assert.assertNotNull;

public class PointValueTest {

    @Before
    public void setUp() throws Exception {
    }


    @Test
    public void pointVal() {
        PointValue p = new PointValue(2, 2);
        double pVal = p.getxValue();

        assertEquals(2, 2);
    }

    @After
    public void tearDown() throws Exception {
    }
}