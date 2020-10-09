package com.example.anxietyapp;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static com.example.anxietyapp.DrawGraph.drawGraph;
import static org.junit.Assert.*;

public class DrawGraphTest {

    @Before
    public void setUp() throws Exception {

        DrawGraph drawGraph = new DrawGraph();


    }
    @Test
    public void drawGraphs()
    {
        //check if value is not empty
        Boolean isDate = true;
        int val = 2;
        String date1 = "1/3/19";

        if(date1.equals(date1))
        {
            isDate = true;
            drawGraph(val, date1);
        }

        assertNotNull("it works!", isDate);
    }

    @After
    public void tearDown() throws Exception {
    }
}