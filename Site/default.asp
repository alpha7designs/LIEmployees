<%if session("x") <> "x" then
    response.redirect "login.asp"
end if%>    

<!--#include file="includes/connect.asp"-->

<%
company = trim(Request.form("company"))
url     = trim(Request("URL"))

if company <> "" and url <>"" then
    s = "insert JodyEmployees(Company, URL) select '" & replace(company, "'", "''") & "', '" & replace(URL, "'", "''") & "'"
    oconn.execute s
end if

del = Request("del")
if del <>"" then
    s = "delete from JodyEmployees where intID = " & del
    oConn.execute s
end if
%>
<html>
    <head>
        <title>Employer Monitor</title>
    </head>

    <body style="font-family:verdana; font-size:14px;">
<%set oRS=CreateRS()
s = "select * from JodyConfig"
oRS.open s, oConn
last = oRS("LastChecked")
oRS.close

s = "select * from JodyEmployees(nolock) order by Company"
oRS.open s, oConn
if not oRS.eof then%>
    <table>
    <tr>
        <td></td>
        <td>Company</td>
        <td>URL</td>
        <td>Employees</td>
        <td></td>
    </tr>
    <form method="post">
    <%c = 0
        while not oRS.eof
            c = c + 1%>
            <tr>
                <td></td>
                <td><input type="text" value="<%=oRS("Company")%>" size="20" maxlength="50"></td>
                <td><input type="text" value="<%=oRS("URL")%>" size="40" maxlength="200"></td>
                <td align="right">
                <% if oRS("LastNum") > 0 then%>
                    <%=formatnumber(oRS("LastNum"), 0)%>
                <%else%>
                    <i>Pending</i>
                <%end if%>    
                </td>
                <td width="100"><center><a href="javascript:void(0);" onclick="del(<%=oRS("intID")%>);">X</a></center></td>
                <input name="f<%=cstr(c)%>" type="hidden" value="<%=oRS("intID")%>">
            </tr>
            <%oRS.movenext
        wend%>
        <tr>
            <td><font color="red">NEW</td>
            <td><input type="text" size="20" maxlength="50" name="company"></td>
            <td><input type="text" size="40" maxlength="200" name="URL"></td>
            <td></td>
            <td><center><input type="submit" value=" Add "></center></td>
        </tr>
        <input type="hidden" value="<%=c%>" name="num">
    </form>
    </table>
<br>&nbsp;Last Checked: <%=formatdatetime(last,2)%>&nbsp;<%=formatdatetime(last,4)%>
<%end if
oRS.close
oConn.close%>
</body>
<script>
function del(i){
    if(confirm('Delete this Company?'))
        window.location='default.asp?del='+i;
}
</script>
</html>

