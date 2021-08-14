function myFunction() {
 var x =document.getElementById("msg");
               x.className="show";
               setTimeout(function(){x.className=x.className.replace("show","");},3000);
  alert("Password should have: <br>
  length between 6 & 20 <br>
  at least one numeral<br>
  at least one uppercase letter<br>
  at least one  lowercase letter<br>
  at least one of the symbols $@#");
}
