<%@ Language=VBScript %>

<%
pw = request("pw")

if pw = "lInkedIn2020@" then
    session("x") = "x"
    response.redirect "default.asp"
end if    
%>

<HTML>
<HEAD>
<title>Employer Monitor - Login</title>
<META NAME="GENERATOR" Content="Microsoft Visual Studio 6.0">
</HEAD>

<body onload="document.getElementById('pw').focus();" style="font-family:verdana; font-size:14px;">

<br><br><br><br><br><br>
<center>
<form method="post">
Password: <input id ="pw" name="pw" type="password" size="15" maxlength="15"><br><br>
<input type="submit" value=" OK ">
</form>
</center>

</body>
</html>