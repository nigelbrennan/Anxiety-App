package com.example.anxietyapp;

import android.app.NotificationManager;
import android.content.Context;
import android.app.PendingIntent;
import android.content.Intent;
import android.support.v4.app.NotificationCompat;

public class Notification {

/*
    public void Notification() {
        NotificationCompat.Builder builder =
                new NotificationCompat.Builder(this, ChannelID)
                        .setSmallIcon(R.drawable.ic_android) //make a drawable button
                        .setContentTitle("Notifications Example")
                        .setContentText("This is a test notification");

        Intent notificationIntent = new Intent(this, Notification.class);
        PendingIntent contentIntent = PendingIntent.getActivity(this, 0, notificationIntent,
                PendingIntent.FLAG_UPDATE_CURRENT);
        builder.setContentIntent(contentIntent);

        // Add as notification
        NotificationManager manager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        manager.notify(0, builder.build());
    }

*/
/*
//my notification method.
public void notify(String dateTime){
	NotificationManager myNotificationManager =
                (NotificationManager) context.getSystemService(Context.NOTIFICATION_SERVICE);

				String string = dateTime;
				String[] parts = string.split(" ");
				String part1 = parts[0];
				String part2 = parts[1];
				String id = reference.push().getKey();
                double x = Double.parseDouble(part1));
                double y = Double.parseDouble(part2);

	//if the anxiety attack happens before 7 am or after 7pm advise the user to meditate
	//instead of tea as the caffeine could upset there sleep and make anxiety worse.

	if(x <07 ||x > 19)
        // Prepare notification.
        Notification.Builder builder = new Notification.Builder(context);
        builder.setSmallIcon(android.R.drawable.ic_dialog_info)
                .setContentTitle("you just experienced an anxiety attack, you should try some mindfulness meditation or deep breathing exercises")
                .setContentText(message)
                .setWhen(System.currentTimeMillis())
                .setAutoCancel(true)
                .setContentIntent(contentIntent)
                .setPriority(Notification.PRIORITY_MAX)
                .setDefaults(Notification.DEFAULT_ALL);

	else{

		 Notification.Builder builder = new Notification.Builder(context);
        builder.setSmallIcon(android.R.drawable.ic_dialog_info)
                .setContentTitle("you just experienced an anxiety attack, you should have a cup of tea and rest for 15 minutes")
                .setContentText(message)
                .setWhen(System.currentTimeMillis())
                .setAutoCancel(true)
                .setContentIntent(contentIntent)
                .setPriority(Notification.PRIORITY_MAX)
                .setDefaults(Notification.DEFAULT_ALL);
	}

        // Notify
        myNotificationManager.notify(notificationId, builder.build());

	}
}
 */
}