import "dart:io";

var alphabetList = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                    'n','o','p','q','r','s','t','u','v','w','x','y','z'];
  
var secretCode = { 'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ', ':'--..--', '.':'.-.-.-',
            '?':'..--..', '/':'-..-.', '-':'-....-',
            '(':'-.--.', ')':'-.--.-',' ':' '};


// String prompt(String promptText){
//   print(promptText);
//   // print("The prompt is: ${promptText}");
//   String answer = stdin.readLineSync()!;
//   return answer;
// }



englishToMorse() {
  var secretCodeReverse = {};
  String decodedCode = "";
  var char2;
  // print(secretCode["A"]);

  // secretCode.forEach((key, value){
  //   // print("$key = $value");
  //   secretCodeReverse["${value}"] = "${key}"; 
  // });
  // print(secretCodeReverse);

  print("\n\n--------\nMessage: ");
  var inputCode = stdin.readLineSync()!;
  // var inputCode = prompt("Message: ");
  
  for(int i=0; i<inputCode.length; i++) {
    var char1 = inputCode[i];
    if(alphabetList.contains(char1)){
      char1 = char1.toUpperCase();
      var char2 = secretCode[char1];
      decodedCode = decodedCode + char2! + " ";
      // print(char2);
    }else{
      var char2 = secretCode[char1];
      decodedCode = decodedCode + char2! + " ";
      // print(char2);
    }  
  }
  print(decodedCode);
}




morseToEnglish(){
  var secretCodeReverse = {};
  String decodedCode = "";
  var char2;
  // print(secretCode["A"]);

  secretCode.forEach((key, value){
    // print("$key = $value");
    secretCodeReverse["${value}"] = "${key}"; 
  });
  // print(secretCodeReverse);

  print("\n\n--------\nMessage: ");
  var inputCode = stdin.readLineSync()!;
  print("\n");
  // var inputCode = prompt("Message: ");

  List<String> inputCodeList = inputCode.split('   ');
  // print(inputCodeList);
  inputCodeList.forEach((i) {
    print(i);
    List<String> inputCodeList2 = i.split(' ');
    inputCodeList2.forEach((j) {
    print(j);
    var char2 = secretCodeReverse[j];
    // decodedCode = decodedCode + char2! + " ";
    decodedCode = decodedCode + char2!;
    });
  decodedCode = decodedCode + " ";
  });
  
  print(decodedCode);
}



void main() {
  print("Type the option No. and press Enter-\n1: eng_to_morse\n2: morse_to_eng");
  var optchosen = stdin.readLineSync();
  // var optchosen = prompt(": ");
  // print(optchosen);
  if(optchosen == "1"){
    englishToMorse();
  }else if(optchosen == "2"){
    morseToEnglish();
  }else{
    print("Invalid Option!");
  }

}
