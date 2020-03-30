<%iTimeOffset = 0

set oConn = server.CreateObject("ADODB.Connection")
sconn = "Provider=SQLOLEDB;Data Source=YOUR SERVER NAME;Initial Catalog=LinkedIn;User Id=LinkedIn;Password=ni2iLvsQnqMMX5O0CXdSOCLdWzKvN58VoqWgdpSjV9I"

oConn.open sConn

function CreateRS
    dim oX
    set oX = server.CreateObject("ADODB.recordset")
    set CreateRS = oX
end function

Function pd(n, totalDigits) 
        if totalDigits > len(n) then 
            pd = String(totalDigits-len(n),"0") & n 
        else 
            pd = n 
        end if 
End Function 

function FixTime(tim)
    if isnull(tim) or not isdate(tim) then
        FixTime = ""
        exit function
    end if
	adj = dateadd("h", iTimeOffset,tim)
    res = Pd(datepart("D",adj), 2) & "/" & Pd(datepart("M",adj), 2) & "/" & YEAR(adj) 
	tmp = formatdatetime(adj,4)
	'tmp = left(tmp,len(tmp) - 6) &  right(tmp,3)
	FixTime = res & " " & tmp
end function

function fixer(s)
    fixer=replace(s, "'", "''")
end function    
%>