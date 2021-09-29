package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import com.google.firebase.database.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val database: FirebaseDatabase =
            FirebaseDatabase.getInstance("https://my-application-e7c14-default-rtdb.firebaseio.com/")
        val myRef1: DatabaseReference = database.getReference("개신동")
        val myRef2: DatabaseReference = database.getReference("사창동")
        val myRef3: DatabaseReference = database.getReference("오창읍")
        val textView1 = findViewById<TextView>(R.id.textView1)
        val textView2 = findViewById<TextView>(R.id.textView2)
        val textView3 = findViewById<TextView>(R.id.textView3)
        val BUTTON = findViewById<Button>(R.id.button)
        val BUTTON2 = findViewById<Button>(R.id.button2)

        BUTTON2.setOnClickListener {
            myRef1.setValue(0)
            myRef2.setValue(0)
            myRef3.setValue(0)

        }


        BUTTON.setOnClickListener {

            //Read from the database
            myRef1.addValueEventListener(object : ValueEventListener {


                override fun onDataChange(snapshot: DataSnapshot) {
                    val value = snapshot.value
                    textView1.text = "$value"
                }

                override fun onCancelled(error: DatabaseError) {
                    println("Failed to read value.")
                }
            })

            myRef2.addValueEventListener(object : ValueEventListener {


                override fun onDataChange(snapshot: DataSnapshot) {
                    val value = snapshot.value
                    textView2.text = "$value"
                }

                override fun onCancelled(error: DatabaseError) {
                    println("Failed to read value.")
                }
            })

            myRef3.addValueEventListener(object : ValueEventListener {


                override fun onDataChange(snapshot: DataSnapshot) {
                    val value = snapshot.value
                    textView3.text = "$value"
                }

                override fun onCancelled(error: DatabaseError) {
                    println("Failed to read value.")
                }
            })

        }


    }


}