1. ✅ OneToOneField
One object is related to exactly one other object.

🔹 Example:
One User has one Profile.
One Student has one ID Card.
class User(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
🧠 Real-life Analogy:
ഒരു ആളിന് ഒരു Aadhaar card മാത്രമേ ഉണ്ടാകൂ — അവയും പരസ്പരം ഇണച്ചിരിക്കുന്നത്.

🌐 Malayalam:
OneToOneField എന്നു പറയുന്നത് ഒരു model-നു ഒരു related model മാത്രമേ ഉണ്ടാകൂ എന്നർത്ഥമാണ്. ഉദാഹരണം: ഒരു user-ന് ഒരു profile മാത്രം.

2. ✅ ForeignKey (Many-to-One)
Many objects relate to one object.

🔹 Example:
Many Students belong to one Classroom.

Many Posts are written by one Author.
class Classroom(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
🧠 Real-life Analogy:
ഒരു teacher-നു അനേകം students ഉണ്ട് — പക്ഷേ student ഒരേ teacher-നോടാണ് reporting ചെയ്യുന്നത്.

🌐 Malayalam:
ForeignKey ആണ് most commonly ഉപയോഗിക്കുന്ന relation. പല objects-um ഒരേ parent-ൽ ചേർക്കുന്നത് പോലെ. ഉദാഹരണം: പല students-യും ഒരു class-ൽ പഠിക്കുന്നു.

3. ✅ ManyToManyField
Many objects are related to many other objects.

🔹 Example:
A Student can enroll in many Courses.

A Post can have many Tags, and each Tag can belong to many posts.
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course')

class Course(models.Model):
    title = models.CharField(max_length=100)
🧠 Real-life Analogy:
ഒരാൾക്ക് പല SIM cards ഉണ്ട്, അതുപോലെ ഒരു SIM പല ഫോണിലും ഉപയോഗിക്കാം.

🌐 Malayalam:
ManyToManyField-ൽ ഒരേ object-നെ പലതുമായി connect ചെയ്യാം. ഉദാഹരണം: ഒരാളെ പല course-ൽ join ചെയ്യാം, course-ൽ പല ആളും join ചെയ്യാം.

✅ Summary Table:
Relationship	Description	Example	Malayalam
OneToOneField	One-to-one	User ↔ Profile	ഒരാൾക്ക് ഒരു Aadhaar
ForeignKey	Many-to-one	Student → Classroom	പല വിദ്യാർത്ഥികൾക്കും ഒരു ക്ലാസ്
ManyToManyField	Many-to-many	Student ↔ Course	ഒരാൾക്ക് പല കോഴ്സുകളും, കോഴ്സിൽ പല ആളുകളും