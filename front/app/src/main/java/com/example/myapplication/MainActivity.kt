package com.example.myapplication

import android.os.Build
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.*
import androidx.annotation.RequiresApi
import com.google.firebase.database.*
import java.util.*


class MainActivity : AppCompatActivity() {

    var UserList = arrayListOf<user>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val database: FirebaseDatabase =
            FirebaseDatabase.getInstance("https://my-application-e7c14-default-rtdb.firebaseio.com/")
        val myRef: DatabaseReference = database.getReference("2021-10-2")
        val textView1 = findViewById<TextView>(R.id.textView1)
        val textView2 = findViewById<TextView>(R.id.textView2)
        val textView3 = findViewById<TextView>(R.id.textView3)
        val BUTTON = findViewById<Button>(R.id.button)
        val BUTTON2 = findViewById<Button>(R.id.button2)
        val listView = findViewById<ListView>(R.id.listView)
        val Adapter = UserAdapter(this,UserList)



        BUTTON2.setOnClickListener {
            myRef.child("총 개수").child("사창동").setValue(0)
            myRef.child("총 개수").child("개신동").setValue(0)
            myRef.child("총 개수").child("오창읍").setValue(0)

        }


        BUTTON.setOnClickListener {


            myRef.addValueEventListener(object : ValueEventListener {

                override fun onDataChange(snapshot: DataSnapshot) { // 리스트 만들 배열 가져오기
                    UserList.clear()
                    val test = snapshot.child("list")
                        for (ds in test.children) {
                            val e1 = user(
                                ds.child("순번").getValue().toString(),
                                ds.child("바코드찍은 날짜").getValue().toString(),
                                ds.child("운송장번호").getValue().toString()
                            )
                            UserList.add(e1)
                        }
                        listView.adapter = Adapter
                }

                override fun onCancelled(error: DatabaseError) {
                    println("Failed to read value.")
                }
            })


            //Read from the database
            myRef.child("총 개수").child("사창동").addValueEventListener(object : ValueEventListener {


                override fun onDataChange(snapshot: DataSnapshot) {
                    val value = snapshot.value
                    textView2.text = "$value"
                }

                override fun onCancelled(error: DatabaseError) {
                    println("Failed to read value.")
                }
            })

            myRef.child("총 개수").child("개신동").addValueEventListener(object : ValueEventListener {


                override fun onDataChange(snapshot: DataSnapshot) {
                    val value = snapshot.value
                    textView1.text = "$value"
                }

                override fun onCancelled(error: DatabaseError) {
                    println("Failed to read value.")
                }
            })

            myRef.child("총 개수").child("오창읍").addValueEventListener(object : ValueEventListener {


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