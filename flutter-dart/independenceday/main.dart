import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.white,
      child: Column(
        children: <Widget>[
          Expanded(child: Container(color: Color(0xf4c43000))),
          Expanded(
            child: Container(
                child: Center(
                    child: Image.network(
                        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Ashoka_Chakra.svg/1200px-Ashoka_Chakra.svg.png"))),
          ),
          Expanded(
            child: Container(color: Colors.green),
          ),
        ],
      ),
    );
  }
}
