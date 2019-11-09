#The HTML Thing
#Cameron Ridderikhoff  
#March 16, 2017
#Lab 8
def main():
    f=open("input.txt", "r")
    long=f.read()
    lineList=long.splitlines()
    IDs=[]
    grades=[]
    highest=0
    lowest=100
    average=0
    z_9=0
    tn_19=0
    tw_29=0
    th_39=0
    f_49=0
    fv_59=0
    s_69=0
    sv_79=0
    e_89=0
    n_100=0
    for line in lineList:
        idgrade=line.split(" ")
        IDs.append(idgrade[0])
        grades.append(int(idgrade[1]))
        if grades[-1]>highest:
            highest=grades[-1]
        if grades[-1]<lowest:
            lowest=grades[-1]
            
        if grades[-1]>=0 and grades[-1]<10:
            z_9+=1
        elif grades[-1]>=10 and grades[-1]<20:
            tn_19+=1
        elif grades[-1]>=20 and grades[-1]<30:
            tw_29+=1
        elif grades[-1]>=30 and grades[-1]<40:
            th_39+=1
        elif grades[-1]>=40 and grades[-1]<50:
            f_49+=1
        elif grades[-1]>=50 and grades[-1]<60:
            fv_59+=1
        elif grades[-1]>=60 and grades[-1]<70:
            s_69+=1
        elif grades[-1]>=70 and grades[-1]<80:
            sv_79+=1
        elif grades[-1]>=80 and grades[-1]<90:
            e_89+=1
        else:
            n_100+=1
            
        average+=grades[-1]
    average=average/len(lineList)
    z_9H=str(10*z_9)+"px"
    tn_19H=str(10*tn_19)+"px"
    tw_29H=str(10*tw_29)+"px"
    th_39H=str(10*th_39)+"px"
    f_49H=str(10*f_49)+"px"
    fv_59H=str(10*fv_59)+"px"
    s_69H=str(10*s_69)+"px"
    sv_79H=str(10*sv_79)+"px"
    e_89H=str(10*e_89)+"px"
    n_100H=str(10*n_100)+"px"
    html=open("index.htm", "w")
    
    html.write("<html>")
    html.write("<body>")
    html.write("<h1>Welcome To EClass, But Better!</h1>")
    html.write("<p>  The maximum is "+str(highest)+".")
    html.write("	 The minimum is "+str(lowest)+".")
    html.write("	 The average is "+str(average)+"</p>")
    
    html.write("<table>")
    html.write("	<tr>")
    
    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+z_9H+";background:blue;border:1px solid red;'></div>")
    html.write("			[0-9]")
    html.write("		</td>")
    
    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+tn_19H+";background:blue;border:1px solid red;'></div>")
    html.write("			[10-19]")
    html.write("		</td>")
            
    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+tw_29H+";background:blue;border:1px solid red;'></div>")
    html.write("			[20-29]")
    html.write("		</td>")  
    
    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+th_39H+";background:blue;border:1px solid red;'></div>")
    html.write("			[30-39]")
    html.write("		</td>")

    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+f_49H+";background:blue;border:1px solid red;'></div>")
    html.write("			[40-49]")
    html.write("		</td>")

    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+fv_59H+";background:blue;border:1px solid red;'></div>")
    html.write("			[50-59]")
    html.write("		</td>")
    
    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+s_69H+";background:blue;border:1px solid red;'></div>")
    html.write("			[60-69]")
    html.write("		</td>")
    
    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+sv_79H+";background:blue;border:1px solid red;'></div>")
    html.write("			[70-79]")
    html.write("		</td>")

    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+e_89H+";background:blue;border:1px solid red;'></div>")
    html.write("			[80-89]")
    html.write("		</td>")    

    html.write("		<td valign='bottom'>")
    html.write("			<div style='width:30px;height:"+n_100H+";background:blue;border:1px solid red;'></div>")
    html.write("			[90-100]")
    html.write("		</td>")
    html.write("	</tr>")
    html.write("</table>")
    
    html.write("</body>")
    html.write("</html>")
    html.close()
    
main()