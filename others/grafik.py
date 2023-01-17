import turtle
import mysql.connector

# Koneksi ke database MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="rangga",
    password="rangga",
    database="test"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT x, y FROM grafik ORDER BY id")
data = mycursor.fetchall()

# Inisialisasi turtle
t = turtle.Turtle()
t.screen.title("Grafik Sumbu X Y")
t.speed(0)

# Plot data
for point in data:    
    x = point[0]
    y = point[1]
    t.goto(x, y)
    t.dot()

#Tunjukkan jendela turtle
t.screen.mainloop()
