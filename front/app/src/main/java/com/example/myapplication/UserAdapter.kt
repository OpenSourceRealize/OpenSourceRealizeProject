package com.example.myapplication
import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.BaseAdapter
import android.widget.TextView
import org.w3c.dom.Text

class UserAdapter(val context: Context,val UserList: ArrayList<user>) : BaseAdapter() {

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View = LayoutInflater.from(context).inflate(R.layout.list_item_user,null)//view붙이기 위함

        val number = view.findViewById<TextView>(R.id.number)
        val date = view.findViewById<TextView>(R.id.datetext)
        val boxnum = view.findViewById<TextView>(R.id.boxnumtext)

        val user = UserList[position]
        number.text = user.number
        date.text = user.date
        boxnum.text = user.boxnum

        return view


    }

    override fun getItem(position: Int): Any {

        return UserList[position]

    }

    override fun getCount(): Int {
        return UserList.size
    }


    override fun getItemId(position: Int): Long {
        return 0
    }

}