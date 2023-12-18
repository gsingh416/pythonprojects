############################################################################## 
 
## The URI list to test 
$User =  "svc-in-hpoo@capgemini.com"
$PWord = ConvertTo-SecureString -string "India#123456789" -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $User, $PWord

Write-Host "Test Message"

$URLListFile = "C:\Windows\Scripts\URLList.txt"  
$URLList = Get-Content $URLListFile -ErrorAction SilentlyContinue  
  $Result = @() 

   j,glkllckxjjjhchkgj fekl;lsfj;wefj;ewj;efj;l;fehfhjsjkkfhlqehlkqgkqklfl;qflj; cqwkjvqlwfkh;qfwj;lqwn;qfw;hbflkqefb;lfj;l hlfqlkbhfqlhqwvghjqfjhfqejhfjwqgkjwdqfjkhfvkjhfqvgdqjhvfjqdwjhqwdjhfvqjhdfjhqdfwhjgqwjhkgqggqwkgvqkgqkjgkjqfwe

   
  Foreach($Uri in $URLList) { 
  $time = try{ 
  $request = $null
  $pos = $Uri.IndexOf(",")
  $region = $Uri.Substring(0, $pos)
  $url = $Uri.Substring($pos+1)
   ## Request the URI, and measure how long the response took. 
  $result1 = Measure-Command { $request = Invoke-WebRequest -Uri $url -UseBasicParsing} 
  $result1.TotalMilliseconds 
  }  
j,glkllckxjjjhchkgj fekl;lsfj;wefj;ewj;efj;l;fehfhjsjkkfhlqehlkqgkqklfl;qflj; cqwkjvqlwfkh;qfwj;lqwn;qfw;hbflkqefb;lfj;l hlfqlkbhfqlhqwvghjqfjhfqejhfjwqgkjwdqfjkhfvkjhfqvgdqjhvfjqdwjhqwdjhfvqjhdfjhqdfwhjgqwjhkgqggqwkgvqkgqkjgkjqfwe
  
  catch 
  { 
   <# If the request generated an exception (i.e.: 500 server 
   error or 404 not found), we can pull the status code from the 
   Exception.Response property #> 
   $request = $_.Exception.Response 
   $time = -1 
  }   
  $result += [PSCustomObject] @{ 
  Time = Get-Date;
  Region = $region;
  Uri = $url; 
  StatusCode = [int] $request.StatusCode; 
  StatusDescription = $request.StatusDescription; 
  ResponseLength = $request.RawContentLength; 
  TimeTaken =  $time;  
  } 
 
} 
    #Prepare email body in HTML format 
if($result -ne $null) 
{ 
    $Outputreport = "<HTML><TITLE>Central login Monitoring Report</TITLE><BODY background-color:peachpuff><font color =""#99000"" face=""Microsoft Tai le""><H2> Central login Monitoring Report </H2></font><Table border=1 cellpadding=0 cellspacing=0><TR bgcolor=gray align=center><TD><B>Region</B></TD><TD><B>URL</B></TD><TD><B>StatusCode</B></TD><TD><B>StatusDescription</B></TD><TD><B>ResponseLength</B></TD><TD><B>TimeTaken</B></TD</TR>" 
    Foreach($Entry in $Result) 
    { 
        if($Entry.StatusCode -ne "200") 
        { 
            $Outputreport += "<TR bgcolor=red>" 
        } 
        else 
        { 
            $Outputreport += "<TR>" 
        } 
        $Outputreport += "<TD>$($Entry.Region)</TD><TD>$($Entry.uri)</TD><TD align=center>$($Entry.StatusCode)</TD><TD align=center>$($Entry.StatusDescription)</TD><TD align=center>$($Entry.ResponseLength)</TD><TD align=center>$($Entry.timetaken)</TD></TR>" 
    } 
    $Outputreport += "</Table></BODY></HTML>" 
} 
 
$Outputreport | out-file "C:\CentralLoginMonitoring.html" 
#Invoke-Expression D:\Users\kbokshi\Desktop\Test3.html  
#$Outputreport
$From = "hpoperations.in@capgemini.com"
$To = "automationplatform.global@capgemini.com"
$Cc = @('krishanu.bokshi@capgemini.com','automationdevlead.global@capgemini.com')
$Attachment = "C:\CentralLoginMonitoring.html"
$Subject = "Utility -Central login page monitoring from Toltec DMZ"
$Body = "
Hello Team,
Below is the report for monitoring central login page from Toltec DMZ central.
$Outputreport"
$SMTPServer = "10.19.210.19"
$SMTPPort = "25"
Send-MailMessage -From $From -to $To -Cc $Cc -Subject $Subject -BodyAsHtml $Body -SmtpServer $SMTPServer -port $SMTPPort -Credential $Credential -Attachments $Attachment

